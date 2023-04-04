from f import center

words = ['разработка', 'администрирование', 'protocol', 'standard']

print(center('Строковое представление', 'Обратное преобразование', 'Байтовое представление', header=True))
for word in words:
    we = word.encode('utf-8')
    wd = we.decode('utf-8')
    print(center(word, wd, we))
