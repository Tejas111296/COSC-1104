def sum_of_digits(number):
    """
    Takes an integer and returns the sum of its individual digits.
    """
    return sum(int(digit) for digit in str(abs(number)))

# Test cases
if __name__ == "__main__":
    # Positive number
    print(sum_of_digits(12345))  # Expected output: 15 (1 + 2 + 3 + 4 + 5)
    
    # Negative number (ignores the sign)
    print(sum_of_digits(-987))  # Expected output: 24 (9 + 8 + 7)
    
    # Single digit
    print(sum_of_digits(5))  # Expected output: 5