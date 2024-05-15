class Test:
    d=500 #static variable

    def m1(self):
        self.a=100
    def m2(self):
        self.b=200
    def m3(self):
        self.c=300
 
t1=Test()
t1.m1()
t1.m2()
t1.m3()

print(t1.__dict__)