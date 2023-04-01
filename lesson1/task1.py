from f import center


words = ['разработка', 'сокет', 'декоратор']

print(center('Тип', 'Содержание', header=True))
for word in words:
    print(center(type(word), word))

unicode_word1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
unicode_word2 = '\u0441\u043e\u043a\u0435\u0442'
unicode_word3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
uw_list = [unicode_word1, unicode_word2, unicode_word3]

print()

print(center('Тип', 'Содержание', 'Кодовое представление', header=True))
for uw in uw_list:
    print(center(type(uw), uw, uw.encode('unicode_escape').decode('utf_8')))
