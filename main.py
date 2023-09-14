import design
import sys
from account import Account, DATA

print(design.welcome)

make_transaction = input("Do you want to access the account interface (0 = no, 1 = yes)?:\n> ")

while make_transaction == "1":
    print(design.selection)

    user = Account()

    prompt = input("> ")

    if prompt == "1":
        print("\n" + user.create_account())
    elif prompt == "2":
        print("\n" + user.withdraw())
    elif prompt == "3":
        print("\n" + user.add())
    elif prompt == "4":
        print("\n" + user.transfer())
        
    make_transaction = input("Do you want to perform another operation (0 = no, 1 = yes)?:\n> ")
        
print("Thanks for banking with us")
