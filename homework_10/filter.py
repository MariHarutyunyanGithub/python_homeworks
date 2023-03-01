# filter ներդրված ֆունկցիան ստանում է երկու արգումենտ և վերադարձնում իտերատոր։ 
# Եթե ֆունկցիան None է, ապա վերադարձվում են միայն այն էլեմենտները, որոնք true են։ 
# Իրականացնել filter ֆունկցիան։

def filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
        if func(i) == None:
            if i:
                yield i

def None_f(num):
    return 

def foo(num):
    return num <= 0

nums = [1, 2, 3, -8, True, False, -9, 0, 4, 5, 6, 7, 8]
print(list(filter(None_f, nums)))
print(list(filter(foo, nums)))