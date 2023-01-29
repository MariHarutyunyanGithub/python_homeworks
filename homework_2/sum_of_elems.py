#Write a program that takes a list of numbers
# and calculates the sum of its elements.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in l:
    sum += i
print('the sum of elements is ' + str(sum))