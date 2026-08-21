from matplotlib import pyplot as plt
import plot_engine  # Plotting engine — dynamically generates polygon coordinates using numpy and plots them

print('''\nWelcome to ProjectA

Select a figure to retrieve its data points:
''')

list_of_figures = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon']
print(list_of_figures, '\n')
print('To leave at any time, type \'Exit\'.', '\n')

def main():
    while True:
        choice = input("")
        if choice == "Triangle" or choice == 'triangle':
            dimension = input('\n2D or 3D? ')
            print('\nThree corners? Bold choice... but which kind? Not as simple as you thought, huh?', '\n')
            triangle_option = input('Isosceles Triangle (I), Equilateral Triangle (E) or Right Triangle (R)? ' )
            if triangle_option == 'I' or triangle_option == 'Isoceles Triangle' or triangle_option == 'Isoceles':
                vertex_angles = [90, 225, 315]
                plot_engine.generate_angles(dimension, vertex_angles, title_body='Two equal sides and an odd one.')
                break
            elif triangle_option == 'E' or triangle_option == 'Equilateral Triangle' or triangle_option == 'Equilateral':
                vertex_angles = [90, 210, 330]
                plot_engine.generate_angles(dimension, vertex_angles, title_body='All sides equal. Perfection!')
                break
            elif triangle_option == 'R' or triangle_option == 'Right Triangle' or triangle_option == 'Right':
                x = [1, 1, 9, 1]  
                y = [1, 9, 1, 1]
                plt.plot(x, y)
                plt.title('One 90° corner — the blueprint of every building.')

                # plt.axis('equal) added so a circle looks like a circle and a square looks like a square. 
                # Without plt.axis('equal' matplotlib auto-scales each axis independently and your shapes get stretched or squished.
                plt.axis('equal') 
                plt.show() # Renders and displays the active plot in a window
                break

         # Using keyword arguments for amount_of_vertices and title_body applies to figures 
         # that don't have hardcoded vertex_angles, 
         # since vertex_angles is the first required parameter and passing positionally would land on the wrong parameter       
        elif choice == 'Square' or choice == 'square':
            dimension = input('\n2D or 3D? ')
            plot_engine.generate_angles(dimension, amount_of_vertices=4, title_body='Four corners? Look at ya!')
            break
        elif choice == 'Pentagon' or choice == 'pentagon':
            dimension = input('\n2D or 3D? ')
            plot_engine.generate_angles(dimension, amount_of_vertices=5, title_body='Secretary of Defense? Roger that!')
            break
        elif choice == 'Hexagon' or choice == 'hexagon':
            dimension = input('\n2D or 3D? ')
            plot_engine.generate_angles(dimension, amount_of_vertices=6, title_body='Honeycombs? Sweet!')
            break
        elif choice == 'Heptagon' or choice == 'heptagon':
            dimension = input('\n2D or 3D? ')
            plot_engine.generate_angles(dimension, amount_of_vertices=7, title_body='Mathematical?')
            break
        elif choice == 'Octagon' or choice == 'octagon':
            dimension = input('\n2D or 3D? ')
            plot_engine.generate_angles(dimension, amount_of_vertices=8, title_body='You want to start a fight? Let\'s go McGregor!')
            break
        elif choice == 'Exit' or choice == 'exit':
            print('Have a nice day!')
            break
        else:
            print('\n')
            print('From the list, a figure select you must, my young Padawan.' , '\n')
            print(list_of_figures)
            print('\n')


if __name__ == '__main__':
    main()


