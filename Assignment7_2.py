class BankAccount:
    ROI = 10.3

    def __init__(self, custnm, value):
        self.name = custnm
        self.amount = value

    def Deposit(self, val):
        self.amount = self.amount + val

    def Withdraw(self, val):
        self.amount = self.amount - val

    def Display(self):
        print ("Customer Name::", self.name)
        print ("Amount::", self.amount)

    def CalculateIntrest(self):
        ans = ((BankAccount.ROI / 100) * self.amount) + self.amount
        print ("Calculated value is==", ans)


def main():
    obj1 = BankAccount("Raj", 10000)
    print(obj1.name)
    print(obj1.amount)
    obj1.CalculateIntrest()
    obj1.Deposit(400)
    print(obj1.amount)
    obj1.Withdraw(200)
    print(obj1.amount)

    obj1.Display()


if __name__ == "__main__":
    main()
