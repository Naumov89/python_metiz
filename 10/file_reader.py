##################################################################################

# with open('/home/oleksandr/Desktop/python_work/10/pi_digits.txt') as file_object:
#     contens = file_object.read()
#     print(contens.rstrip())

##################################################################################

# file_path = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'
# with open (file_path) as file_object:
#     contens = file_object.read()
#     print(contens.rstrip())

##################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

##################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

###################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

###################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))

####################################################################################

filename = '/home/oleksandr/Desktop/python_work/10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))