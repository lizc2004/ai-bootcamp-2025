# Scrivere il codice dell'esercizi qui dentro
def mydivmod(a, b):
    if b == 0:
        return "error: division by zero not allowed"
    else:
        quotient = a // b
        remainder = a % b
        return (quotient, remainder)

print(mydivmod(10, 2))


def pow_list(lst):
    return [x ** 2 for x in lst]
assert pow_list([1, 2, 3]) == [1, 4, 9]

def count_words(s):
    return len(s.split(' '))
assert count_words("hello world") == 2

def reverse_string(s):
    return s[::-1]
assert reverse_string("hello") == "olleh"
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
assert factorial(5) == 120
def is_palindrome(s):
    return s == s[::-1]
assert is_palindrome("racecar") == True

def sum_even_numbers(lst):
    return sum (x for x in lst if x % 2 == 0)
def find_max(lst):
    return max(lst)
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


