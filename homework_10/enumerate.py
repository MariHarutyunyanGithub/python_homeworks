# enumerate ներկառուցված մեթոդը ավելացնում է հաշվիչ (counter) իտերացվող 
# օբյեկտի վրա և վերադարձնում է enumerate օբյեկտ, որն էլ իր հերթին 
# հնարավոր է ներկայացնել list-ի տեսքով։ Իրականացնել պարզագույն enumerate 
# ֆունկցիա, որն առաջին արգումենտով կստանա իտերացվող օբյեկտը (պետք է ստուգում 
# կատարել՝ արդյոք փոխանցված օբյեկտը իտերացվող է), իսկ երկրորդ արգումենտով start, 
# որն էլ նշանակում է հաշվարկի սկիզբը(default 0 է վերագրված)։ 
# Վերադարձվող օբյեկտը կարող է լինել tuple-ների list։

def enumerate(iterable, start = 0):
        if not hasattr(iterable, '__iter__'):
            print(f'{iterable} is not iterable')
            exit()
        res = []
        for i in range(len(iterable)):
            res.append((start + i, iterable[i]))
        return res        

ls = [1, 2, 3, 'hello', False, ['a', 'b']]
print(enumerate(ls, 8))