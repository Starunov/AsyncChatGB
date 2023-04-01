from f import center

words = ['attribute', 'класс', 'функция', 'type']

print(center('Строка', 'Запись в байтовом типе', header=True))
for word in words:
    try:
        print(center(word, bytes(word, 'ascii')))
    except UnicodeEncodeError:
        print(center(word, '\033[31m error'))
