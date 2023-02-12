from googletrans import Translator

my_dict = {}
file = open('words.txt')
word = 'nonempty'
while word != '':
    word = file.readline()
    translated_text = Translator().translate(word, dest='hy')
    my_dict[word] = translated_text.text

for key,value in my_dict.items():
    print('{:<15}'.format(key.strip()), end = '')
    print(value)