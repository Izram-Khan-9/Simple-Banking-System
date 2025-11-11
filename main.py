# Importing all necessary modules
import random
import string

# Main dict where all the accounts will be created
bank = {}
# Generating numbers for account ID
numbers = string.digits
# A list where all notes will be stored
notes = []
# A list where all the transaction history will be stored
transaction_history = []

#____________________________________________________________________________________________________

# Function to create a bank account
def create_account():

    print('''
|----------------------|
|---CREATING_ACCOUNT---|
|----------------------|
          ''')

    # Generating a random ID (ensure unique)
    ID = ''.join(random.sample(numbers, 8))
    while ID in bank:
        ID = ''.join(random.sample(numbers, 8))

    name = input('Enter your name: ')
    # Making a sub-dict (ID) in side main_dict (bank) and storing name in it
    bank[ID] = {'Name': name}
    
    print('\n✅ Name added successfully!')

    while True:
        gmail = input('\nEnter your gmail: ')

        if not gmail.endswith('@gmail.com'):
            print('\n❌ Error: Gmail must end with @gmail.com!')
        
        else:
            # Adding gmail to sub-dict
            bank[ID]['Gmail'] = gmail
            print('\n✅ Gmail added successfully!')
            break

    while True:
        password = input('\nCreate a password: ')

        if len(password) < 8:
            print('\n❌ Error: Password must be atleast 8 characters long!')

        elif len(password) > 15:
            print('\n❌ Error: Password must be atmost 15 characters long!')

        else:
            # Adding password to sub-dict
            bank[ID]['Password'] = password
            break

    print('\n✅ Account created successfully!')

    print('-'*30)

    for account_id, account_info in bank.items():
        print(f'\nAccount ID: {account_id}')
        for key, value in account_info.items():
            print(f'{key} - {value}')

    print('-'*30)

    print('\nNote: Remember you Account ID!')

#____________________________________________________________________________________________________

# Function to view bank account
def view_account():

    print('''
|----------------------|
|-----VIEW_ACCOUNT-----|
|----------------------|
          ''')

    try:

        id_check = input('Enter your account ID: ')

        access_the_id = bank[id_check]
        print('\n--Account_Info--\n')
        for key, value in access_the_id.items():
            print(f'{key} - {value}')

    except KeyError:
        print('\n❌ Error: Account ID does not exist!')

#____________________________________________________________________________________________________

# Function to deposit money into the bank account
def deposit_money():

    print('''
|---------------------|
|----DEPOSIT_MONEY----|
|---------------------|
          ''')

    while True:
        try:
            id_check = input('Enter your account ID: ')

            if id_check == '0':
                print('\n🛑 Depositing money was stopped!')
                break
            
            elif id_check in bank.keys():
                
                amount_to_add = int(input('\nEnter the amount: '))

                if amount_to_add == 0:
                    print('\n🛑 Depositing money was stopped!')
                    break
                    
                note = input('\nEnter note: ').title()
                if note == '0':
                    print('\n🛑 No note added!')
                notes.append(note)

                # Storing the sub-dict (ID) in a variable name access_the_id
                access_the_id = bank[id_check]
                # Creating a new key-value pair inside the sub-dict (ID)
                access_the_id['Amount present'] = amount_to_add
                result = f'\n✅ Amount: ${amount_to_add} deposited successfully!'
                # Adding transaction history to transaction_history list
                transaction_history.append(result)
                print('\n')
                print(result)
                break
                
            else:
                print('\n❌ Error: Account ID does not exist!')

        except ValueError:
            print('\n❌ Error: Invalid amount!')

        except KeyError:
            print('\n❌ Error: ID does not exist!')

#____________________________________________________________________________________________________

# Funtion to withdraw money from the bank account
def withdraw_money():

    print('''
|----------------------|
|----WITHDRAW_MONEY----|
|----------------------|
          ''')

    while True:
        id_check = input('Enter account ID: ')

        if id_check in bank.keys():
            try:
                # Check that an amount is present for this account
                if 'Amount present' not in bank[id_check]:
                    print('\n❌ Error: No amount deposited yet!')
                    break

                # Storing the key(Amount present) inside a specific sub-dict (ID) in a varialbe name total_amount
                total_amount = bank[id_check]['Amount present']
                print(f'\nTotal amount present: ${total_amount}')

                amount_to_withdraw = int(input('\nEnter the amount: '))

                if amount_to_withdraw > total_amount:
                    print(f'\n❌ Error: ${amount_to_withdraw} is higher then actual amount!')
                    continue

                elif total_amount == 0:
                    print('\n❌ Error: No amount deposited yet!')
                    break

                elif amount_to_withdraw == 0:
                    print('\n🛑 Stop withdrawing money!')
                    break

                else:
                    note = input('\nEnter note: ').title()

                    if note == '0':
                        print('\n🛑 No note added')
                    notes.append(note)

                    # Subtratcing the withdraw amount from the total amount and storing it in a variable name remaining_amount
                    remaining_amount = total_amount - amount_to_withdraw
                    # Replacing the total_amount in key(Amount present) with remaining amount
                    bank[id_check]['Amount present'] = remaining_amount
                    print('\n')
                    result = f'✅ Amount: ${amount_to_withdraw} withdrew successfully!'
                    # Adding the transaction to the transaction_history list
                    transaction_history.append(result)
                    print(result)
                    print(f'Remaining amount: ${remaining_amount}')
                    break

            except ValueError:
                print('\n❌ Error: Invalid amount!')
        
        else:
            print('\n❌ Error: ID does not exist!')

#____________________________________________________________________________________________________

# Function to view transaction history
def view_transaction_history():

    print('''
|------------------------------|
|---VIEW_TRANSACTION-HISTORY---|
|------------------------------|
          ''')

    try:

        id_check = input('Enter account ID: ')

        if id_check in bank.keys():

            if not transaction_history:
                print('\n🛑 No transaction history available!')
                return

            for i, (transaction, note) in enumerate(zip(transaction_history, notes), start=1):
                print(f"{i}: {transaction.replace('successfully!','')} - {note}")
    
    except KeyError:
        print('\n❌ Error: ID does not exist')

#____________________________________________________________________________________________________

# Function for different account settings
def account_settings():

    print('''
|----------------------|
|---ACCOUNT_SETTINGS---|
|----------------------|
          ''')

    while True:  
        print('\n1. View account')
        print('2. Change settings')
        print('3. Exit settings')

        user_input = input('\nEnter (1/2/3): ')
        
        if user_input == '1':
            view_account()

        elif user_input == '2':
            print('\n--SETTINGS--')
            
            id_check = input('\nEnter account ID: ')

            if id_check in bank.keys():

                print('\n1 - Change name')
                print('2 - Change gmail')
                print('3 - Change password')

                user_input = int(input('\nEnter (1/2/3): '))

                if user_input == 1:
                    new_name = input('\nEnter new name: ')

                    # Replacing the name with new name
                    bank[id_check]['Name'] = new_name
                    print(f'\n✅ Name changed to [{new_name}] successfully!')
                
                elif user_input == 2:
                    new_gmail = input('\nEnter new gmail: ')

                    if not new_gmail.endswith('@gmail.com'):
                        print('\n❌ Error: Email must end with @gmail.com')

                    else:
                        # Replacing the gmail with new gmail
                        bank[id_check]['Gmail'] = new_gmail
                        print(f'\n✅ Gmail changed to [{new_gmail}] successfully!')

                elif user_input == 3:
                    new_password = input('\nEnter new password: ')

                    if len(new_password) < 8:
                        print('\n❌ Error: Password must be atleast 8 characters long!')

                    elif len(new_password) > 15:
                        print('\n❌ Error: Password must be atmost 15 characters long!')
                    else:
                        # Replacing the password with new password
                        bank[id_check]['Password'] = new_password
                        print(f'\n✅ Password changed to [{new_password}] successfully!')
                
                else:
                    print('\n❌ Error: Please enter (1/2/3)!')
            
            else:
                print('\n❌ Error: ID does not exist!')

        elif user_input == '3':
            print('\n🛑 Settings Exited!')
            break

        else:
            print('\n❌ Error: Please enter (1/2/3)!')

#____________________________________________________________________________________________________

# An instro function that will be displayed at the start  
def intro():
    print("\n" + "="*50)
    print("          WELCOME TO BANKING SYSTEM")
    print("="*50)
    print("\n      Manage multiple accounts, deposits,")
    print("     withdrawals, and  track transactions!")
    print("\n" + "-"*50)

# A function for detailed instruction manual
def instruction_manual():
    print("\n" + "="*50)
    print("          BANKING SYSTEM - INSTRUCTIONS")
    print("="*50)
    print("\n1. Create Account - Start with account creation")
    print("2. Deposit - Add money to any account using ID")
    print("3. Withdraw - Remove money with balance check")
    print("4. View Account - Check account details with ID")
    print("5. Transaction History - See all transactions")
    print("\nFeatures:")
    print("• Multiple account support")
    print("• Secure ID-based access")
    print("• Transaction notes and history")
    print("• Balance validation")
    print('\nNote: Enter 0 to stop depositing, withdrawing and adding notes!')
    print("\nNote: Remember your Account ID for all operations!")
    print("-"*50)

#____________________________________________________________________________________________________

# Storing all functions inside a dict
all_func = {
    'create_account': create_account,
    'view_account': view_account,
    'deposit_money': deposit_money,
    'withdraw_money': withdraw_money,
    'transaction_history': view_transaction_history,
    'account_settings': account_settings
}

#____________________________________________________________________________________________________

# Main function to run the whole banking system
def use_bank():
    intro()
    print('\nCREATE YOUR FIRST ACCOUNT!')
    create_account()
    
    while True:
        print('\n' + '-'*30)
        for i, func_name in enumerate(all_func.keys(), start=1):
            print(f"{i} - {func_name.replace('_',' ').title()}")
        print('0 - Exit')
        
        choice = input('\nEnter your choice (0-6): ')
        
        if choice == '0':
            print('\nGoodbye!')
            print('Hope you like it!')
            break
            
        try:
            # Get the function name from the dictionary keys
            func_name = list(all_func.keys())[int(choice)-1]
            # Call the function
            all_func[func_name]()
        except (ValueError, IndexError):
            print('\n❌ Invalid choice!')

if __name__ == '__main__':
    use_bank()
    
#____________________________________________________________________________________________________
# Created by: Izram Khan
# Date created: 11-11-25 [Thursday](9:20 pm)
# AI usage: 20%
# All credit goes to Izram Khan (80%), Deepseek (15%), Claud (5%)
