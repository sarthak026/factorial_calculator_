import argparse

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def main():
    parser = argparse.ArgumentParser(description="Calculate the factorial of a number.")
    parser.add_argument("number", type=int, help="The number to calculate the factorial for.")
    
    args = parser.parse_args()
    number = args.number

    if number < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
