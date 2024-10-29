'''
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

my_decorator(wrapper)
'''

def my_function():
    print("Inside my_function")

my_function() 

'''
Class decoratpr
'''
def add_method(cls):
    def new_method(self):
        print("This is a new method added to the Class, by the decorator")
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self):
        pass

obj = MyClass()
obj.new_method()
