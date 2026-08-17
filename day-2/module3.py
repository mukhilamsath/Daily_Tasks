

import csv
import json




class InsufficientFundsError(Exception):
    pass




class BankAccount:

    def __init__(self, holder_name, balance=0):

        if balance < 0:
            raise ValueError(
                "Initial balance cannot be negative."
            )

        self.holder_name = holder_name
        self.balance = balance

    # --------------------------------------
    # Deposit
    # --------------------------------------

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self.balance += amount

        print(
            f"₹{amount} deposited into "
            f"{self.holder_name}'s account."
        )

    # --------------------------------------
    # Withdraw
    # --------------------------------------

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance:
            raise InsufficientFundsError(
                "Insufficient balance."
            )

        self.balance -= amount

        print(
            f"₹{amount} withdrawn from "
            f"{self.holder_name}'s account."
        )

    # --------------------------------------
    # Display balance
    # --------------------------------------

    def display_balance(self):

        print("--------------------------------")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")
        print("--------------------------------")


# ==========================================
# 3. SAVINGS ACCOUNT
# ==========================================

class SavingsAccount(BankAccount):

    def add_interest(self, rate):

        if rate < 0:
            raise ValueError(
                "Interest rate cannot be negative."
            )

        interest = self.balance * rate / 100

        self.balance += interest

        print(
            f"₹{interest} interest added to "
            f"{self.holder_name}'s account."
        )



class CurrentAccount(BankAccount):

    def __init__(
        self,
        holder_name,
        balance=0,
        overdraft_limit=0
    ):

        if overdraft_limit < 0:
            raise ValueError(
                "Overdraft limit cannot be negative."
            )

        super().__init__(
            holder_name,
            balance
        )

        self.overdraft_limit = overdraft_limit

    # --------------------------------------
    # Withdraw with overdraft
    # --------------------------------------

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError(
                "Withdrawal exceeds the overdraft limit."
            )

        self.balance -= amount

        print(
            f"₹{amount} withdrawn from "
            f"{self.holder_name}'s account."
        )

  

    def display_balance(self):

        print("--------------------------------")
        print(f"Account Holder  : {self.holder_name}")
        print(f"Balance         : ₹{self.balance}")
        print(f"Overdraft Limit : ₹{self.overdraft_limit}")
        print("--------------------------------")




def transfer(sender, receiver, amount):

    if amount <= 0:
        raise ValueError(
            "Transfer amount must be greater than zero."
        )

    if amount > sender.balance:
        raise InsufficientFundsError(
            "Transfer failed: insufficient balance."
        )

    sender.balance -= amount
    receiver.balance += amount

    print(
        f"₹{amount} transferred from "
        f"{sender.holder_name} to "
        f"{receiver.holder_name}."
    )




print("\n========== BANK ACCOUNT TEST ==========")

try:

    mukhi_account = SavingsAccount(
        "Mukhi",
        10000
    )

    arun_account = CurrentAccount(
        "Arun",
        5000,
        3000
    )

    mukhi_account.display_balance()
    arun_account.display_balance()

    # Deposit
    mukhi_account.deposit(2000)

    # Withdraw
    mukhi_account.withdraw(1000)

    # Add interest
    mukhi_account.add_interest(5)

    # Current account withdrawal
    arun_account.withdraw(7000)

    # Transfer
    transfer(
        mukhi_account,
        arun_account,
        3000
    )

except ValueError as error:

    print("Value Error:", error)

except InsufficientFundsError as error:

    print("Insufficient Funds:", error)

finally:

    print("Bank transaction testing completed.")



print("\n========== ERROR HANDLING TEST ==========")

try:

    mukhi_account.deposit(-500)

except ValueError as error:

    print("Caught ValueError:", error)


try:

    mukhi_account.withdraw(50000)

except InsufficientFundsError as error:

    print("Caught InsufficientFundsError:", error)




csv_filename = "students.csv"

students = [
    ["name", "grade"],
    ["Arun", 80],
    ["Rahul", 90],
    ["Mukhi", 85],
    ["Priya", 95]
]


try:

    with open(
        csv_filename,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerows(students)

    print(
        f"\nCSV file '{csv_filename}' created successfully."
    )

except IOError as error:

    print("File error:", error)




grades = []

try:

    with open(
        csv_filename,
        "r"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            grade = int(row["grade"])

            grades.append(grade)

    if len(grades) == 0:
        raise ValueError(
            "No student grades found."
        )

    average_grade = sum(grades) / len(grades)

    print("\n========== STUDENT RESULTS ==========")

    print(
        "Number of students:",
        len(grades)
    )

    print(
        "Average grade:",
        average_grade
    )

except FileNotFoundError:

    print("CSV file was not found.")

except ValueError as error:

    print("Invalid grade data:", error)

except IOError as error:

    print("File reading error:", error)




summary = {
    "total_students": len(grades),
    "average_grade": average_grade,
    "grades": grades
}

json_filename = "summary.json"


try:

    with open(
        json_filename,
        "w"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )

    print(
        f"\nJSON report '{json_filename}' "
        "created successfully."
    )

except IOError as error:

    print("JSON file error:", error)




try:

    with open(
        json_filename,
        "r"
    ) as file:

        report = json.load(file)

    print("\n========== JSON REPORT ==========")

    print(
        "Total Students:",
        report["total_students"]
    )

    print(
        "Average Grade:",
        report["average_grade"]
    )

except FileNotFoundError:

    print("JSON file was not found.")

except json.JSONDecodeError:

    print("Invalid JSON file.")

except IOError as error:

    print("Error reading JSON:", error)



print("\n========== MODULE 3 COMPLETED ==========")
