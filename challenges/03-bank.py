print("Welcome to Chase bank.")

class BankAccount:
  def __init__(self, owner, balance, interestRate):
    self.owner = owner
    self.balance = balance or 0
    self.interestRate = interestRate or .02

  def __str__(self):
    return"{}'s bank account currently has ${} in it".format(self.owner, self.balance)
  
  def deposit(self):
    deposit_amount = input("Please record how much will be deposited ")
    if (deposit_amount>=0):
      self.balance = self.balance + deposit_amount
      return"{}'s bank account now contains ${}".format(self.owner, self.balance)
    else :
      return False + "While we appreciate the idea of a gift, we do not accept them"
  
  def withdraw(self):
    withdraw_amount = input("How much will you be withdrawing? ")
    if (withdraw_amount > self.balance or withdraw_amount < 0):
      return False + "You are unable to withdraw more than is in your account, or withdraw negative amounts"
    else :   
      self.balance = self.balance - withdraw_amount

basic_account = BankAccount
print(__str__)

print("Have a nice day!")