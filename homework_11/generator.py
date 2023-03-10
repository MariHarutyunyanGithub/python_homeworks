# Իրականացնել map, reduce, range ֆունկցիաները օգտագործելով գեներատոր ֆունկցիաներ։

def my_map(func, *iterable):
    for i in zip(*iterable):
        yield func(*i)

ls = [-1, -2, 3, 4]
ls1 = [1, 2, 3, 4, 5, 6]
print(list(my_map(pow,ls,ls1)))
print(list(my_map(abs, ls)))

# ####################################################################

def my_reduce(func, iterable):
    current = iterable[0]
    for next in iterable[1:]:
        current = func(current, next)
    yield current

ls = [2, 3, 4]
print(list(my_reduce(pow, ls)))

# #####################################################################

def my_range(start, end = None, step = 1):
    if end is None:
        end = start
        start = 0
    if (not isinstance(start, int) or
        not isinstance(end, int) or
        not isinstance(step, int)):
        print('the argument is not an integer')
        raise TypeError    
    while start < end:
            value = start
            start += step
            yield value

print(list(my_range(-9, 3, 2)))
print(list(my_range(-9, 3)))
print(list(my_range(9)))