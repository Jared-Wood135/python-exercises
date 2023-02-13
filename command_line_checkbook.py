# =======================================================================================================
# TABLE OF CONTENTS START
# =======================================================================================================

#       PLANNING
#       FUNCTIONS
#           - MENU
#           - DATE
#           - CURRENT BALANCE
#           - WITHDRAWL
#           - DEPOSIT
#       END PRODUCT

# =======================================================================================================
# TABLE OF CONTENTS END
# TABLE OF CONTENTS TO PLANNING
# PLANNING START
# =======================================================================================================

# If statements (Notify if invalid input)
#       - View current balance
#           - Display current balance
#       - Add A Debit(Withdrawl)
#           - Ask for input
#           - Add *Additional - id*, time, amount to csv
#       - Add A Credit(Deposit)
#           - Ask for input
#           - Add *Additional - id*, time, amount to csv
#       - Exit
#           - break function

# =======================================================================================================
# PLANNING END
# PLANNING TO FUNCTIONS
# FUNCTIONS START
# =======================================================================================================

# ====================> MENU FUNCTION <====================
def menu():
    '''
    Main Menu for checkbook
    '''
    while True:
        print("(1) -- View Current Balance")
        print("(2) -- Add A Debit (Withdrawl)")
        print("(3) -- Add A Credit (Deposit)")
        print("(4) -- Exit Program")
        menuin = input("Hello!  What would you like to do?\n")
        if menuin == '1':
            balance()
        elif menuin == '2':
            withdrawl()
        elif menuin == '3':
            deposit()
        elif menuin == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid input")

# ====================> DATE FUNCTION <====================
def datetime():
    '''
    Gets current time in HH:MM:SS
    '''
    import datetime
    current_time = datetime.datetime.now().time()
    time_str = current_time.strftime("%d-%b-%Y %H:%M:%S")
    return(time_str)

# ====================> CURRENT BALANCE FUNCTION <====================
def balance():
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    #print(os.getcwd())
    os.chdir('codeup-data-science')
    #print(os.getcwd())
    os.chdir('python-exercises')
    #print(os.getcwd())
    # vvv GET TOTAL DEPOSITS vvv
    with open('command_line_checkbook_deposit.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        alldeposits = ([float(row['amount']) for row in reader])
        totaldeposits = sum(alldeposits)
    # vvv GET TOTAL WITHDRAWLS vvv
    with open('command_line_checkbook_withdrawl.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        allwithdrawls = ([float(row['amount']) for row in reader])
        totalwithdrawls = sum(allwithdrawls)
    # vvv CURRENT BALANCE vvv
    print(f"${totaldeposits - totalwithdrawls} as of {datetime()}")

# ====================> WITHDRAW FUNCTION <====================
def withdrawl():
    '''
    All withdrawls from 'command_line_checkbook_withdrawl.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    #print(os.getcwd())
    os.chdir('codeup-data-science')
    #print(os.getcwd())
    os.chdir('python-exercises')
    #print(os.getcwd())
    # vvv INITIAL MENU vvv
    print('(1) Make A Withdrawl')
    print('(2) All Withdrawls')
    print('(3) Back To Main Menu')
    menuin = input("Welcome to the 'Withdrawl Menu'!  What would you like to do?\n")
    while True:
        # vvv MAKE A WITHDRAW vvv
        if menuin == '1':
            # vvv VARIABLES vvv
            withdrawin = input('How much would you like to withdraw?\n')
            cols = ['id', 'time', 'amount']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_withdrawl.csv') == False:
                print("Creating 'command_line_checkbook_withdrawl.csv' file...")
                with open('command_line_checkbook_withdrawl.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'time' : datetime(),
                            'amount' : 0
                        }
                    )
                withdrawl()
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_withdrawl.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_withdrawl.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                with open('command_line_checkbook_withdrawl.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writerow(
                        {
                            'id' : new_id,
                            'time' : datetime(),
                            'amount' : withdrawin
                        }
                    )
                withdrawl()
        # vvv IF USER WANTS ALL WITHDRAWLS vvv
        elif menuin == '2':
            cols = ['id', 'time', 'amount']
            with open('command_line_checkbook_withdrawl.csv', 'r') as f:
                reader = csv.DictReader(f, fieldnames = cols)
                lines = []
                for line in reader:
                    lines.append(line)
                print(lines)
            withdrawl()
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            menu()
        # vvv IF INPUT IS INVALID vvv
        else:
            print("Invalid input, changing to Main Menu")
    
# ====================> DEPOSIT FUNCTION <====================
def deposit():
    '''
    All deposits from 'command_line_checkbook_deposit.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    #print(os.getcwd())
    os.chdir('codeup-data-science')
    #print(os.getcwd())
    os.chdir('python-exercises')
    #print(os.getcwd())
    # vvv INITIAL MENU vvv
    print('(1) Make A Deposit')
    print('(2) All Deposits')
    print('(3) Back To Main Menu')
    menuin = input("Welcome to the 'Deposit Menu'!  What would you like to do?\n")
    while True:
        # vvv MAKE A DEPOSIT vvv
        if menuin == '1':
            # vvv VARIABLES vvv
            depositin = input('How much would you like to deposit?\n')
            cols = ['id', 'time', 'amount']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_deposit.csv') == False:
                print("Creating 'command_line_checkbook_deposit.csv' file...")
                with open('command_line_checkbook_deposit.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'time' : datetime(),
                            'amount' : 0
                        }
                    )
                deposit()
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_deposit.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_deposit.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                with open('command_line_checkbook_deposit.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writerow(
                        {
                            'id' : new_id,
                            'time' : datetime(),
                            'amount' : depositin
                        }
                    )
                deposit()
        # vvv IF USER WANTS ALL DEPOSITS vvv
        elif menuin == '2':
            cols = ['id', 'time', 'amount']
            with open('command_line_checkbook_deposit.csv', 'r') as f:
                reader = csv.DictReader(f, fieldnames = cols)
                lines = []
                for line in reader:
                    lines.append(line)
                print(lines)
            deposit()
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            menu()
        # vvv IF INPUT IS INVALID vvv
        else:
            print("Invalid input, changing to Main Menu")

# =======================================================================================================
# FUNCTIONS END
# FUNCTIONS TO END PRODUCT
# END PRODUCT START
# =======================================================================================================

menu()

# =======================================================================================================
# END PRODUCT END
# =======================================================================================================