class Normal:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __repr__(self):
        return f"Normal(a={self.a}, b={self.b})"
    
    def __add__(self, other):
        return Normal(self.a + other.a, self.b + other.b)
    
    def __call__(self, *args, **kwds):
        pass

p1 = Normal(1, 2)

list_ = [1,2,3,4,5]
list_.__add__([6,7,8,9,10])





class One:
    def __init__(self, a, b):
        self.b = b
        self.a = a

class NEW:
    def __init__(self, b):
        self.a = 5
    g = 3

class Two(One, NEW):
    def __init__(self, a, b=4):
        super().__init__(a, b)
    a = 7
    b = 2
    c = 3

awdadwad = Two(2)

# print(awdadwad.a) # a from instance, not class


class One:
    a = 1

class Two(One):
    def __init__(self):
        self.a = 2
    b = 2
    c = One.a + 1

awdadwad = Two()
# print(awdadwad.c)


