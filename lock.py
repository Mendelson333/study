from threading import Thread, Lock
import time

lock = Lock()
class BankAccount():
    def __init__(self, count):
        self.count = count
    def deposit(self,amount):
        self.count += amount

    def withdraw(self,amount):
        self.count -= amount

def deposit_task(account, amount):
  for i in range(5):
    with lock:
        account.deposit(amount)
        print(f"Deposited {amount}, new balance is {account.count}")
        time.sleep(1)
def withdraw_task(account, amount):

  for i in range(5):
      with lock:
        account.withdraw(amount)
        print(f"Withdrew {amount}, new balance is {account.count}")
        time.sleep(1)
account = BankAccount(1000)
deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
