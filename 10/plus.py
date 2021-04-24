
print("Give me two numbers, and I'll addition them.")

try:
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    answer = int(first_number) + int(second_number)
    print(f"Result: {answer}")
except ValueError:
    print("Numbers cannot be added!")
