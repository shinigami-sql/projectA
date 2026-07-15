import figures  # Figures module — holds the DataFrame containing figure names and their corresponding data points


print('\n')
print('''Welcome to ProjectA

Select a figure to retrieve its data points:
''')

list_of_figures = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon']
print(list_of_figures, '\n')
print('To leave at any time, type \'Exit\'.', '\n')

while True:
    choice = input("")
    print('\n')
    if choice == "Triangle" or choice == 'triangle':
        print('Three corners? Bold choice... but which kind? Not as simple as you thought, huh?', '\n')
        triangle_option = input('Isosceles Triangle (I), Equilateral Triangle (E) or Right Triangle (R)? \n')
        if triangle_option == 'I' or triangle_option == 'Isoceles Triangle' or triangle_option == 'Isoceles':
            print(figures.figures_df.loc['Isosceles Triangle'])
            break
        elif triangle_option == 'E' or triangle_option == 'Equilateral Triangle' or triangle_option == 'Equilateral':
            print(figures.figures_df.loc['Equilateral Triangle'])
            break
        elif triangle_option == 'R' or triangle_option == 'Right Triangle' or triangle_option == 'Right':
            print(figures.figures_df.loc['Right Triangle'])
            break
    elif choice == 'Square' or choice == 'square':
        print('Four corners? Look at ya!')
        print(figures.figures_df.loc['Square'])
        break
    elif choice == 'Pentagon' or choice == 'pentagon':
        print('Secretary of Defense? Roger that!')
        print(figures.figures_df.loc['Pentagon'])
        break
    elif choice == 'Hexagon' or choice == 'hexagon':
        print('Honeycombs? Sweet!')
        print(figures.figures_df.loc['Hexagon'])
        break
    elif choice == 'Heptagon' or choice == 'heptagon':
        print('Mathematical?')
        print(figures.figures_df.loc['Heptagon'])
        break
    elif choice == 'Octagon' or choice == 'octagon':
        print('You want to start a fight?')
        print(figures.figures_df.loc['Octagon'])
        break
    elif choice == 'Exit' or choice == 'exit':
        print('Have a nice day!')
        break
    else:
        print('\n')
        print('From the list, a figure select you must, my young Padawan.' , '\n')
        print(list_of_figures)
        print('\n')





