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
def calculate_tip():
    '''
    Takes a tip input and bill total input then multiplies them to return the tip percent, tip amount, 
    bill, and grand total
    '''
    tip_percent = float(input("What tip percent would you like to apply? e.g. 5% = .05\n"))
    bill_total = float(input("What is the total cost of your bill?\n"))
    grand_total = (tip_percent * bill_total) + bill_total
    return print('Tip Total:', tip_percent * bill_total, '\nTip Percentage:', tip_percent * 100, '%', '\nBill Total:', bill_total, '\nGrand Total:', grand_total)
#    return print((f"{'Tip Total' : ^20}|{'Tip Percentage' : ^20}|{'Bill Total' : ^20}|{'Grand Total' : ^20}"), '\n'(f"{'----------' : ^20}|{'---------------' : ^20}|{'-----------' : ^20}|{'------------' : ^20}"), '\n'(f"{tip_percent * bill_total : ^20}|{tip_percent : ^20}|{bill_total : ^20}|{(tip_percent * bill_total) + bill_total : ^20}"))
calculate_tip()

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
#    and return the price after the discount is applied.
def apply_discount():
    '''
    Takes original price and discount percent input and returns both as well as the new price
    '''
    original_price = float(input("What're you buyin'...  Stranger...\n"))
    discount_percent = float(input("Special discounts for strangers... e.g. 5% = .05\n"))
    new_price = original_price - (original_price * discount_percent)
    return print('Original Price:', original_price, '\nDiscount Percent:', discount_percent * 100, '%', '\nNew Price:', new_price)
apply_discount()

# 7. Define a function named handle_commas. It should accept a string that is a number that contains 
#    commas in it as input, and return a number as output.
def handle_commas():
    '''
    Takes a string input of number with commas (10,000) and returns without commas and as int type (10000)
    '''
    string = (input("I love numbers, but hate commas...  Give me a number and I'll show you:\n"))
    int_convert = int(string.replace(',', ''))
    return print(int_convert, type(int_convert), '<== Impressive right?!  TELL ME I\'M USEFUL')
handle_commas()

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade 
#    associated with that number (A-F).
def get_letter_grade():
    '''
    Takes a number input and returns a letter grade along with words of wisdom
    '''
    number_grade = int(input('WUT NUMBAH YUU GIT ON TEST?\n'))
    if number_grade >= 90:
        return print('A <== Y U NO DOCTA YET')
    elif 89 >= number_grade >= 80:
        return print('B <== B BETTER DUM DUM')
    elif 79 >= number_grade >= 70:
        return print('C <== I C that your skills are lacking')
    elif 69 >= number_grade >= 60:
        return print('D <== DISHONAH TO YOUR FAMIREE')
    else:
        return print('F <== FFFFFFUUUUUUUUUUUUdge sicle :D')
get_letter_grade()

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels 
#    removed.
def remove_vowels():
    '''
    Takes input string and returns string with all vowels removed
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        string = input("Tell me what you want what you really really want, \nI'll tell you what I want what I really really want, \nI wanna, I wanna, I really really really really really WANT TO REMOVE YO' VOWELS...  or 'quit' :D:\n")
        if string.lower() != 'quit':
            for char in string.lower():
                if char in vowel:
                    string = string.replace(char, '')
            return print(string, '<== Is this what you want what you really really want?')
        elif string == 'quit':
            return print('Guess you don\'t wanna be my lover and you don\'t wanna get with my friends ;-;')
        else:
            print(string, '<== Spice Girls don\'t understand what you really really want:\n')
remove_vowels()

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
def normalize_name():
    '''
    Takes in any string and normalizes the string for python
    '''
    string = input('Lemme set things straight...  Python style! or \'quit\':\n')
    if string == 'quit':
        return print('It\'s not like I wanted to fix it anyhow!')
    else:
        newstring = string.strip()
        newstring = newstring.lower()
        newstring = ''.join(char for char in newstring if char.isalnum())
        return print('Your input ==>', string, '\nNew input ==>', newstring)
normalize_name()

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is 
#     the cumulative sum of the numbers in the list.
#       - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#       - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum():
    list = [input("Give me a list of numbers and I'll sum it for you!\n")]

list = [input('testing')]
list
type(list)
# LIST TO STR
list2 = ''.join(list)
list2
type(list2)
# STR TO LIST
list3 = list2.split()
list3
type(list3)
newlist3 = []
j = 0

lst = []
n = int(input("Enter a number"))
for i in range(1, n + 1):
    ele = int(input())
    lst.append(ele)
print(lst)

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