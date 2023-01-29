#Write a program that checks if a string is a palindrome.

s = input('please, enter a string\n')
ls = list(s)
ls.reverse()
s1 = ''.join(ls)
if s == s1:
    print('the string is a palindrome')
else:
    print('the string is not a palindrome')