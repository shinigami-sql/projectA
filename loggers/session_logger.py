import json # built-in Python module, provides methods to convert between Python dictionaries and JSON strings
from datetime import datetime # datetime class from the datetime library, used here to dynamically name the log file with today's date
import os # operating system module, provides functions to interact with the file system and OS
import sys  # built-in Python module, provides access to interpreter variables and functions

# creates the json directory if it doesn't exist and 'exist_ok=True' prevents error if folder already exists
os.makedirs('projectA_sessions', exist_ok=True)

# __file__ is a built-in Python variable automatically set to the path of this file as a string
# os.path.abspath(__file__) takes that string and converts it into a guaranteed full absolute path
# os.path.dirname() strips the last item in the path, calling it twice goes 2 levels up
# first dirname: strips the filename, leaves the folder this file is in
# second dirname: strips that folder, leaves projectA/ which is the project root
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sys.path is Python's list of directories it searches in order when you do an import
# it includes the current directory, venv site-packages, and system Python directories
# sys.path.insert(0, root) adds projectA/ to position 0, the front of that list
# insert doesn't replace anything, it shifts everything else down one position
# position 0 means Python checks projectA/ first before any other directory
# without this, scripts in subfolders can't find modules in other folders
sys.path.insert(0, root)

from data import db_connector # establishes the PostgreSQL connection and cursor on import, Python equivalent of psql connecting to the server

# session_filename is defined at module level so it is generated once on import and 
# reused across all calls to generate_session_json, ensuring all entries from the same session go to the same file, 
# global is not needed since session_filename is only read inside the function, not modified
session_file = f'projectA_sessions/{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}_session.json'

# for generate_json
# strftime format codes used in this project:
# %Y: 4-digit year e.g. 2026, %y: 2-digit year e.g. 26
# %m: month as number e.g. 08, %M: minutes e.g. 45 — easy to mix up
# %d: day of month e.g. 24
# %H: 24-hour hour e.g. 14
# %S: seconds e.g. 01

def generate_session_json(turn, figure, dimension, triangle_type=None):

	# triangle_type is optional, defaults to None for non-triangle figures
	# 'triangle_type if triangle_type' means use the value if it exists (truthy), otherwise False
	# same pattern as 'True if condition else False' but using the value itself instead of True

	entry = {'Turn': turn, 'Figure' : figure, 'Triangle Type': triangle_type if triangle_type else False ,'Dimension' : dimension, 'Rotation' : True if dimension.lower() == '3d' else False, 'Datetime' : datetime.now().strftime("%Y-%m-%d %H-%M-%S")} 

	# json_file is the file object referencing the open json file
	# .write() is the file object method used to write to it
	# json.dumps(entry) converts the Python dictionary to a JSON string + '\n' 
	# adds a newline after each entry so each plot gets its own line

	# filename includes date and time to generate a unique file per session
	# preventing entries from different sessions being written to the same file

	with open(session_file, 'a') as json_file:
		json_file.write(json.dumps(entry) + '\n')

def insert_into_db(turn, figure, dimension, triangle_type=None): 
	# cursor.execute() sends the SQL INSERT statement to the PostgreSQL server through the open pipeline
	# the triple quoted string allows the SQL to span multiple lines without concatenation
	# %s are placeholders, psycopg2 replaces them in order with the values from the tuple below
	# the tuple uses the same function arguments as the JSON entry, applying the same conditional logic
	# db_connector.db_connection.commit() confirms and saves the transaction to the database

	db_connector.cursor.execute("""INSERT INTO plots (plot_turn, figure, triangle_type, dimension, rotation, date)
		VALUES (%s, %s, %s, %s, %s, %s)
		""", (turn, figure, triangle_type if triangle_type else None, dimension, True if dimension.lower() == '3d' else False, datetime.now()))

	# execute() sends the SQL to the server and processes it in a temporary transaction
	# commit() confirms and permanently saves it to the database
	# without commit() the transaction is rolled back when the connection closes, like it never happened
	db_connector.db_connection.commit()




