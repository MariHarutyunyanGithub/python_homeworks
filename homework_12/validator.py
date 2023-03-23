# Իրականացնել կոդում առկա դեկորատորները հետևյալ սկզբունքներով

# @input_validator
# @adder
# def add_numbers(a, b) : return a + b

# @input_validator դեկորատորը պետք է ստուգում կատարի, որ @adder 
# դեկորտարտորը կանչվի հստակ երկու արգումենտով, իսկ @adder դեկորատորը 
# իր հերթին պետք է արտածի add_numbers-ի գործողությունը։ Մեկ ավելացում, 
# որ այստեղ պետք է հաշվի առնել դեկորատորների կանչման հերթականությունը։

def input_validator(func):
    def wrapper(*args, **kwargs):
        assert len(args) == 2, 'add_numbers() takes 2 positional arguments'
        return func(*args, **kwargs)
    return wrapper


def adder(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@adder
@input_validator
def add_numbers(a, b): 
    return a + b 

print(add_numbers(4, 5))