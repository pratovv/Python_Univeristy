def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])
        
def provider_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    validate = False
    f = open('./accounts/provider.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2[:-1] == password:
            validate = True
            while True:
                menu = str(input(
                    'Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 5: '))
                if menu == '1':
                    read_file('./data/need_material.txt')
                elif menu == '2':
                    f = open('./data/need_material.txt')
                    count = 0
                    for line in f:
                        count += 1
                    print(count)

                elif menu == '3':
                    array = []
                    f = open('./data/need_material.txt')
                    for line in f:
                        val1, val2 = line.split(' ')
                        array.append(val1+' '+val2[:-1])
                        array.sort(key=lambda x: int(x.split()[1]))
                    max = int(array[-1].split()[1])
                    for line in reversed(array):
                        price = int(line.split()[1])
                        if(price == max):
                            print(line)
                elif menu == '4':
                    array = []
                    f = open('./data/need_material.txt')
                    for line in f:
                        val1, val2 = line.split(' ')
                        array.append(val1+' '+val2[:-1])
                        array.sort(key=lambda x: -int(x.split()[1]))
                    max = int(array[-1].split()[1])
                    for line in reversed(array):
                        price = int(line.split()[1])
                        if(price == max):
                            print(line)
                elif menu == '5':
                    return print('Программа завершена, мы будем рады вашему возвращению!')
                else:
                    print('Введите пункт из меню')
                continue
    if validate == False:
        print('Я не понимаю вас')