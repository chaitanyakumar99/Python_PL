class Employee:
    org_name="TCS"

    def set_ename(self,name):
        self.ename=name 
    def set_esal(self,sal):
        self.esal=sal 
e1=Employee()
e1.set_ename('Rahul')
e1.set_esal(65000)

e2=Employee()
e2.set_ename('Kumar')
e2.set_esal(75000)

e3=Employee()
e3.set_ename('Varma')
e3.set_esal(95000)

print(e1.__dict__)  
print(e2.__dict__)
print(e3.__dict__)

print(Employee.__dict__)
