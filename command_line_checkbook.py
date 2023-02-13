# =======================================================================================================
# PLANNING START
# =======================================================================================================

# If statements (Notify if invalid input)
#       - View current balance
#           - Display current balance
#       - Add A Debit(Withdrawl)
#           - Ask for input
#           - Add id, time, amount to csv
#       - Add A Credit(Deposit)
#           - Ask for input
#           - Add id, time, amount to csv
#       - Exit
#           - break function

# =======================================================================================================
# PLANNING END
# PLANNING TO CODE
# CODE START
# =======================================================================================================

def menu():
    '''
    Main Menu for checkbook
    '''
    while True:
        print("(1) -- View Current Balance")
        print("(2) -- Add A Debit (Withdrawl)")
        print("(3) -- Add A Credit(Deposit)")
        print("(4) -- Exit Program")
        menuin = input("Hello!  What would you like to do?\n")
        if menuin == '1':
            print("Current Balance")
        elif menuin == '2':
            print("Withdrawl")
        elif menuin == '3':
            print("Deposit")
        elif menuin == '4':
            break
        else:
            print("Invalid input")
menu()

def withdrawl():
    '''
    All withdrawls from 'command_line_checkbook_withdrawl.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    print(os.getcwd())
    os.chdir('codeup-data-science')
    print(os.getcwd())
    os.chdir('python-exercises')
    print(os.getcwd())
    # vvv VARIABLES vvv
    withdrawin = input('How much would you like to withdraw?\n')
    cols = ['id', 'time', 'amount']
#    with open('command_line_checkbook_withdrawl.csv', 'w') as f:
#        writer = csv.DictWriter(f, fieldnames = cols)
#        writer.writeheader()
    with open('command_line_checkbook_withdrawl.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames = cols)
        writer.writeheader()
        for i, row in enumerate(rows):
            row['id'] = i + 1
        writer.writerow(
            {
                'id' : 1,
                'time' : datetime(),
                'amount' : withdrawin
            }
        )
    with open('command_line_checkbook_withdrawl.csv', 'r') as f:
        content = csv.DictReader(f, fieldnames = cols)
        lines = []
        for line in content:
            lines.append(line)
    print(lines)
withdrawl()

def datetime():
    '''
    Gets current time in HH:MM:SS
    '''
    import datetime
    current_time = datetime.datetime.now().time()
    time_str = current_time.strftime("%H:%M:%S")
    return(time_str)
datetime()

def deposit():
    '''
    All deposits from 'command_line_checkbook_deposit.csv'
    '''
