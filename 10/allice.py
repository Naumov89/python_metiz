
# filename =  '/home/oleksandr/Desktop/python_work/10/alice.txt'

# with open(filename, encoding='utf-8') as f:
#     contens = f.read()

##########################################################################


# filename =  '/home/oleksandr/Desktop/python_work/10/alice.txt'

# try:
#     with open(filename, encoding='utf-8') as f:
#         contens = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")

###########################################################################

# filename =  '/home/oleksandr/Desktop/python_work/10/alice.txt'
# file_alice = 'alice.txt'

# try:
#     with open(filename, encoding='utf-8') as f:
#         contens = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {file_alice} does not exist.")

###########################################################################

title = "Alice in Wonderland"
split_words = title.split()
num_words = len(title.split())

print(title)
print(split_words)
print(num_words)
print(len(title))