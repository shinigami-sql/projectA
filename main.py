print('\n')
print('''Welcome to the PLOT-ter!

Select a figure below and we will build it for you:
''')

list_of_figures = ['Triangle', 'Square', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon']
print(list_of_figures, '\n')

while True:
    choice = input("")
    if choice == "Triangle":
        print('Three corners? Not bad...')
        break
    elif choice == 'Square':
        print('Four corners? Look at ya!')
        break
    elif choice == 'Pentagon':
        print('Secretary of Defense? Roger that!')
        break
    elif choice == 'Hexagon':
        print('Honeycombs? Sweet!')
        break
    elif choice == 'Heptagon':
        print('Mathematical?')
        break
    elif choice == 'Octagon':
        print('You want to start a fight?')
        break
    elif choice == 'Exit' or choice == 'exit':
        print('Have a nice day!')
        break
    else:
        print('\n')
        print('From the list, a figure select you must, my young Padawan.' , '\n')
        print(list_of_figures)
        print('\n')





