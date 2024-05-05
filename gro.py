import math
import random

class Motorbike:
    def __init__(self, location, phone_number):
        self.location = location
        self.phone_number = phone_number

def calculate_distance(user_location, motorbike_location):
    # For simplicity, let's assume we're using Euclidean distance for distance calculation
    x1, y1 = user_location
    x2, y2 = motorbike_location
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def find_nearest_motorbike(user_location, motorbikes):
    nearest_motorbike = None
    min_distance = float('inf')
    for motorbike in motorbikes:
        distance = calculate_distance(user_location, motorbike.location)
        if distance < min_distance:
            min_distance = distance
            nearest_motorbike = motorbike
    return nearest_motorbike, min_distance

def generate_payment_amount():
    # Generate a random payment amount between 5 and 20
    return round(random.uniform(500, 2000), 2)

def payment_process(user_balance):
    # Simulate payment process
    print("Your current account balance is: $", user_balance)
    while True:
        payment_method = input("Enter payment method (Cash/Card): ").lower()
        if payment_method in ["cash", "card"]:
            break
        else:
            print("Invalid payment method. Please enter 'Cash' or 'Card'.")

    # Generate payment amount
    amount = generate_payment_amount()
    print("The amount to be paid is: $", amount)

    while True:
        confirm_payment = input("Do you accept this payment? (yes/no): ").lower()
        if confirm_payment == "yes":
            if user_balance >= amount:
                user_balance -= amount
                print("Payment successful! Amount deducted:", amount)
                print("Remaining balance:", user_balance)
                break
            else:
                print("Insufficient balance. Please recharge your account.")
                break
        elif confirm_payment == "no":
            print("Payment declined.")
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def main():
    try:
        # Dummy data for demonstration
        user_name = input("Enter your name: ")
        user_address = input("Enter your address: ")  # User's address
        user_phone_number = input("Enter your phone number: ")  # User's phone number
        user_balance = float(input("Enter your account balance: "))  # User's account balance

        user_location = (123.45, 67.89)  # User's location coordinates

        motorbikes = [
            Motorbike((123.46, 67.90), "0987654321"),  # Motorbike 1
            Motorbike((123.47, 67.88), "0987654322"),  # Motorbike 2
            Motorbike((123.44, 67.91), "0987654323")   # Motorbike 3
        ]

        # Find nearest motorbike
        nearest_motorbike, distance = find_nearest_motorbike(user_location, motorbikes)
        print("Nearest motorbike found at location:", nearest_motorbike.location)
        print("Distance to motorbike:", distance)

        # Simulate motorbike reaching the user
        print("Motorbike is on the way...")

        

        # Payment process
        payment_process(user_balance)

    except ValueError:
        print("Invalid input. Please enter a valid number for account balance.")

if __name__ == "__main__":
    main()




