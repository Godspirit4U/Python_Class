class A:
    def details1(self):
        print("Class A")

class B:
    def details2(self):
        print("Class B")

class C(A, B):
    def details3(self):
        super().details1()
        super().details2()


c = C()
c.details3()
# c.details2()