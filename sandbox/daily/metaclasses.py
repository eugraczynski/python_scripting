
# Example 1:
# Prevention of attribute name clashes - on CLIENT side
# LIBRARY CODE
class Base:
    def foo(self):
        return "foo from Base"
    
# CLIENT CODE
# before you can assert it has req method

assert hasattr(Base, "foo")

class Derived(Base):
    def bar(self):
        return self.foo()

p2 = Derived()
p2.bar() # raises an error, if method changed name in Base class, client code will break


# Example 2:
# Prevention of attribute name clashes - on LIBRARY side
# LIBRARY CODE
class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if name != "Base" and not 'bar' in body:
            raise TypeError("Derived classes must implement 'bar' method")
        return super().__new__(cls, name, bases, body)
    

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    
    def __init_subclass__(self, *args, **kwargs):
        print(f"Registering subclass {self.__name__} ", args, kwargs)
        return super().__init_subclass__(*args, **kwargs)
    


# CLIENT CODE

class Derived(Base):
    def bar(self):
        return 'bar from Derived'

p2 = Derived()
p2.bar() # raises an error, if method changed name in Base class, client code will break


