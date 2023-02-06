# =======================================================================================================
# Initial 4 Questions START
# =======================================================================================================

# 1. Identify the data type of the following values:
# 99.9
type(99.9)
# "False"
type("False")
# False
type(False)
# '0'
type('0')
# 0
type(0)
# True
type(True)
# 'True'
type('True')
# [{}]
type([{}])
# {'a': []}
type({'a': []})

# 2. What data type would best represent the following?
# A term or phrase typed into a search box
type(str)
# Whether or not a user is logged in
type(bool)
# A discount amount to apply to a user's shopping cart
type(int), type(float), type(bool)
# Whether or not a coupon code is valid
type(bool)
# An email address typed into a registration form
type(str)
# The price of a product
type(int), type(float)
# The email addresses collected from a registration form
type(list)
# Information about applicants to Codeup's data science program
type(dict)

# 3. For each of the following code blocks:
# -- Read the expression and predict the evaluated results
# -- Execute the expression in a Python REPL.
# '1' + 2
'1' + 2
# 6 % 4
6 % 4
# type(6 % 4)
type(6 % 4)
# type(type(6 % 4))
type(type(6 % 2))
# '3 + 4 is ' + 3 + 4
'3 + 4 is ' + 3 + 4
# 0 < 0
0 < 0
# 'False' == False
'False' == False
# True == 'True'
True == 'True'
# 5 >= -5
5 >= -5
# True or "42"
True or "42"
# 6 % 5
6 % 5
# 5 < 4 and 1 == 1
5 < 4 and 1 == 1
# 'codeup' == 'codeup' and 'codeup' == 'Codeup'
'codeup' == 'codeup' and 'codeup' == 'Codeup'
# 4 >= 0 and 1 !== '1'
4 >= 0 and 1 !== '1'
# 6 % 3 == 0
6 % 3 == 0
# 5 % 2 != 0
5 % 2 != 0
# [1] + 2
[1] + 2
# [1] + [2]
[1] + [2]
# [1] * 2
[1] * 2
# [1] * [2]
[1] * [2]
# [] + [] == []
[] + [] == []
# {} + {}
{} + {}

# 4. Create a Python script file named data_types_and_variables.py. Inside the script, write 
#    Python code to describe the following scenarios. You will need to create and assign 
#    variables and use operators.

# =======================================================================================================
# Initial 4 Questions END
# Initial 4 Questions TO Questions 5-9
# Questions 5-9 START
# =======================================================================================================

# 5. You have rented some movies for your kids:
# -- The Little Mermaid for 3 days
# -- Brother Bear for 5 days
# -- Hercules for 1 day
# -- If the daily fee to rent a movie is 3 dollars, how much will you have to pay?
# Answer: 27 dollars
3 * 9

# 6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.
# -- They pay you the following hourly rates:
# -- Google: 400 dollars
# -- Amazon: 380 dollars
# -- Facebook: 350 dollars
# -- This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
# -- How much will you receive in payment for this week?
# Answer: 7420 dollars
(10 * 350) + (6 * 400) + (4 * 380)

# 7. A student can be enrolled to a class only if the class is not full and the class schedule does 
#    not conflict with her current schedule.
???

# 8. A product offer can be applied only if people buys more than 2 items, and the offer has not 
#    expired. Premium members do not need to buy a specific amount of products.
???

# 9. Continue working in the data_types_and_variables.py file. Use the following code to follow the 
#    instructions below:
# -- username = 'codeup'
# -- password = 'notastrongpassword'
# -- Create a variable that holds a boolean value for each of the following conditions:
# -- The password must be at least 5 characters
# -- The username must be no more than 20 characters
# -- The password must not be the same as the username
# -- Bonus Neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'
def userpass():
    IF password >= 5
    
bool(password >= 5, password <= 20 AND username != password)

# =======================================================================================================
# Questions 5-9 END
# Questions 5-9 TO Bonus Exercises
# Bonus Exercises START
# =======================================================================================================

# 1. For practicing with list comprehensions, work through 17 List Comprehension Exercises. Add your 
#    solutions to a new file named list_comprehensions.py

# 2. For even more practice with all your Python tools together, work through 20 Python Data Structure 
#    Manipulation Exercises. Name this file python_data_structure_manipulation_exercises.py.