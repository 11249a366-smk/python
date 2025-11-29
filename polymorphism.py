class PalindromeChecker:
    def is_palindrome(self, value):
        raise NotImplementedError

class StringPalindromeChecker(PalindromeChecker):
    def is_palindrome(self, value):
        value = value.lower().replace(" ", "")
        return value == value[::-1]

class IntegerPalindromeChecker(PalindromeChecker):
    def is_palindrome(self, value):
        s = str(value)
        return s == s[::-1]

input_value = input("Enter a value: ")

if input_value.isdigit():
    checker = IntegerPalindromeChecker()
    print(checker.is_palindrome(int(input_value)))
else:
    checker = StringPalindromeChecker()
    print(checker.is_palindrome(input_value))
