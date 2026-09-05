import random  # built-in Python module, used here to randomly select figures, dimensions and triangle types
import sys  # built-in Python module, provides access to interpreter variables and functions
import os   # built-in Python module, provides functions to interact with the operating system and file system

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

from loggers import session_logger # handles JSON and PostgreSQL logging, imported here to call generate_session_json with random data
import constants  # holds all static message strings and lists, imported here to access list_of_figures and data_generation_complete_message


# loops 100 times generating random figure, dimension and triangle type
# calls insert_into_db to send each entry to the PostgreSQL database
# prints completion message with total records inserted once the loop finishes

iterations = 0

while iterations != 1:
	turn = iterations
	figure = random.choice(constants.list_of_figures)
	dimension = random.choice(['2d', '3d'])
	triangle_type = None
	if figure.lower() == 'triangle':
		triangle_type = random.choice(['i', 'r', 'e'])


	session_logger.insert_into_db(turn, figure, dimension, triangle_type=triangle_type)
	iterations +=1


print(constants.data_generation_complete_message.format(iterations))