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

a = 0
# before while
t1 = time.time()
while a < number:
    a += 1
# after while
t2 = time.time()

print('while_complexity')
print(t2 - t1)
