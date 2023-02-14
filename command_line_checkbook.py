# =======================================================================================================
# TABLE OF CONTENTS START
# =======================================================================================================

#       PLANNING
#       FUNCTIONS
#           - MENU
#           - TIME
#           - DATE
#           - CURRENT BALANCE
#           - WITHDRAWL
#           - DEPOSIT
#           - HISTORY
#           - CLEAR TERMINAL
#           - DELETE HISTORY
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
#           - Add id, time, amount to csv
#       - Add A Credit(Deposit)
#           - Ask for input
#           - Add id, time, amount to csv
#       - Exit
#           - break function
#       EXTRA:
#           -   X   HISTORICAL TRANSACTIONS
#           -   X   CATEGORY PER TRANSACTION
#           -   X   SUMMARY BY CATEGORY
#           -   X   DATE-TIME
#           -       TRANSACTION BY DAY
#           -   X   OPTIONAL DESCRIPTION INPUT
#           -       TRANSACTIONS BY DESCRIPTION INPUT
#           -       OPTIONAL PAST MODIFICATION

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
    # vvv BODY/OUTPUT vvv
    clear()
    while True:
        print(
              "\033[33m==>  MAIN MENU <==\033[0m\n\n"
              "\033[36m(1) View Current Balance\033[0m\n"
              "\033[36m(2) Add A Debit (Withdrawl)\033[0m\n"
              "\033[36m(3) Add A Credit (Deposit)\033[0m\n"
              "\033[36m(4) History of Transactions\033[0m\n"
              "\033[36m(5) Exit Program\033[0m\n"
              "\033[31m(DELETE) DELETE HISTORY\033[0m\n"
             )
        menuin = input("Hello!  What would you like to do?\n")
        if menuin == '1':
            clear()
            balance()
        elif menuin == '2':
            clear()
            withdrawl()
        elif menuin == '3':
            clear()
            deposit()
        elif menuin == '4':
            clear()
            history()
        elif menuin == '5':
            clear()
            print("Goodbye!")
            break
        elif menuin == 'DELETE':
            clear()
            DELETE()
        else:
            clear()
            print("Invalid input")

# ====================> TIME FUNCTION <====================
def time():
    '''
    Gets current time in HH:MM:SS
    '''
    # vvv IMPORTS vvv
    import datetime
    # vvv VARIABLES vvv
    current_time = datetime.datetime.now().time()
    time_str = current_time.strftime("%H:%M:%S")
    # vvv OUTPUT vvv
    return(time_str)

# ====================> DATE FUNCTION <====================
def date():
    '''
    Gets current date DD-MMM-YYYY
    '''
    # vvv IMPORTS vvv
    import datetime
    # vvv VARIABLES vvv
    current_date = datetime.datetime.now()
    date_str = current_date.strftime("%d-%b-%Y")
    # vvv OUTPUT vvv
    return(date_str)

# ====================> CURRENT BALANCE FUNCTION <====================
def balance():
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv GET TOTAL DEPOSITS vvv
    with open('command_line_checkbook_transactions.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        alldeposits = ([float(row['amount']) for row in reader if 'deposit' in row['category']])
        totaldeposits = sum(alldeposits)
    # vvv GET TOTAL WITHDRAWLS vvv
    with open('command_line_checkbook_transactions.csv', 'r') as read:
        reader = csv.DictReader(read)
        next(reader)
        allwithdrawls = ([float(row['amount']) for row in reader if 'withdrawl' in row['category']])
        totalwithdrawls = sum(allwithdrawls)
    # vvv CURRENT BALANCE vvv
    print(f"\033[32m${totaldeposits - totalwithdrawls}\033[0m as of {date()} // {time()}")
    print("")

# ====================> WITHDRAW FUNCTION <====================
def withdrawl():
    '''
    All withdrawls from 'command_line_checkbook_transactions.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv INITIAL MENU vvv
    print(
          "\033[33m==> WITHDRAWL MENU <==\033[0m\n\n"
          "\033[36m(1) Make A Withdrawl\033[0m\n"
          "\033[36m(2) Summary of Withdrawls\033[0m\n"
          "\033[36m(3) Back To Main Menu\033[0m\n"
         )
    menuin = input("Welcome to the 'Withdrawl Menu'!  What would you like to do?\n")
    while True:
        # vvv MAKE A WITHDRAW vvv
        if menuin == '1':
            clear()
            # vvv VARIABLES vvv
            cols = ['id', 'date', 'time', 'category', 'amount', 'description']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_transactions.csv') == False:
                print("Creating 'command_line_checkbook_transactions.csv' file...")
                with open('command_line_checkbook_transactions.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'date' : date(),
                            'time' : time(),
                            'category' : '',
                            'amount' : 0,
                            'description' : ''
                        }
                    )
                if os.path.exists('command_line_checkbook_transactions.csv') == True:
                    print("Successfully created file...\nReturning to 'Main Menu'")
                    print("")
                    break
                else:
                    print("Failed to create file...\nReturning to 'Main Menu'")
                    print("")
                    break
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_transactions.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_transactions.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                while True:
                    try:
                        withdrawin = float(input('How much would you like to withdraw?\n'))
                        break
                    except ValueError:
                        clear()
                        print("Invalid input\n")
                descqst = input("Would you like to add a descriptor? \033[33m(Y/N)\033[0m\n")
                if descqst.lower() == 'y':
                    descin = input("Input your descriptor:\n")
                    with open('command_line_checkbook_transactions.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames = cols)
                        writer.writerow(
                            {
                                'id' : new_id,
                                'date' : date(),
                                'time' : time(),
                                'category' : 'withdrawl',
                                'amount' : withdrawin,
                                'description' : descin
                            }
                        )
                    clear()
                    print(f"\033[32m${withdrawin}\033[0m logged on {time()}...\n\033[33m{descin}\033[0m inputted into description...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                    break
                else:
                    with open('command_line_checkbook_transactions.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames = cols)
                        writer.writerow(
                            {
                                'id' : new_id,
                                'date' : date(),
                                'time' : time(),
                                'category' : 'withdrawl',
                                'amount' : withdrawin,
                                'description' : ''
                            }
                        )
                    clear()
                    print(f"\033[32m${withdrawin}\033[0m logged on {time()}...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                    break
        # vvv IF USER WANTS SUMMARY OF WITHDRAWLS vvv
        elif menuin == '2':
            with open('command_line_checkbook_transactions.csv', 'r') as f:
                reader = csv.DictReader(f)
                next(reader)
                allwithdrawls = ([float(row['amount']) for row in reader if 'withdrawl' in row['category']])
                sumwithdrawls = sum(allwithdrawls)
                clear()
                print(f"Total Withdrawls ==> \033[32m${sumwithdrawls}\033[0m")
                print("")
                break
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            clear()
            print("Returning to \033[33m'Main Menu'\033[0m...")
            print("")
            break
        # vvv IF INPUT IS INVALID vvv
        else:
            clear()
            print("Invalid input...\nReturning to \033[33m'Main Menu'\033[0m")
            print("")
            break
    
# ====================> DEPOSIT FUNCTION <====================
def deposit():
    '''
    All deposits from 'command_line_checkbook_transactions.csv'
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv INITIAL MENU vvv
    print(
          "\033[33m==> DEPOSIT MENU <==\033[0m\n\n"
          "\033[36m(1) Make A Deposit\033[0m\n"
          "\033[36m(2) Summary of Deposits\033[0m\n"
          "\033[36m(3) Back To Main Menu\033[0m\n"
         )
    menuin = input("Welcome to the \033[33m'Deposit Menu'\033[0m!  What would you like to do?\n")
    while True:
        # vvv MAKE A DEPOSIT vvv
        if menuin == '1':
            clear()
            # vvv VARIABLES vvv
            cols = ['id', 'date', 'time', 'category', 'amount', 'description']    
            # vvv IF CSV FILE DOESN'T EXIST...  CREATE FILE vvv
            if os.path.exists('command_line_checkbook_transactions.csv') == False:
                print("Creating 'command_line_checkbook_transactions.csv' file...")
                with open('command_line_checkbook_transactions.csv', 'w') as f:
                    writer = csv.DictWriter(f, fieldnames = cols)
                    writer.writeheader()
                    writer.writerow(
                        {
                            'id' : 0,
                            'date' : date(),
                            'time' : time(),
                            'category' : '',
                            'amount' : 0,
                            'description' : ''
                        }
                    )
                if os.path.exists('command_line_checkbook_transactions.csv') == True:
                    print("Successfully created file...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                    break
                else:
                    print("Failed to create file...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                    break
            # vvv IF CSV FILE EXIST... EDIT FILE vvv
            elif os.path.exists('command_line_checkbook_transactions.csv'):
                # vvv MAX ID VALUE FROM CSV
                with open('command_line_checkbook_transactions.csv', 'r') as read:
                    reader = csv.reader(read)
                    next(reader)
                    max_id = max([int(row[0]) for row in reader])
                    new_id = max_id + 1
                # vvv CREATE NEW LINE vvv
                while True:
                    try:
                        depositin = float(input('How much would you like to deposit?\n'))
                        break
                    except ValueError:
                        clear()
                        print("Invalid input\n")
                descqst = input("Would you like to add a descriptor? \033[33m(Y/N)\033[0m\n")
                if descqst.lower() == 'y':
                    descin = input("Input your descriptor:\n")
                    with open('command_line_checkbook_transactions.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames = cols)
                        writer.writerow(
                            {
                                'id' : new_id,
                                'date' : date(),
                                'time' : time(),
                                'category' : 'deposit',
                                'amount' : depositin,
                                'description' : descin
                            }
                        )
                    clear()
                    print(f"\033[32m${depositin}\033[0m logged on {time()}...\n\033[33m{descin}\033[0m inputted into description...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                    break
                else:
                    with open('command_line_checkbook_transactions.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames = cols)
                        writer.writerow(
                            {
                                'id' : new_id,
                                'date' : date(),
                                'time' : time(),
                                'category' : 'deposit',
                                'amount' : depositin,
                                'description' : ''
                            }
                        )
                    clear()
                    print(f"\033[32m${depositin}\033[0m logged on {time()}...\nReturning to \033[33m'Main Menu'\033[0m")
                    print("")
                break
        # vvv IF USER WANTS SUMMARY OF DEPOSITS vvv
        elif menuin == '2':
            with open('command_line_checkbook_transactions.csv', 'r') as f:
                reader = csv.DictReader(f)
                next(reader)
                alldeposits = ([float(row['amount']) for row in reader if 'deposit' in row['category']])
                sumdeposits = sum(alldeposits)
                clear()
                print(f"Total Deposits ==> \033[32m${sumdeposits}\033[0m")
                print("")
                break
        # vvv IF USER INPUT WANTS TO GO BACK TO MAIN MENU vvv    
        elif menuin == '3':
            clear()
            print("Returning to \033[33m'Main Menu'\033[0m...\n")
            break
        # vvv IF INPUT IS INVALID vvv
        else:
            clear()
            print("Invalid input...\nReturning to \033[33m'Main Menu'\033[0m\n")
            break

# ====================> TRANSACTION HISTORY FUNCTION <====================
def history():
    '''
    Gets the history of all transactions
    '''
    # vvv IMPORTS vvv
    import os
    import csv
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv VARIABLES vvv
    cols = ['id', 'date', 'time', 'category', 'amount', 'description']
    # vvv BODY/OUTPUT vvv
    with open('command_line_checkbook_transactions.csv', 'r') as f:
        rows = f.readlines()
        headers = rows[0].strip().split(',')
        print(f"\033[33m{headers[0] : ^20}\033[0m | \033[33m{headers[1] : ^20}\033[0m | \033[33m{headers[2] : ^20}\033[0m | \033[33m{headers[3] : ^20}\033[0m | \033[33m{headers[4] : ^20}\033[0m | \033[33m{headers[5] : ^20}\033[0m")
        print(f"\033[33m{'--------------------' : ^20}\033[0m | \033[33m{'--------------------' : ^20}\033[0m | \033[33m{'--------------------' : ^20}\033[0m | \033[33m{'--------------------' : ^20}\033[0m | \033[33m{'--------------------' : ^20}\033[0m | \033[33m{'--------------------' : ^20}\033[0m")
        for row in rows[2:]:
            data = row.strip().split(',')
            print(f"\033[36m{data[0] : ^20}\033[0m | \033[36m{data[1] : ^20}\033[0m | \033[36m{data[2] : ^20}\033[0m | \033[36m{data[3] : ^20}\033[0m | \033[32m{data[4] : ^20}\033[0m | \033[36m{data[5] : ^20}\033[0m")
            print(f"\033[35m{'----------' : ^20}\033[0m | \033[35m{'----------' : ^20}\033[0m | \033[35m{'----------' : ^20}\033[0m | \033[35m{'----------' : ^20}\033[0m | \033[35m{'----------' : ^20}\033[0m | \033[35m{'----------' : ^20}\033[0m")
        print("")

# ====================> CLEAR TERMINAL FUNCTION <====================
def clear():
    '''
    Clears terminal
    '''
    # vvv IMPORTS vvv
    import os
    # vvv BODY/OUTPUT vvv
    os.system('clear')

# ====================> DELETE HISTORY FUNCTION <====================
def DELETE():
    # vvv IMPORTS vvv
    import os
    # vvv os.chdir vvv
    os.chdir(os.path.expanduser('~'))
    os.chdir('codeup-data-science')
    os.chdir('python-exercises')
    # vvv BODY/OUTPUT vvv
    req = input('Are you sure you want to \033[31mDELETE\033[0m your transaction history? \033[33m(Y/N)\033[0m\n')
    while True:
        if req.lower() == 'y':
            clear()
            print('\033[31mDELETING\033[0m history...')
            os.remove('command_line_checkbook_transactions.csv')
            print('History \033[31mDELETED\033[0m')
            print("Returning to \033[33m'Main Menu'\033[0m...\n")
            break
        elif req.lower() == 'n':
            clear()
            print("Returning to \033[33m'Main Menu'\033[0m...\n")
            break
        # vvv IF INPUT IS INVALID vvv
        else:
            clear()
            print("Invalid input...\nReturning to \033[33m'Main Menu'\033[0m\n")
            break

# =======================================================================================================
# FUNCTIONS END
# FUNCTIONS TO END PRODUCT
# END PRODUCT START
# =======================================================================================================

menu()

# =======================================================================================================
# END PRODUCT END
# =======================================================================================================