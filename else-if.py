# Function to check PIN
def check_pin(pin):
    saved_pin = "1234"  # Assuming PIN is 1234
    return pin == saved_pin

# Function to check balance
def check_balance():
    return 10000  # Assuming initial balance is $10,000

# Function to withdraw money
def withdraw(amount, balance):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient balance!")
        return balance

# Function to deposit money
def deposit(amount, balance):
    return balance + amount

# Main program
print("Welcome to Simple ATM")

while True:
    pin = input("Enter your PIN: ")


    if check_pin(pin):
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Quit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            print("Your balance is:", check_balance())
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            new_balance = withdraw(amount, check_balance())
            print("Withdrawal successful. Your new balance is:", new_balance)
        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            new_balance = deposit(amount, check_balance())
            print("Deposit successful. Your new balance is:", new_balance)
        elif choice == 4:
            print("Thank you for using Simple ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")
    else:
        print("Invalid PIN. Please try again.")

# Checking a student's grade based on their score
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is:", grade)

# Checking eligibility for a discount based on purchase amount and membership status
purchase_amount = float(input("Enter your purchase amount: "))
is_member = input("Are you a member? (yes/no): ").lower()

if is_member == 'yes':
    if purchase_amount > 100:
        discount = 0.2  # 20% discount for members on purchases over $100
    else:
        discount = 0.1  # 10% discount for members on purchases below $100
else:
    if purchase_amount > 200:
        discount = 0.15  # 15% discount for non-members on purchases over $200
    else:
        discount = 0.05  # 5% discount for non-members on purchases below $200

total_amount = purchase_amount * (1 - discount)
print("Your total amount after discount is:", total_amount)


