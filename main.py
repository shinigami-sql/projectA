import plot_engine  # plotting engine — generates polygon coordinates using numpy, plots figures in 2D and 3D with rotation
import constants # holds all static message strings used across main.py, keeps logic and text separate

# logfile_generator sets up the activity log for the entire session
# it sets up the connection — it tells Python where to write, 
# what format, and what minimum level. Think of it as opening and configuring the file.
from loggers import logfile_generator

# logging module, used here to write to the activity log configured in logfile_generator
# it provides the write functions, logging.info(), logging.warning() and logging.error(), 
# that send entries to the file opened and configured by logfile_generator
import logging  

from loggers import session_logger # session logger, writes one JSON entry per plot to the session file

# input_handler.py handles all user input validation and control flow, 
# imported here to access get_dimension, get_triangle_option and run_again
import input_handler

logging.info(constants.session_initiation_message)
print(constants.welcome_message)
print(constants.list_of_figures)
print(f'\n{constants.exit_instructions_message}\n')

# plot_turn tracks how many figures have been plotted in the current session, incremented each time run_again() is called
plot_turn = 1

def main():
    try: 

        # while True loops indefinitely, only exits when break is hit
        # every time the loop completes its final condition without hitting break, it returns to the top
        while True:
            choice = input("")
            if choice == "Triangle" or choice == 'triangle':

                dimension = input_handler.get_dimension()
                print(constants.initial_triangle_message, '\n')
                triangle_option = input_handler.get_triangle_option()

                if triangle_option.lower() == 'i':
                    vertex_angles = [90, 225, 315]
                    plot_engine.generate_angles(dimension, vertex_angles)

                    # required to write to the log file, without calling logging.info() the log file is created but nothing is written to it, configured in logfile_generator
                    logging.info(f'Isosceles Triangle plotted in {dimension}') 

                    session_logger.generate_session_json(plot_turn, choice, dimension, triangle_type=triangle_option)
                    session_logger.insert_into_db(plot_turn, choice, dimension, triangle_type=triangle_option)
                    logging.info(f'{constants.plot_logged_logfile_message}')
                    logging.info(f'{constants.db_insert_message}')

                    if not run_again():
                        break

    
                elif triangle_option.lower() == 'e': 
                    vertex_angles = [90, 210, 330]
                    plot_engine.generate_angles(dimension, vertex_angles)
                    logging.info(f'Equilateral Triangle plotted in {dimension}')

                    session_logger.generate_session_json(plot_turn, choice, dimension, triangle_type=triangle_option)
                    session_logger.insert_into_db(plot_turn, choice, dimension, triangle_type=triangle_option)
                    logging.info(f'{constants.plot_logged_logfile_message}')
                    logging.info(f'{constants.db_insert_message}')

                    
                    if not run_again():
                        break
                    

                # right triangle cannot use the circle formula since its vertices are not evenly spaced around a circle
                # the 90 degree corner requires two perpendicular sides which cannot be generated with equal angle spacing
                # x and y are hardcoded directly here instead of using plot_engine
                elif triangle_option.lower() == 'r':
                    x = [1, 1, 9, 1]  
                    y = [1, 9, 1, 1]

                    plot_engine.plot_figures(dimension, x, y)
                    logging.info(f'Right Triangle plotted in {dimension}')

                    session_logger.generate_session_json(plot_turn, choice, dimension, triangle_type=triangle_option)
                    session_logger.insert_into_db(plot_turn, choice, dimension, triangle_type=triangle_option)
                    logging.info(f'{constants.plot_logged_logfile_message}')
                    logging.info(f'{constants.db_insert_message}')

                    if not run_again():
                        break
                    



             # using keyword argument for amount_of_vertices applies to figures that don't have hardcoded vertex_angles
             # since dimension is the only required parameter, 
             # passing amount_of_vertices positionally would land on the wrong parameter    
            elif choice.lower() == 'square':
                dimension = input_handler.get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=4)

                logging.info(f'Square plotted in {dimension}')

                session_logger.generate_session_json(plot_turn, choice, dimension)
                session_logger.insert_into_db(plot_turn, choice, dimension)
                logging.info(f'{constants.plot_logged_logfile_message}')
                logging.info(f'{constants.db_insert_message}')
                
                # run_again() returns True if user wants to continue, False if not
                # if not False (user said no) the condition is True and we break
                #if not True (user said yes) the condition is False and the loop continues, back to 'while True'
                if not run_again():
                    break
                



            elif choice.lower() == 'pentagon':
                dimension = input_handler.get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=5)
                logging.info(f'Pentagon plotted in {dimension}')

                session_logger.generate_session_json(plot_turn, choice, dimension)
                session_logger.insert_into_db(plot_turn, choice, dimension)
                logging.info(f'{constants.plot_logged_logfile_message}')
                logging.info(f'{constants.db_insert_message}')
                
                if not run_again():
                    break
               

            elif choice.lower() == 'hexagon':
                dimension = input_handler.get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=6)
                logging.info(f'Hexagon plotted in {dimension}')

                session_logger.generate_session_json(plot_turn, choice, dimension)
                session_logger.insert_into_db(plot_turn, choice, dimension)
                logging.info(f'{constants.plot_logged_logfile_message}')
                logging.info(f'{constants.db_insert_message}')
                
                if not run_again():
                    break
          

            elif choice.lower() == 'heptagon':
                dimension = input_handler.get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=7)
                logging.info(f'Heptagon plotted in {dimension}')

                session_logger.generate_session_json(plot_turn, choice, dimension)
                session_logger.insert_into_db(plot_turn, choice, dimension)
                logging.info(f'{constants.plot_logged_logfile_message}')
                logging.info(f'{constants.db_insert_message}')

                
                if not run_again():
                    break
               

            elif choice.lower() == 'octagon':
                dimension = input_handler.get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=8)
                logging.info(f'Octagon plotted in {dimension}')

                session_logger.generate_session_json(plot_turn, choice, dimension)
                session_logger.insert_into_db(plot_turn, choice, dimension)
                logging.info(f'{constants.plot_logged_logfile_message}')
                logging.info(f'{constants.db_insert_message}')
                
                if not run_again():
                    break
              

            elif choice.lower() == 'exit':
                print(f'\n{constants.exit_message}\n')
                logging.info('User ended the session without plotting any figure')
                break

            else:
                print(constants.failed_selecting_figure_1_message)
                logging.warning('User entered an invalid figure name') # logging.warning() logs unexpected but non-critical behavior, such as invalid user input
                print(constants.list_of_figures, '\n')

    # triggered when user hits Ctrl+C mid execution
    except KeyboardInterrupt as e:
        # f-string, embeds variables directly inside the string using {}, cleaner alternative to .format()
        print(f'\n{constants.keyboard_interrupt_message}\n')
        logging.error(f'KeyboardInterrupt: {e}') # logging.error() # logs errors, captures the exception object with 'as e' for the exact error message

    # triggered when an unexpected value is passed to a function, such as a string where a number is expected
    except ValueError as e:
        print(f'\n{constants.value_error_message}\n')
        logging.error(f'ValueError: {e}')

    except NameError as e:
        print(f'\n{constants.name_error_message}\n')
        logging.error(f'NameError: {e}')

    # catch-all for any unexpected runtime error not covered by KeyboardInterrupt or ValueError
    # covers errors from plot_engine, matplotlib, numpy, or anything else that crashes at runtime
    except Exception as e:
        print(f'\n{constants.exception_message}\n')
        logging.error(f'Exception: {e}')

# asks the user if they want to plot another figure
# validates input, loops until Y or N is entered
# returns True if they say yes and prints the figure list, False if they say no and prints session ended message
# used with 'if not run_again()' to decide whether to break the loop or continue
def run_again():

    # global declares that plot_turn refers to the module-level variable defined outside this function
    # without global, Python would treat plot_turn as a new local variable and throw an UnboundLocalError
    # also, global is needed here since we're modifying the variable, if that wasn't the case we wouldn't call it
    global plot_turn
    plot_turn += 1
    
    answer = input(constants.retry_message)
    logging.info('User prompted to plot another figure')
    while answer.lower() not in ['y', 'n']:
        print('Y/N only')
        answer = input(constants.retry_message)

    if answer.lower() == 'y':
        print(f'\n{constants.list_of_figures}\n')
        logging.info('User chose to plot another figure')
        return True
    else:
        print(f'\n{constants.no_try_again_message}\n')
        logging.info('User decided not to plot another figure and ended the session')
        return False

if __name__ == '__main__':
    main()


