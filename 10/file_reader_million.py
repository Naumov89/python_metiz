#################################################################################

# filename = '/home/oleksandr/Desktop/python_work/10/pi_million_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))

####################################################################################

filename = '/home/oleksandr/Desktop/python_work/10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appers in the first million digits of pi!")
else:
    print("Your birthday does not apper in the first million digits of pi!")