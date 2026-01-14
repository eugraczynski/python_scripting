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

print(awdadwad.a) # a from instance, not class