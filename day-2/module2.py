

class BankAccount:

    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.balance = balance

  
    def deposit(self, amount):
        self.balance += amount

        print(
            f"₹{amount} deposited into "
            f"{self.holder_name}'s account."
        )

    # Withdraw money
    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount

            print(
                f"₹{amount} withdrawn from "
                f"{self.holder_name}'s account."
            )

        else:
            print(
                f"Insufficient balance in "
                f"{self.holder_name}'s account."
            )

    # Display account details
    def display_balance(self):
        print("--------------------------------")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")
        print("--------------------------------")




class SavingsAccount(BankAccount):

    def add_interest(self, rate):

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

        # Call parent class constructor
        super().__init__(holder_name, balance)

        self.overdraft_limit = overdraft_limit

    # Override withdraw method
    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft_limit:

            self.balance -= amount

            print(
                f"₹{amount} withdrawn from "
                f"{self.holder_name}'s account."
            )

        else:

            print(
                f"Overdraft limit exceeded for "
                f"{self.holder_name}'s account."
            )

    # Display overdraft information
    def display_balance(self):

        print("--------------------------------")
        print(f"Account Holder  : {self.holder_name}")
        print(f"Balance         : ₹{self.balance}")
        print(f"Overdraft Limit : ₹{self.overdraft_limit}")
        print("--------------------------------")



def transfer(sender, receiver, amount):

    if amount <= sender.balance:

        sender.balance -= amount
        receiver.balance += amount

        print(
            f"₹{amount} transferred from "
            f"{sender.holder_name} to "
            f"{receiver.holder_name}."
        )

    else:

        print(
            f"Transfer failed: "
            f"{sender.holder_name} has insufficient balance."
        )




# Savings account
mukhi_account = SavingsAccount(
    "Mukhi",
    10000
)

# Current account
bala_account = CurrentAccount(
    "Bala",
    5000,
    3000
)




print("\n===== MUKHI'S ACCOUNT =====")

mukhi_account.display_balance()

# Deposit
mukhi_account.deposit(2000)

# Withdraw
mukhi_account.withdraw(1000)

# Add 5% interest
mukhi_account.add_interest(5)

# Display final balance
mukhi_account.display_balance()




print("\n===== bala'S ACCOUNT =====")

bala_account.display_balance()

# Deposit
bala_account.deposit(2000)

# Withdraw
bala_account.withdraw(3000)

# Display balance
bala_account.display_balance()




print("\n===== TRANSFER =====")

transfer(
    mukhi_account,
    bala_account,
    3000
)




print("\n===== FINAL BALANCES =====")

mukhi_account.display_balance()

bala_account.display_balance()
