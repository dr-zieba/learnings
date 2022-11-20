class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """Checking account class"""

    acc_type = "Checking"

    def __init__(self, filepath):
        Account.__init__(self, filepath)
        self.fee = 1

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

check = Checking(r"C:\Users\zieba\Desktop\python\10appCourse\account\balance.txt")
check.deposit(100)
print(check.balance)
check.transfer(500)
check.commit()
print(check.balance)
print(check.acc_type)
print(check.__doc__)