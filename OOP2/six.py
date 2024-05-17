class Test:
    a=10   #static variable

    def m1(self):
        self.b=200
    def m2(self):
        self.c=300
    def m3(self):
        self.d=600
    
t1=Test()
t1.m1()

t2=Test()
t2.m2()

t3=Test()
t3.m3()

t4=Test()
print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)
print(t4.__dict__)   