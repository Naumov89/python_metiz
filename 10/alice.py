#######################################################################
# Подсчет слов
# title = "Alice in Wonderland"
# split_words = title.split()
# num_words = len(title.split())

# print(title)
# print(split_words)
# print(num_words)
# print(len(title))

#######################################################################

filename =  '/home/oleksandr/Desktop/python_work/10/alice.txt'
name_file = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contens = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Подсчет приблизительного количества слов
    words = contens.split()
    num_words = len(words)
    print(f"The file {name_file} has about {num_words} words.")