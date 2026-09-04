import session_logger # handles JSON and PostgreSQL logging, imported here to call generate_session_json with random data
import random  # built-in Python module, used here to randomly select figures, dimensions and triangle types
import constants  # holds all static message strings and lists, imported here to access list_of_figures and data_generation_complete_message

# loops 100 times generating random figure, dimension and triangle type
# calls insert_into_db to send each entry to the PostgreSQL database
# prints completion message with total records inserted once the loop finishes

iterations = 0

while iterations != 150:
	turn = iterations
	figure = random.choice(constants.list_of_figures)
	dimension = random.choice(['2d', '3d'])
	triangle_type = None
	if figure.lower() == 'triangle':
		triangle_type = random.choice(['i', 'r', 'e'])


	session_logger.insert_into_db(turn, figure, dimension, triangle_type=triangle_type)
	iterations +=1


print(constants.data_generation_complete_message.format(iterations))