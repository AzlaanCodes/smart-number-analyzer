def even_odd(n):
    if n == 0:
        return "Zero is neither Even nor Odd"
    return "Even" if n % 2 == 0 else "Odd"


def positive_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def square_cube(n):
    return n ** 2, n ** 3


def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


while True:
    print("\n<----------------->")
    print("1. Check Even or Odd")
    print("2. Check Positive, Negative or Zero")
    print("3. Print Table of a Number")
    print("4. Square and Cube")
    print("5. Sum of first N numbers")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print(even_odd(num))

    elif choice == 2:
        num = int(input("Enter a number: "))
        print(positive_negative(num))

    elif choice == 3:
        num = int(input("Enter a number: "))
        print_table(num)

    elif choice == 4:
        num = int(input("Enter a number: "))
        sq, cu = square_cube(num)
        print(f"Square: {sq}")
        print(f"Cube: {cu}")

    elif choice == 5:
        num = int(input("Enter a number: "))
        print(f"Sum: {sum_of_numbers(num)}")

    elif choice == 6:
        print("Program Exited Successfully.")
        break

    else:
        print("Invalid choice. Try again.")
