# Write a program that asks the user to enter a character,checks,
# and prints whether the character is a consonant or a vowel.

while True:
    char = input('Please, enter a character to check consonant or vowel\n')
    if len(char) > 1 or not char.isalpha():
        print('your input is not valid!')
    else:
        if (char == 'a' or
            char == 'i' or
            char == 'u' or
            char == 'e' or
            char == 'o'):
            print('the character is vowel')
            break
        else:
            print('the character is consonant')
            break