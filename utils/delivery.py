from os import read


def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])
        
def delivery_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    validate = False
    f = open('./accounts/delivery.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2[:-1] == password:
            validate = True
            while True:
                menu = str(input(
                    'Приветствую дорогой, Доставщик!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7: '))
                if menu == '1':
                    read_file('./data/solt.txt')
                elif menu == '2':
                    read_file('./data/delivered.txt')
                elif menu == '3':
                    array = []
                    f = open('./data/delivered.txt')
                    for line in f:
                        array.append(line)
                    for i in range(len(array)):
                        print(str(i+1)+'.'+array[i])
                    deleteOne = int(input(
                        'Какой заказ вы бы хотели удалить (Выберите цифру)?>>> '))
                    for i in range(len(array)):
                        if i == deleteOne-1:
                            array.remove(array[i])
                            with open ("report.txt","w")as f:
                                f.write(str(array[i]))
                    with open('./data/delivered.txt', "w") as file:
                        for line in array:
                            file.write(line)
                    print('У вас осталось:')
                    read_file('./data/delivered.txt')
                elif menu == '4':
                    f = open('./data/delivered.txt')
                    count = 0
                    for line in f:
                        count += 1
                    print('Количество доставленных товаров', count)
                elif menu == '5':
                    f = open('./data/solt.txt')
                    count = 0
                    for line in f:
                        count += 1
                    print('Количество заказанных товаров', count)
                elif menu == '6':
                    f = open('./data/delivered.txt')
                    count = 0
                    for line in f:
                        val1, val2 = line.split(' ')
                        count += int(val2)
                    print(count)
                elif menu == '7':
                    return print('Программа завершена, мы будем рады вашему возвращению!')
                else:
                    print('Введите пункт из меню')
                continue
    if validate == False:
        print('Я не понимаю вас')
