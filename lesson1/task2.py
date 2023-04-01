from f import center

word1 = b'class'
word2 = b'function'
word3 = b'method'


print(center('Тип', 'Содержимое', 'Длина', header=True))
for w in word1, word2, word3:
    print(center(type(w), w, len(w)))
