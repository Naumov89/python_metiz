
print("Give me two numbers, and I'll addition them.")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
        print(f"Result: {answer}")
    except ValueError:
        print("Numbers cannot be added!")