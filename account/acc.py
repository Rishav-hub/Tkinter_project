#account=Account("account//balance.txt")
class Account:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.bal=int(file.read())


    def withdraw(self,amount):
        self.bal= self.bal-amount

    def deposite(self,amount):
        self.bal= self.bal+amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.bal))

class Checking(Account):
    def __init__(self,filepath,tax):
        Account.__init__(self,filepath)
        self.tax=tax

    def transfer(self,amount):
        self.bal= self.bal-amount-self.tax



checking=Checking("account//balance.txt",0.0018)
print(checking.bal)
checking.transfer(20)
print(checking.bal)
checking.commit()
