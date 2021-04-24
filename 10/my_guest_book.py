
filename = '/home/oleksandr/Desktop/python_work/10/guest_book.txt'
message = ''
with open(filename, 'a') as file_object:
    message = ''
    while message != 'q':
        message = input("Enter 'q' to exit!\nEnter your name: ")
        if message != 'q':
            file_object.write(f"{message}\n")

