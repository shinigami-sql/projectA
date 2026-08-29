import constants
import logging

# validates triangle selection, loops until I, E or R is entered
# returns the valid option to be used in the triangle if/elif block
def get_triangle_option():
    triangle_option = input(constants.triangle_options_message) 
    logging.info('User prompted to select triangle type, Isosceles, Equilateral or Right')
    while triangle_option.lower() not in ['i', 'e', 'r']:
        logging.warning('User entered invalid triangle option, prompting again')
        print(f'\n{constants.select_correct_triangle_message}\n')
        triangle_option = input(constants.triangle_options_message) 
    return triangle_option



# loops until user enters a valid dimension, 2D or 3D
# while condition is True (input not in list) keep asking
# when input matches, condition becomes False and loop exits, returning the valid dimension
def get_dimension():
    dimension = input('\n2D or 3D? ')
    logging.info('User prompted to select dimension, 2D or 3D')
    while dimension.lower() not in ['2d', '3d']:
        logging.warning('User entered invalid dimension, prompting again')
        print(f'\n{constants.dimension_failed_retry_message}')
        dimension = input('\n2D or 3D? ')
    return dimension





