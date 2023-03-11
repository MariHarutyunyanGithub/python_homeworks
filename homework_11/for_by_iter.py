# Իրականացնել for օգտագործելով iterator։

def my_for(iterable):
    if not hasattr(iterable, '__iter__'):
        print('object is not iterable')
        raise TypeError
    start = 0
    it = iter(iterable)   
    while start < len(iterable):
        value = next(it)
        start += 1
        yield value

ls = ['hello', 'world']
x = iter(my_for(ls))

print(next(x)) # 'hello'
print(next(x)) # 'world'
# print(next(x)) # StopIteration

print(list(my_for(ls)))