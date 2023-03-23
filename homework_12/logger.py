# Իրականացնել կոդում առկա դեկորատորները՝  հետևյալ սկզբունքներով

# @my_logger
# def display(name, age):
#    print('display info has two arguments ({}, {})'.format(name, age))

# @my_logger դեկորատորը պետք է ստեղծի պարզագույն loger, 
# որում կավելանան տողեր ամեն ֆունկցիան կանչելիս։

# display('James', 25) -> INFO:root:Ran with args: ('James', 25), and kwargs: {}
# display('Hank', 30) -> INFO:root:Ran with args: ('Hank', 30), and kwargs: {}

def my_logger(foo):
    def wrapper(*args, **kwargs):
        print(f'INFO:root:Ran with args: {args} and kwargs {kwargs}')
        foo(*args, **kwargs)
        print('\n')
    return wrapper

di = {'c': 5, 'd': 'hello'}
a = 8
b = 1
@my_logger
def display(*args, **kwargs):
    count = len(args) + len(kwargs)
    print(f'display info has {count} arguments', *args, *kwargs)

display('James', 25)
display('Hank', 30, 'hello')
display(a, b, **di)
display(name = 'James', age = 25, address = 'Yerevan')