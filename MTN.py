import random

class SimCard:
    def __init__(self, name, pin):
        self.name = name
        self.number = self.generate_number()
        self.pin = pin
        self.main_account_balance = 2000
        self.mobile_money_balance = 100000

    def generate_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def send_money(self, recipient_number, amount, pin):
        if pin != self.pin:
            return "Incorrect PIN. Transaction failed."         
        if amount > self.main_account_balance:
            return "Insufficient balance."
        
        self.main_account_balance -= amount
        return f"Successfully sent {amount} RWF to {recipient_number}."

    def add_money_to_mobile_money(self, amount):
        self.mobile_money_balance += amount


def main():
    user_name = input("Enter your name: ")
    user_pin = input("Enter your PIN (4 digits): ")       #user's place to provide the created PIN
    sim_card = SimCard(user_name, user_pin)
    print(f"Welcome, {sim_card.name}! Your SIM card number is {sim_card.number}")

    while True:
        option = input("\nChoose an option:\n1. Send money\n2. Add money to Mobile Money\n3. Quit\n")
        
        if option == "1":
            recipient_number = input("Enter recipient's phone number: ")
            amount = float(input("Enter amount to send: "))
            pin = input("Enter your PIN: ")
            print(sim_card.send_money(recipient_number, amount, pin))
        
        elif option == "2":
            amount = float(input("Enter amount to add to Mobile Money: "))
            sim_card.add_money_to_mobile_money(amount)
            print(f"{amount} RWF added to Mobile Money.")
        
        elif option == "3":
            print("THANK YOU  FOR CHOOSING MTN !.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

