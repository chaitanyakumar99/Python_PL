class Test():
      
    def m1(self):
        self.a=30
    @classmethod
    def m2(cls):
        cls.b=50
    @classmethod
    def m3(cls):
       cls.c=100
    @staticmethod
    def m4():
       d=400
    @staticmethod
    def m4():
       e=500

t1=Test()
t1.m1()
t1.m2()
t1.m3()
t1.m4()

print(t1.__dict__)
print(Test.__dict__)


  