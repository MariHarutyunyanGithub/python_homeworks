# Pdf ֆայլից (US_Declaration.pdf) դուրս բերել նահանգների և մարդկանց անունները և 
# համապատասխանաբար պահել բառարանի մեջ (dict)։

import PyPDF2

my_dict = dict()
text_lines = []
states = []
# text_lines լիստի մեջ տող առ տող լցնում ենք ամբողջ տեքստը
with open('US_Declaration.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)
    for page in pdf_reader.pages: 
        for line in page.extract_text().splitlines():
            text_lines.append(line)

# states լիստի մեջ լցնում ենք նահանգների անունները
for line in range(87, len(text_lines) - 1):
    if text_lines[line][len(text_lines[line]) - 1] == ':':
        if '[' in text_lines[line]:
            for i in range(len(text_lines[line])):
                if text_lines[line][i] == ']':
                    states.append(text_lines[line][i + 2:-1])
        else:
            states.append(text_lines[line][1:-1])

# my_dict dictionary֊ի մեջ map ենք անում ամեն նահանգի անունը և համապատասխան մարդկանց անունները
for line in range(87, len(text_lines) - 1):
    for state in range(1, len(states)):        
        if states[state - 1] in text_lines[line]:
            my_dict[states[state - 1]] = []
            i = 1
            while states[state] not in text_lines[line + i] and (line + i != len(text_lines) - 1):
                my_dict[states[state - 1]].append(text_lines[line + i][3:])
                i += 1
            

for i, j in my_dict.items():
    print(i,':', j)