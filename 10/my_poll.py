
filename = '/home/oleksandr/Desktop/python_work/10/poll.txt'

with open(filename, 'a') as file_object:
    message = ''
    while message != 'q':
        text = "Enter 'q' to exit!\nWhy do you like programming? "
        message = input(text)
        if message != 'q':
            file_object.write(f"{message}\n")


