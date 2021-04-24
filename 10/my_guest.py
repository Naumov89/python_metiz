
# filename = '/home/oleksandr/Desktop/python_work/10/guest.txt'

# with open(filename, 'w') as file_object:
#     name = input('Enter your name: ')
#     file_object.write(name)


filename = '/home/oleksandr/Desktop/python_work/10/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(input('Enter your name: '))

