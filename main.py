from matplotlib import pyplot as plt
import plot_engine  # Plotting engine — generates polygon coordinates using numpy, plots figures in 2D and 3D with rotation
import constants # holds all static message strings used across main.py, keeps logic and text separate

print(constants.welcome_message)

print(constants.list_of_figures, '\n')
print(constants.exit_instructions_message, '\n')

def main():
    try: 
        # while True loops indefinitely, only exits when break is hit
        # every time the loop completes its final condition without hitting break, it returns to the top
        while True:
            choice = input("")
            if choice == "Triangle" or choice == 'triangle':

                dimension = get_dimension()
                print(constants.initial_triangle_message, '\n')
                triangle_option = get_triangle_option()

                if triangle_option.lower() == 'i':
                    vertex_angles = [90, 225, 315]
                    plot_engine.generate_angles(dimension, vertex_angles, title_body=constants.isoceles_body_title)

                    if not run_again():
                        break

    
                elif triangle_option.lower() == 'e': 
                    vertex_angles = [90, 210, 330]
                    plot_engine.generate_angles(dimension, vertex_angles, title_body=constants.equilateral_body_title)
                    
                    if not run_again():
                        break
                    

                # right triangle cannot use the circle formula since its vertices are not evenly spaced around a circle
                # the 90 degree corner requires two perpendicular sides which cannot be generated with equal angle spacing
                # x and y are hardcoded directly here instead of using plot_engine
                elif triangle_option.lower() == 'r':
                    x = [1, 1, 9, 1]  
                    y = [1, 9, 1, 1]
                    title_body = constants.right_triangle_body_title

                    plot_engine.plot_figures(dimension, x, y, title_body)
                    
                    if not run_again():
                        break
                    



             # Using keyword arguments for amount_of_vertices and title_body applies to figures 
             # that don't have hardcoded vertex_angles, 
             # since vertex_angles is the first required parameter and passing positionally would land on the wrong parameter       
            elif choice.lower() == 'square':
                dimension = get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=4, title_body=constants.square_body_title)
                
                # run_again() returns True if user wants to continue, False if not
                # if not False (user said no) the condition is True and we break
                #if not True (user said yes) the condition is False and the loop continues, back to 'while True'
                if not run_again():
                    break
                



            elif choice.lower() == 'pentagon':
                dimension = get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=5, title_body=constants.pentagon_body_title)
                
                if not run_again():
                    break
               

            elif choice.lower() == 'hexagon':
                dimension = get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=6, title_body=constants.hexagon_body_title)
                
                if not run_again():
                    break
          

            elif choice.lower() == 'heptagon':
                dimension = get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=7, title_body=constants.heptagon_body_title)
                
                if not run_again():
                    break
               

            elif choice.lower() == 'octagon':
                dimension = get_dimension()
                plot_engine.generate_angles(dimension, amount_of_vertices=8, title_body=constants.octagon_body_title)
                
                if not run_again():
                    break
              

            elif choice.lower() == 'exit':
                print(constants.exit_message)
                break

            else:
                print(constants.failed_selecting_figure_1_message)
                print(constants.list_of_figures, '\n')

    # triggered when user hits Ctrl+C mid execution
    except KeyboardInterrupt:
        # f-string, embeds variables directly inside the string using {}, cleaner alternative to .format()
        print(f'\n{constants.keyboard_interrupt_message}\n')

    # triggered when an unexpected value is passed to a function, such as a string where a number is expected
    except ValueError:
        print(f'\n{constants.value_error_message}\n')

    # catch-all for any unexpected runtime error not covered by KeyboardInterrupt or ValueError
    # covers errors from plot_engine, matplotlib, numpy, or anything else that crashes at runtime
    except Exception:
        print(f'\n{constants.exception_message}\n')


# validates triangle selection, loops until I, E or R is entered
# returns the valid option to be used in the triangle if/elif block
def get_triangle_option():
    triangle_option = input(constants.triangle_options_message) 
    while triangle_option.lower() not in ['i', 'e', 'r']:
        print(constants.correct_triangle_message)
        triangle_option = input(constants.triangle_options_message) 
    return triangle_option



# loops until user enters a valid dimension, 2D or 3D
# while condition is True (input not in list) keep asking
# when input matches, condition becomes False and loop exits, returning the valid dimension
def get_dimension():
    dimension = input('\n2D or 3D? ')
    while dimension.lower() not in ['2d', '3d']:
        print(constants.dimension_failed_retry_message)
        dimension = input('\n2D or 3D? ')
    return dimension


# asks the user if they want to plot another figure
# validates input, loops until Y or N is entered
# returns True if they say yes and prints the figure list, False if they say no and prints session ended message
# used with 'if not run_again()' to decide whether to break the loop or continue
def run_again():
    answer = input(constants.retry_message)
    while answer.lower() not in ['y', 'n']:
        print('Y/N only')
        answer = input(constants.retry_message)

    if answer.lower() == 'y':
        print(f'\n{constants.list_of_figures}\n')
        return True
    else:
        print(f'\n{constants.no_try_again_message}\n')
        return False


if __name__ == '__main__':
    main()


