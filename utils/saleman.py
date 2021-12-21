def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])

def saleman_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    validate = False
    f = open('./accounts/saleman.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2[:-1] == password:
            validate = True
            while True:
                menu = str(input(
                    'Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 6: '))
                if menu == '1':
                    read_file('./data/sale.txt')
                elif menu == '2':
                    print('1-Поиск по названию')
                    print('2-Поиск по дате')
                    print('3-выход')
                    while True:
                        Number = input('')
                        if Number == '1':
                            Name = str(input('Поиск товара по названию:>>'))
                            f = open('./data/sale.txt')
                            result = False
                            for line in f:
                                val1, val2 = line.split(' ')
                                if Name.lower() == val1.lower():
                                    result = True
                                    print(line)
                            if result == False:
                                print('Такого товара нет')
                        elif Number == '2':
                            Date = str(input('Поиск товара по дате:>>'))
                            f = open('./data/sale.txt')
                            result = False
                            for line in f:
                                val1, val2 = line.split(' ')
                                if Date.lower() == val2[:-1].lower():
                                    result = True
                                    print(line)
                            if result == False:
                                print('Товара по данной дате нет')
                        elif Number == '3':
                            break
                        else:
                            print('Нет команды')

                elif menu == '3':
                    read_file('solt.txt')

                elif menu == '4':
                    read_file('order.txt')
                    Name = str(input('Название товара для заказа-> '))
                    Quantity = str(input('Количество-> '))
                    with open('order.txt', "a+") as file:
                        file.write(Name+" "+Quantity+"\n")
                elif menu == '5':
                    array = []
                    f = open('solt.txt')
                    for line in f:
                        array.append(line)
                    for i in range(len(array)):
                        print(str(i+1)+'.'+array[i])
                    deleteOne = int(
                        input('Какой заказ вы бы хотели удалить (Выберите цифру)?>>> '))
                    for i in range(len(array)):
                        if i == deleteOne-1:
                            array.remove(array[i])
                    with open('solt.txt', "w") as file:
                        for line in array:
                            file.write(line)
                    print('У вас осталось:')
                    read_file('solt.txt')

                elif menu == '6':
                    return print('Программа завершена, мы будем рады вашему возвращению! ')

    if validate == False:
        print('Я не понимаю вас')

