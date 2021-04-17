#Сделать проверку, что хотя бы один из введенных символов в перменной яляется цифрой
while 0==0:
    word=input('Введите слово:')
    for symbol in word:
        if symbol.isdigit():
            print('Есть цифра!')
            break

