import random
import json

DATA = "user_data.json"


class Account:
    def create_account(self) -> str:
        first_name = input("Please enter first name:\n> ")
        last_name = input("Please enter a last name:\n> ")

        name = first_name + " " + last_name
        pin = input("Please enter a 4-digit pin:\n> ")
        confirm_pin = input("Please confirm your pin:\n> ")

        account_number = str(random.random() * 10e9).split(".")[0]
        info = {
            account_number: {
                "name": name,
                "pin": pin,
                "balance": 0
            }
        }

        if len(pin) != 4:
            return ValueError("PIN not allowed")
        elif pin != confirm_pin:
            return "PIN does not match"

        try:
            with open(DATA, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(DATA, "w") as file:
                json.dump(info, file, indent=4)
        else:
            data.update(info)

            with open(DATA, "w") as file:
                json.dump(data, file, indent=4)

        return f"""
        Account successfully opened 🥳🥳
        Here's your account number: {account_number}
        """

    def confirm_user(self) -> tuple:
        account = input("Enter account number:\n> ")
        pin = input("Enter your pin:\n> ")

        try:
            with open(DATA, "r+") as file:
                data = json.load(file)

                if data[account]["pin"] != pin:
                    return "Incorrect PIN"
            
            return data, account, data[account]["balance"]
        except KeyError:
            return "No Account Found"
    
    def withdraw(self) -> str:
        user = self.confirm_user()
        data = user[0]
        account = user[1]
        balance = user[2]

        amount = float(input("How much do you want to withdraw:\n> "))
        if balance >= amount:
            data[account]["balance"] -= amount
            with open(DATA, "w") as file:
                json.dump(data, file, indent=4)

            return "Transaction Successful"
        else:
            print("Insufficient funds")
    
    def add(self):
        user = self.confirm_user()
        data = user[0]
        account = user[1]
        amount = float(input("How much do you want to add:\n> "))

        data[account]["balance"] += amount
        with open(DATA, "w") as file:
            json.dump(data, file, indent=4)

        return "Balance Updated\n"
    
    def transfer(self) -> str:
        user = self.confirm_user()
        data = user[0]
        account = user[1]
        balance = user[2]
        recipient = input("Enter the account number of the person you want to send to: \n> ")
        
        try:
            check = input(f"Is that the person's name {data[recipient]['name']} (0 = no, 1 = yes):\n> ")
            if check == "0":
                return "Please check the account number and try again."
            elif check == "1":
                funds = float(input("How much do you want to transfer:\n> "))

                if balance >= funds:
                    data[recipient]["balance"] += funds
                    data[account]["balance"] -= funds

                    with open(DATA, "w") as file:
                        json.dump(data, file, indent=4)

                    return "Funds transferred successfully"
                else:
                    return "Insufficient Funds"
        except KeyError:
            return "No Account Found. Please check the account number."
