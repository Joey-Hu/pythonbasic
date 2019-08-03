# @author: huhao
# @file: huhao_BankSystem.py
# @time: 2019/7/10 13:17
# @Document：https://www.python.org/doc/
# @desc:


import sys
from time import gmtime, strftime


class Bank:
    f1 = open("Accnt_Record.txt", 'r+')
    a = int(f1.readline()) + 1
    f1.close()

    def BankSystem(self):
        print("Enter your choice\n")
        print("1] Create an account in our bank\n")
        print("2] Credit amount in your account\n")
        print("3] Debit amount from your account\n")
        print("4] Check Balance\n")
        print("5] Transaction Summary\n")
        choice = int(input("Please enter your choice:"))

        if choice == 1:
            name = input("Enter name:")
            amt = int(input("\nEnter opening balance:"))
            self.Create(name, amt)
        elif choice == 2 or choice == 3 or choice == 4 or choice == 5:
            name = input("Enter name:")
            accnt_no = int(input("\nEnter Account Number:"))

            f = open(str(accnt_no) + '-pin.txt', 'r')
            p = int(f.readline())
            f.close()

            for i in range(0, 3):
                pin = int(input("Enter pin:"))
                if (not (pin == p)):
                    print("PIN is incorrect. Try again")
                if i == 2:
                    return
                else:
                    break

            if choice == 2 or choice == 3:
                amt = int(input("\nEnter amount:"))
                if choice == 2:
                    self.Credit(accnt_no, name, amt)
                if choice == 3:
                    self.Debit(accnt_no, name, amt)

            if choice == 4:
                self.check_bal(accnt_no)

            if choice == 5:
                self.transact_history(accnt_no)
            print('Thank you for Banking with us!!')

            return

    # 存款
    def Credit(self, accnt_no, name, amt=0):
        f = open(str(accnt_no) + '.txt', 'r+')  # r+、w+可读可写，覆盖
        cb = int(f.readline())
        cb = cb + amt

        # 写交易记录
        ff = open(str(accnt_no) + '-rec.txt', 'a+')
        ff.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + '\t' + str(amt) + "\t     \t" + str(cb) + '\n')
        ff.close()
        self.update(cb, name, accnt_no)
        return

    def Debit(self, accnt_no, name, amt=0):
        f = open(str(accnt_no) + '.txt', 'r+')  # r+、w+可读可写，覆盖
        cb = int(f.readline())
        if cb < amt:
            strin = "Sorry!!\nyou dont have enough balance left in your account to perform this transaction\nCurrent Balance=" + str(
                cb)
            raise ValueError(strin)
        cb = cb - amt
        f.close()

        # 写交易记录
        ff = open(str(accnt_no) + '-rec.txt', 'a+')
        ff.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "\t     \t" + str(amt) + '\t' + str(cb) + '\n')
        ff.close()
        self.update(cb, name, accnt_no)
        return

    def update(self, cb, name, accnt_no):
        f = open(str(accnt_no) + '.txt', 'w')
        f.write(str(cb) + "\n")
        f.write(str(name) + "\n")
        f.write(str(accnt_no) + "\n")
        f.close()

        return

    # def check_bal(accnt_no):

    # self.check_bal(accnt_no)
    # TypeError: check_bal() takes 1 positional argument but 2 were given
    def check_bal(self, accnt_no):
        f = open(str(accnt_no)
                 + '.txt', 'r')
        bal = int(f.readline())
        print('\nCurrent Balance=(INR)',bal)
        f.close()
        return

    def transact_history(self, accnt_no):
        f = open(str(accnt_no) + '-rec.txt', 'r')
        for line in f:
            print(line)
        f.close()
        return

    # 创建账户
    def Create(self, name, amt=0):
        accnt_no = (Bank.a)
        pin = 0
        for i in range(0, 2):
            print("Please Enter an ATM pin (of 4 dgits)")
            pin = int(input())
            if i == 1:
                print("You have exhausted your two attempts.Try again later!!")
                return
            if (pin // 1000 >= 1) and (pin // 10000 == 0):
                break
            print("Enter pin of exaclty 4 digits!!")

        # 写pin文件
        fpin = open(str(accnt_no) + '-pin.txt', 'w')
        fpin.write(str(pin))
        fpin.close()

        # 写Accnt_Record文件
        f1 = open("Accnt_Record.txt", 'w+')
        f1.write(str(Bank.a))
        f1.close()
        Bank.a += 1

        # 写账户文件
        f = open(str(accnt_no) + '.txt', 'w')
        f.write(str(amt) + "\n")
        f.write(str(name) + "\n")
        f.write(str(accnt_no) + "\n")
        f.close()

        # 写Trasaction history文件
        ff = open(str(accnt_no) + '-rec.txt', 'w')
        ff.write("Date                   \tCredit\t Debit\tBalance\n")
        ff.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + '\t' + str(amt) + "\t    \t" + str(amt) + "\n")
        ff.close()
        print('''Congratulations!!
		 Account created successfully!!
		 Your Account No. is -''', accnt_no)
        return


print("****************************************************")
print("*                                                  *")
print("*                                                  *")
print("*              Welcom to Bank System               *")
print("*                                                  *")
print("*                                                  *")
print("****************************************************")

while True:
    ch = int(input("Enter 1 to continue 0 to quit: "))

    # 退出条件
    if ch == 0:
        sys.exit()

    b = Bank()
    b.BankSystem()
