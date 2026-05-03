class A:
    def __init__(self):
        print("Class A")


class B:
    def __init__(self):
        print("Class B")


class C(A, B):
    def __init__(self):
        super().__init__()
        super(A, self).__init__()
        print("Class C")

# print(C.__mro__)
c = C()
