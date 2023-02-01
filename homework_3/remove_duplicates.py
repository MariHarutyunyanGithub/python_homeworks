#Write a program that accepts a string from the user and removes all duplicates.
# The resulting string should contain only unique characters.

my_str = input('Please, input a string\n')
s = set(my_str)
my_str = ''.join(s)
print(my_str)