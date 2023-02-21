# implement switch-case by Python

# def month_to_string(month):
#     match month:
#         case 1:
#             return "January"
#         case 2:
#             return "February"
#         case 3:
#             return "March"
#         case 4:
#             return "April"
#         case 5:
#             return "May"
#         case 6:
#             return "June"
#         case 7:
#             return "July"
#         case 8:
#             return "August"
#         case 9:
#             return "September"
#         case 10:
#             return "October"
#         case 11:
#             return "November"
#         case 12:
#             return "December"
#         case default:
#             return "your input is not valid"


def month_to_string(month):
    my_dict = {
                1:'January',
                2:'February',
                3:'March',
                4:'April',
                5:'May',
                6:'June',
                7:'July',
                8:'August',
                9:'September',
                10:'October',
                11:'November',
                12:'December'
               }
    return my_dict.get(month, 'your input is not valid')


while True:
    try:
        month = int(input('please; enter the number of range(1;12)\n'))
        break
    except:
        print('your input is not a number!!!')

print(month_to_string(month))