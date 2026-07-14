print('\n')
print('''Welcome to the PLOT-ter!

Select a figure below and we will build it for you:
''')

list_of_figures = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon']
print(list_of_figures, '\n')

choice = input("")

if choice == "Triangle":
        print('Three corners? Not bad...')
    elif choice == 'Square':
        print('Four corners? Look at ya!')
    elif choice == 'Pentagon':
        print('Secretary of Defense? Roger that!')
    elif choice == 'Hexagon':
        print('Honeycombs? Sweet!')
    elif choice == 'Heptagon':
        print('Mathematical?')
    elif choice == 'Octagon':
        print('You want to start a fight?')
    else:
        print('Match must the figure name, or error you will get my young Padawan')




