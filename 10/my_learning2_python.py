
filename = '/home/oleksandr/Desktop/python_work/10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

python_strings = ''
for line in lines:
    python_strings += line.strip()

for python_string in python_strings.split('.'):
    print(python_string)

for python_string in python_strings.split('.'):
    print(python_string.replace('Python', 'C'))

