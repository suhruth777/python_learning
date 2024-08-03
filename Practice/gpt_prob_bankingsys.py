# Create a simple banking system. The program should:

# 1.	Display a menu with options: “Check Balance,” “Deposit,” “Withdraw,” and “Exit.”
# 2.	Use a while loop to keep the program running until the user chooses to exit.
# 3.	Implement each option with appropriate functionality:
#           Check Balance: Display the current balance.
#           Deposit: Ask for the amount to deposit, add it to the balance, and display the new balance.
#           Withdraw: Ask for the amount to withdraw, subtract it from the balance if there are sufficient funds, and display the new balance.
# 4.	Use a variable to store the user’s balance, initialized to 0.

balance = 0


while True:
    print('Check Balance')
    print('Deposit')
    print('Withdraw')
    print('Exit')
    option = input("Choose from one of the options above: ").lower()
    if option == 'check balance':
        print("Your balance is: ", balance)
    elif option == 'deposit':
        deposit = int(input('How much would you like to deposit?: '))
        balance += deposit
        print('New balance: ', balance)
    elif option == 'withdraw':
        withdraw = int(input('How much would you like to withdraw?: '))
        if withdraw <= balance:
            balance -= withdraw
            print('New balance: ', balance)
        else:
            print('Insufficient funds')
    elif option == "exit":
        print('Thank you for banking with us.')
        break
    else:
        print("Invalid option, please choose again.")
        
