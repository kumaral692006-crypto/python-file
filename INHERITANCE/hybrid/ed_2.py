class bank:
    def branch(self):
        print("welcometo indian bank user")

class savings(bank):
    def savings (self):
        print("student is studying")

class premiumsaving(bank):
    def k_acc(self):
        print("yu have premiumsaving")

class balance(savings,premiumsaving):
    def intern_task(self):
        print("currect account ")

a= savings()
b=premiumsaving()
c=balance()
a.savings()
b.k_acc()
c. intern_task()