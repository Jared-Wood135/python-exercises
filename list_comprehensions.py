# =======================================================================================================
# Initial Examples/Orientation START
# =======================================================================================================

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# =======================================================================================================
# Initial Examples/Orientation END
# Initial Examples/Orientation TO 17 Exercises
# 17 Exercises START
# =======================================================================================================

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named 
#              uppercased_fruits to hold the output of the list comprehension. Output should be 
#              ['MANGO', 'KIWI', etc...]
uppercased_fruits = [str.upper() for str in fruits]
uppercased_fruits

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce 
#              output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [str.capitalize() for str in fruits]
capitalized_fruits

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
#              Hint: You'll need a way to check if something is a vowel.
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_more_than_two_vowels = [str for str in fruits if sum(char in vowels for char in str) >= 3]
fruits_with_more_than_two_vowels

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be 
#              ['mango', 'kiwi', 'strawberry']
vowels = ['a', 'e', 'i', 'o', 'u']
fruits_with_only_two_vowels = [str for str in fruits if sum(char in vowels for char in str) == 2]
fruits_with_only_two_vowels

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_characters = [str for str in fruits if sum(char in str for char in str) >= 5]
fruits_with_more_than_five_characters

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_only_five_characters = [str for str in fruits if sum(char in str for char in str) == 5]
fruits_with_only_five_characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_characters = [str for str in fruits if sum(char in str for char in str) < 5]
fruits_with_less_than_five_characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be 
#              [5, 4, 10, etc... ]
fruits_char_length = [len(str) for str in fruits]
fruits_char_length

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits 
#              that contain the letter "a"
fruits_with_letter_a = [str for str in fruits if 'a' in str]
fruits_with_letter_a

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = int % 2 == 0

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = int % 2  != 0

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = int >= 0

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = int < 0

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 
#               2 or more numerals
digits = [int for int in range(10)]
digits
digits_str = list(map(str, digits))
digits_str
test = list(map(str, numbers))
test2 = [str for str in test if sum(char in digits_str for char in str) >= 2]
test2
final = list(map(int, test2))
final

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element 
#               squared. Output is [4, 9, 16, etc...]
numbers_squared = [int ** 2 for int in numbers]
numbers_squared

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are 
#               both odd and negative.
odd_negative_numbers = [int for int in numbers if int % 2 != 0 and int < 0]
odd_negative_numbers
numbers

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [int + 5 for int in numbers]
numbers_plus_5

# =======================================================================================================
# 17 Exercises END
# 17 Exercises TO BONUS Exercise
# BONUS Exercise START
# =======================================================================================================

# Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
import sympy
print(sympy.isprime(3))
10**0.5


# =======================================================================================================
# BONUS Exercise END
# =======================================================================================================