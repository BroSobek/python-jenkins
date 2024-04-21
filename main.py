import random

def generate_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def sum_and_print(num1, num2):
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")
    return total

if __name__ == "__main__":
    num1, num2 = generate_random_numbers()
    total = sum_and_print(num1, num2)
