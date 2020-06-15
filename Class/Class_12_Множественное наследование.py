class D:
    pass
class E:
    pass
class B(D,E):
    pass
class C:
    pass
class A(B,C):
    pass
x = A()
isinstance(x, A)
isinstance(x, B)
isinstance(x, object)
isinstance(x, str)
