# Իրականացնել for օգտագործելով iterator։

def my_for(iterable):
    start = 0
    it = iter(iterable)   
    while start < len(iterable):
        value = start
        start = next(it)
        yield value

ls = [1, 2, 3, 4]
print(list(my_for(ls)))