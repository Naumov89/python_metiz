
# filename = '/home/oleksandr/Desktop/python_work/10/learning_python.txt'

# with open(filename) as file_object:
#     content = file_object.read()

# print(content.rstrip())

################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/learning_python.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#################################################################################

filename = '/home/oleksandr/Desktop/python_work/10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

python_strings = ''
for line in lines:
    python_strings += line

print(python_strings)

