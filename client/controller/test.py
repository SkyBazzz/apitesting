def wrapper(func):
    def wrap():
        return "Fibo"
    return wrap


def some_func():
    return "Fibonaci"


f = wrapper(some_func)
print(f())
print(some_func())