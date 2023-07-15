class Account:
    def __init__(self):
        # Account initialization logic
        pass

    def withdraw(self, amount):
        # Withdrawal logic
        pass


class Savings(Account):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if amount > 5000:
            return "You have reached your daily limit."
        else:
            return super().withdraw(amount)


savings = Savings()
print(savings.withdraw(2000))
