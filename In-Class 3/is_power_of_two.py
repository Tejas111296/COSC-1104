def is_power_of_two(number):
    """
    Returns True if the number is a power of two, False otherwise.
    A number is a power of two if there exists an integer x such that 2^x = number.
    """
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

# Test cases
if __name__ == "__main__":
    # Power of two cases
    print(is_power_of_two(2))    # Expected output: True
    print(is_power_of_two(16))   # Expected output: True
    print(is_power_of_two(64))   # Expected output: True

    # Non-power of two cases
    print(is_power_of_two(10))   # Expected output: False
    print(is_power_of_two(-2))   # Expected output: False