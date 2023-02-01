# Write a program that implements the Caesar cipher,a simple
# encryption technique where each letter in the plaintext is
# shifted a certain number of places down the alphabet

import encode
import decode

while True:
    to_do = input('1 to encode\n2 to decode\n')
    if to_do == '1':
        path = input('enter the file name (or path) where the text to be encoded is located\n')
        print('enter a number of shifts and the direction you want(on range[-25,25]).') 
        print('if the number you enter is positive, the shift direction is left, otherwise it is right')
        while True:    
            try:       
                digit = int(input('number: '))
                if digit < -25 or digit > 25:
                    print('your input is out of range required')
                else:
                    break
            except:
                print('your input is not valid, try again')            

        encode.my_encode(path, digit)
        break
    elif to_do == '2':
        path = input('enter the file name (or path) where is located the text to be decoded\n')
        print('enter a number of shifts and the direction you need(on range[-25,25]).') 
        print('if the number you enter is positive, the shift direction is right, otherwise it is left')
        while True:    
            try:       
                digit = int(input('number: '))
                if digit < -25 or digit > 25:
                    print('your input is out of range required')
                else:
                    break
            except:
                print('your input is not valid, try again')            

        decode.my_decode(path, digit)
        break
    else:
        print('your input is not valid!!')