import functools
from flask import Flask
import logging

app = Flask(__name__)

def function_logger(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        logging.basicConfig(filename='function.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(f"Function {func.__name__} called with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return new_func

@app.route('/')
@function_logger
def index():
    return 'Hello, World!'

@app.route('/add/<int:x>/<int:y>')
@function_logger
def add(x, y):
    return str(x + y)

if __name__ == '__main__':
    app.run()
