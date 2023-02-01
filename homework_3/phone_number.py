# Write a program that gets a string from the user containing 
# a potential telephone number. The program should print Valid 
# if it decides the phone number is a real phone number, and 
# Invalid otherwise. A phone number is considered valid as long 
# as it is written in the form abc-def-hijk or 1-abc-def-hijk. The 
# dashes must be included, the phone number should contain only numbers 
# and dashes, and the number of digits in each group must be correct. 

while True:
    num = input('Enter a phone number:')
    ls = list()
    ls = num.split('-')
    if len(ls) != 3 and not(len(ls) == 4 and ls[0] == '1'):
        print('Invalid')
    else:
        valid = True
        for i in ls:
            if not i.isdigit():
                valid = False
                break
        if valid:
            if (len(ls) == 4 and 
                ls[0] == '1' and
                len(ls[1]) == 3 and
                len(ls[2]) == 3 and
                len(ls[3]) == 4):
                print('Valid')
                break
            if (len(ls) == 3 and
                len(ls[0]) == 3 and
                len(ls[2]) == 4):
                print('Valid')
                break
        else:
            print('Invalid')