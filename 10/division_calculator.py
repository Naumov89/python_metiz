###################################################

# print(5 / 0)

###################################################

# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

######################################################

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to exit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

############################################################

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:   # любой успешный код добавляется в блок else
        print(answer)