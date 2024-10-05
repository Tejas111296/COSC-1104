def is_palindrome(word):
    """
    Returns True if the word is a palindrome (ignores punctuation and case).
    """
    # Normalize the string: remove spaces, punctuation and make it lowercase
    clean_word = ''.join(char.lower() for char in word if char.isalnum())
    # Compare the cleaned word to its reverse
    return clean_word == clean_word[::-1]

# Test cases
if __name__ == "__main__":
    # Palindrome case (ignores case and punctuation)
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True
    
    # Non-palindrome
    print(is_palindrome("Hello"))  # Expected output: False
    
    # Single character (considered palindrome)
    print(is_palindrome("A"))  # Expected output: True