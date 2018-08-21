class A:
    def method(self):
        print("class A")


class B(A):
    def method(self):
        print("class B")


class C(A):
    def method(self):
        print("class B")


class D(B, C):
    def __init__(self):
        self.method()


d = D()
