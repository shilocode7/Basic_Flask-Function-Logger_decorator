import logging

def function_logger(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='function.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(f"Function {func.__name__} called with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@function_logger
def my_function(x, y):
    return x + y


print (my_function(5,5))

@function_logger
def calc(x,y,tf):
    def add_one(x,y):
        return x + y
    def minos_one(x,y):
        return x - y
    if tf == True:
        return add_one
    else:
        return minos_one

# print(calc(5, 2, True)(5, 2)) 
