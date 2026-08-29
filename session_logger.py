import json # built-in Python module, provides methods to convert between Python dictionaries and JSON strings
from datetime import datetime # datetime class from the datetime library, used here to dynamically name the log file with today's date
import os # operating system module, provides functions to interact with the file system and OS

# creates the json directory if it doesn't exist and 'exist_ok=True' prevents error if folder already exists
os.makedirs('projectA_sessions', exist_ok=True)

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

