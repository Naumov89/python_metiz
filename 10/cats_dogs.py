
# def cats_dogs(filename):
#     try:
#         with open(filename) as f:
#             contens = f.read()
#             print(contens)
#     except FileNotFoundError:
#         print(f"File not Found - {filename}.")

# filename = '/home/oleksandr/Desktop/python_work/10/cats.txt'
# cats_dogs(filename)

# filename = '/home/oleksandr/Desktop/python_work/10/dogs.txt'
# cats_dogs(filename)

# filename = '/home/oleksandr/Desktop/python_work/10/cats_dogs.txt'
# cats_dogs(filename)

#########################################################################

def cats_dogs(filename):
    try:
        with open(filename) as f:
            contens = f.read()
            print(contens)
    except FileNotFoundError:
        pass

filename = '/home/oleksandr/Desktop/python_work/10/cats.txt'
cats_dogs(filename)

filename = '/home/oleksandr/Desktop/python_work/10/dogs.txt'
cats_dogs(filename)

filename = '/home/oleksandr/Desktop/python_work/10/cats_dogs.txt'
cats_dogs(filename)


