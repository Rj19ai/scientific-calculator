import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    print("Scientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Logarithm")
    print("4. Power Function")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        num = float(input("Enter a number: "))
        print(f"Square root: {square_root(num)}")

    elif choice == 2:
        num = int(input("Enter a number: "))
        print(f"Factorial: {factorial(num)}")

    elif choice == 3:
        num = float(input("Enter a number: "))
        print(f"Natural Log: {natural_log(num)}")

    elif choice == 4:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"Power: {power(base, exponent)}")

    else:
        print("Exiting program. Thanks again!!")
