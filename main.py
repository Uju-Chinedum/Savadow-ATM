import design
from account import Account


def main():
    print(design.welcome)

    make_transaction = input(
        "Do you want to access the account interface (0 = no, 1 = yes)?:\n> ")

    while make_transaction == "1":
        print(design.selection)

        account = Account()

        prompt = input("> ")

        if prompt == "1":
            print(account.create_account())
        elif prompt == "2":
            print(account.withdraw())
        elif prompt == "3":
            print(account.add())
        elif prompt == "4":
            print(account.transfer())
        elif prompt == "5":
            print(account.check_balance())
        elif prompt == "6":
            print(account.update_pin())
        elif prompt == "7":
            print(account.close())
        else:
            return "Invalid Selection"

        make_transaction = input(
            "\nDo you want to perform another operation (0 = no, 1 = yes)?:\n> ")

    print("Thanks for banking with us")


if __name__ == "__main__":
    main()
