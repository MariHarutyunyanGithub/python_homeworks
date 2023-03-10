# Իրականացնել սեփական MyIterable class-ը, որը կունենա iter և next ատրիբուտները։

class myIterable:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            value = self
            self.index +=1
            return value
        else:
            raise StopIteration
    
    def print(self):
        print(self.iterable)

m = myIterable((1, 2, 3, 4, 5, "hello"))
if hasattr(m, '__iter__'):
    print("it is iterable")
m.print()