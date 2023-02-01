def f(text, shift):
    c = text.encode()
    s = bytearray(c)
    if shift > 0:
        for i in range(len(s)):        
            if s[i] >= 65 + shift and s[i] <= 90:
                s[i] -= shift
            elif s[i] >= 65 and s[i] < 65 + shift:
                s[i] -= shift - 26
            elif s[i] >= 97 + shift and s[i] <= 122:
                s[i] -= shift
            elif s[i] >= 97 and s[i] < 97 + shift:
                s[i] -= shift - 26
    else:
        for i in range(len(s)):
            if s[i] >= 65 and s[i] <= 90 + shift:
                s[i] -= shift
            elif s[i] > 90 + shift and s[i] <= 90:
                s[i] -= 26 + shift
            elif s[i] >= 97 and s[i] <= 122 + shift:
                s[i] -= shift
            elif s[i] > 122 + shift and s[i] <= 122:
                s[i] -= 26 + shift
    text = s.decode()
    return text

def my_decode(file_name, shift):
    try:
        file = open(file_name)
    except:
        print('file open failed!!')
        return
    other_file = open('decoded.txt', 'w')
    line = 'hello file'
    while line != '':
        line = file.readline()
        line = f(line, shift)
        other_file.write(line)
    file.close()
    other_file.close()