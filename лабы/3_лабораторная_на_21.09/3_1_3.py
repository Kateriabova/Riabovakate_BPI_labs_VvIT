with open("example.txt", 'r') as f: # открытие файла с последующим закрытием на чтение
    text = f.readlines()  # чтение всех строк в массив строчек
    print(''.join(text))  # объединение всех строк и последующий вывод на экран

with open("example.txt", 'r') as f:
    text_2 = f.read() # чтение всего файла стандартным методом read
    print(text_2)

with open("example.txt", 'r') as f:
    for line in f: # построчное чтение файла и отдельный вывод каждой строки на экран
        print(f.readline())

with open("example.txt", 'r') as f:
    text_4 = f.read(18) # чтение первых 18 знаков файла
    print(text_4)

with open("example.txt", 'r') as f:
    print(*f) # читерский способ выведения на экран содержимого всего файла
