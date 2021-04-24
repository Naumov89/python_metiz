
# def counts_words(filename):
#     with open(filename, encoding='utf-8') as f:
#         contens = f.read()
#         counts = contens.count('the')
#         print(counts)


# filenames = [
#         '/home/oleksandr/Desktop/python_work/10/blue.txt',
#         '/home/oleksandr/Desktop/python_work/10/negro.txt',
#         '/home/oleksandr/Desktop/python_work/10/protocols.txt'
#         ]

# for filename in filenames:
#     counts_words(filename)

#######################################################################

# def counts_words(filename):
#     with open(filename, encoding='utf-8') as f:
#         contens = f.read()
#         counts = contens.lower().count('the')
#         print(counts)


# filenames = [
#         '/home/oleksandr/Desktop/python_work/10/blue.txt',
#         '/home/oleksandr/Desktop/python_work/10/negro.txt',
#         '/home/oleksandr/Desktop/python_work/10/protocols.txt'
#         ]

# for filename in filenames:
#     counts_words(filename)

#########################################################################

def counts_words(filename):
    with open(filename, encoding='utf-8') as f:
        contens = f.read()
        counts = contens.lower().count('the ')
        print(counts)


filenames = [
        '/home/oleksandr/Desktop/python_work/10/blue.txt',
        '/home/oleksandr/Desktop/python_work/10/negro.txt',
        '/home/oleksandr/Desktop/python_work/10/protocols.txt'
        ]

for filename in filenames:
    counts_words(filename)