#Author: Tejas Tondase (100947705)
#Date: 2024-10-11
#Description: This Python program checks if a user-inputted number is prime, finds the closest prime numbers before and after it, and lists divisors if the number is not prime.

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def previous_prime_number(n):
    for i in range(n - 1, 1, -1):
        if is_prime_number(i):
            return i
    return None

def next_prime_number(n):
    i = n + 1
    while True:
        if is_prime_number(i):
            return i
        i += 1

def divisors(n):
    return [i for i in range(2, n) if n % i == 0]

def main():
    while True:
        try:
            number = int(input("Please enter a positive whole number: "))
            if number < 1:
                print("That is not a positive whole number. Try again.")
                continue
            break
        except ValueError:
            print("That is not a positive whole number. Try again.")

    prev_prime = previous_prime_number(number)
    if prev_prime:
        print(f"\nThe prime number before {number} is {prev_prime}.")
    else:
        print(f"\nThere is no prime number before {number}.")

    if is_prime_number(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not prime. Its factors are {divisors(number)}.")

    print(f"The prime number after {number} is {next_prime_number(number)}.")

    input("\nPress Enter to exit the program...")

if __name__ == "__main__":
    main()
