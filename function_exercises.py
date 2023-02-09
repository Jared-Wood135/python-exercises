# =======================================================================================================
# 11 Exercises START
# =======================================================================================================

#  1. Define a function named is_two. It should accept one input and return True if the passed input is 
#     either the number or the string 2, False otherwise.
def is_two():
    '''
    Function to identify if an input is string type 2 or integer type 2...
    Otherwise repeats the function until prompted to quit.
    '''
    while True:
        num = input("Enter ye digits or 'quit'!\n")
        if num.isdigit() == True and num == '2':
            print(num, "<== This be a string of two!")
            break
        elif type(num) == int and num == 2:
            print(num, "This be an integer of 2!")
            break
        elif num.lower() == 'quit':
            print("Running from your terrible two's are we?")
            break
        else:
            print(num, "<== Neither a string or integer of two!")
is_two()

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False 
#    otherwise.
def is_vowel():
    '''
    Identifies if a single letter input is a vowel or not...
    Otherwise repeats the function until prompted to quit.
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        letter = input("GIVE ME AN A...  GIVE ME A E...  Or anything really I don't care, just a letter or 'quit':\n")
        if letter in vowel:
            print("You got vowel spirit!")
            break
        elif letter.lower() == 'quit':
            print("Aw, what a party pooper!")
            break
        else:
            print(letter, "<== You can do better than that!")
is_vowel()

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
#    False otherwise. Use your is_vowel function to accomplish this.
def is_consonant():
    '''
    Identifies if a single letter is a consonant or not...
    Otherwise will repeat the function until prompted to quit.
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        letter = input("Back at it again, but with consonant spirit!  Gimme a letter or 'quit':\n")
        if letter not in vowel:
            print(letter, "<== Behold the consonant!")
            break
        elif letter.lower() == 'quit':
            print("Keep up your spirit!")
            break
        else:
            print(letter, '<== One more time!')
is_consonant()

# 4. Define a function that accepts a string that is a word. The function should capitalize the first 
#    letter of the word if the word starts with a consonant.
def first_letter_consonant_capitalize():
    '''
    Identifies if the first letter of a str input is a consonant then capitalizes it...
    Otherwise, repeats the function until prompted to quit.
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        word = input("Throw a word at me and I'll capitilize it!  ONLY IF THE 1ST LETTER IS A CONSONANT...  I'm picky like that or 'quit':\n")
        if word.isdigit() == False and word[0] not in vowel:
            print(word.capitalize(), '<== My finest work yet!')
            break
        elif word.lower()  == 'quit':
            print("Guess I really am useless...  Bye ;-;")
            break
        else:
            print(word, "<== C'mon, gimme something to work with here!")
first_letter_consonant_capitalize()

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
#    and the bill total, and return the amount to tip.


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
#    and return the price after the discount is applied.


# 7. Define a function named handle_commas. It should accept a string that is a number that contains 
#    commas in it as input, and return a number as output.


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
#    associated with that number (A-F).


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels 
#    removed.


# 10. Define a function named normalize_name. It should accept a string and return a valid python 
#     identifier, that is:
#       - anything that is not a valid python identifier should be removed
#       - leading and trailing whitespace should be removed
#       - everything should be lowercase
#       - spaces should be replaced with underscores
#       - for example:
#           - Name will become name
#           - First Name will become first_name
#           - % Completed will become completed


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is 
#     the cumulative sum of the numbers in the list.
#       - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#       - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# =======================================================================================================
# 11 Exercises END
# 11 Exercises TO Additional Exercise (1)
# Additional Exercise (1) START
# =======================================================================================================

# - Once you've completed the above exercises, follow the directions from 
#   https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment 
#   your code to explain your code.


# =======================================================================================================
# Additional Exercise (1) END
# Additional Exercise (1) TO BONUS (2)
# BONUS (2) START
# =======================================================================================================

# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and 
#    return a string that is the representation of the time in a 24-hour format. 


# 1-Bonus. write a function that does the opposite.


# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index 
#    number of the column.
#       - col_index('A') returns 1
#       - col_index('B') returns 2
#       - col_index('AA') returns 27


# =======================================================================================================
# BONUS (2) END
# =======================================================================================================