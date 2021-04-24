
# filename = '/home/oleksandr/Desktop/python_work/10/programing.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.')

#     # "w" - режим чтения
#     # "r" - режим записи
#     # "r+" - режим чтения и записи
#     # "a" - режим присоединения

########################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/programing1.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.')
#     file_object.write('I love creating new games.')

#########################################################################
# 1
# filename = '/home/oleksandr/Desktop/python_work/10/programing2.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.\n')
#     file_object.write('I love creating new games.\n')

#########################################################################
#2
filename = '/home/oleksandr/Desktop/python_work/10/programing2.txt'

with open(filename, 'a') as file_object:
    file_object.write('I olso love finding meaning in large datdsets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')