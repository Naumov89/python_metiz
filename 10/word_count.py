
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contens = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#     else:
#         # Подсчет приблизительного количества слов
#         words = contens.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

# # filename = '/home/oleksandr/Desktop/python_work/10/alice.txt'
# # count_words(filename)

# filenames = [
#         '/home/oleksandr/Desktop/python_work/10/alice.txt',
#         '/home/oleksandr/Desktop/python_work/10/little_women.txt',
#         '/home/oleksandr/Desktop/python_work/10/moby_dick.txt',
#         '/home/oleksandr/Desktop/python_work/10/siddhartha.txt',
#         '/home/oleksandr/Desktop/python_work/10/sida.txt'
#         ]

# for filename in filenames:
#     count_words(filename)

##########################################################################

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contens = f.read()
    except FileNotFoundError:
        pass     # Команда при которой в Python, блок  ничего не делает
    else:
        # Подсчет приблизительного количества слов
        words = contens.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = [
        '/home/oleksandr/Desktop/python_work/10/alice.txt',
        '/home/oleksandr/Desktop/python_work/10/little_women.txt',
        '/home/oleksandr/Desktop/python_work/10/moby_dick.txt',
        '/home/oleksandr/Desktop/python_work/10/siddhartha.txt',
        '/home/oleksandr/Desktop/python_work/10/sida.txt'
        ]

for filename in filenames:
    count_words(filename)