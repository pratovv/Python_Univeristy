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
                    deleteOne = str(input(
                        'Какой заказ был доставлен? Введите название оборудование или его серийный номер '))
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
