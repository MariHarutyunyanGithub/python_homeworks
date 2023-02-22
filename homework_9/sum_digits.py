# Գրել sum_digits անունով ֆունկցիա, որը վերադարձնում է 
# իրեն փոխանցված ամբողջ թվի թվանշանների գումարը:

def sum_digits(num):
    num_list = list(str(num))
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    sum1 = sum(num_list)
    return sum1
  
number = 0
print(sum_digits(number))