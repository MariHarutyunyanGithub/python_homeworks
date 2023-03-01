# In Python, the for loop is generally faster than the while 
# loop for iterating over sequences such as lists, tuples, 
# and strings. This is because Python's for loop is implemented 
# as an optimized C loop that can quickly and efficiently 
# iterate over the elements in a sequence, while the while 
# loop requires more Python bytecode to perform the same task.


import time

a = 0
number = 100000000
# before for
t1 = time.time() 
for i in range(number):
    a += 1
# after for
t2 = time.time()

print('for_complexity')
print(t2 - t1) 
# prints 6.0851829051971436

a = 0
# before while
t1 = time.time()
while a < number:
    a += 1
# after while
t2 = time.time()

print('while_complexity')
print(t2 - t1)
# prints 6.852759122848511