# Իրականացնել սեփական MyIterable class-ը, որը կունենա iter և next ատրիբուտները։

class myIterable:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            value = self.iterable[self.index]
            self.index +=1
            return value
        else:
            raise StopIteration
    
ls = [1, 2, 3, 'hello']
x = iter(myIterable(ls))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))
