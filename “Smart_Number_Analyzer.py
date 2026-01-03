def even_odd(a):
    if a != 0:
        if a % 2 == 0:
            print("The number is Even")
        else:
            print("The Number is Odd")
    else:
        print("Zero is neither Even or Odd")
def positive_negative(a):
    if a > 0:
        print("The number is Positive")
    elif a == 0:
        print("The Number is Zero")
    else:
        print("The number is Negative")
def print_table(a):
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
def square_cube(a):
    print(f"The square of {a} is {a ** 2}")
    print(f"The cube of {a} is {a ** 3}")
def sum_of_number(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    print(f"The Sum of number is {sum}")
while True:
    print("     <----------------->")
    print("1. Check Even or Odd")
    print("2. Check Positive, Negative or Zero")
    print("3. Print Table of a Number")
    print("4. Square and Cube")
    print("5. Sum of first N numbers")
    print("6. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        num = int(input("Enter Any Number : "))
        even_odd(num)
    elif choice == 2:
        num = int(input("Enter Any Number : "))
        positive_negative(num)
    elif choice == 3:
        num = int(input("Enter Any Number : "))
        print_table(num)
    elif choice == 4:
        num = int(input("Enter Any Number : "))
        square_cube(num)
    elif choice == 5:
        num = int(input("Enter Any Number : "))
        sum_of_number(num)
    elif choice == 6:
        print("The Program is Exited")
        break
    else:
        print("You Entered invalid Choice")
    














































