def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])


account = str(input('Для запуска программы, пожалуйста введите тип аккаунта: >>> '))



def saleman_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    k=0
    a=0
    f = open('saleman.txt')
    for line in f:
        val1,val2 = line.split(' ')
        if val1 == login and val2== password:
            k+=1
            while True:
                menu = str(input('Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 6: '))
                if menu == '1':
                    read_file('sale.txt')
                elif menu == '2':
                    print('1-Поиск по названию')
                    print('2-Поиск по дате')
                    print('3-выход')
                    while True:
                        Number=input('')
                        if Number=='1':
                            Name = str(input('название товара для поиска:>>'))
                            f = open('sale.txt')
                            for line in f:
                                val1, val2 = line.split(' ')
                                print(val2,val1)
                                if Name==val1:
                                    print(val2)
                                return
                        elif Number=='2':
                            Date = str(input('Напишите дату для поиска:>>'))
                            f = open('sale.txt')
                            for line in f:
                                val1, val2 = line.split(' ')
                                print(val2)
                                if Date==val2[:-1]:
                                    print(val1)
                                break
                                
                        elif Number=='3':
                            break
                          
                elif menu == '3':
                    read_file('solt.txt')

                elif menu == '4':
                    read_file('solt.txt')
                    Name = str(input('Название товра для заказа '))
                    Quantity = str(input('Количество '))
                elif menu == '5':
                    deleteOne = str(
                        input('Какой заказ вы бы хотели удалить?>>> '))
                elif menu == '6':
                    return print('Программа завершена, мы будем рады вашему возвращению! ')
              
    if k==a:
        print('Я не понимаю вас')


def delivery_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    f = open('delivery.txt')
    for line in f:
        val1, val2 = line.split(' ')
        if val1 == login and val2 == password:
            while True:
                menu = str(input(
                    'Приветствую дорогой, Доставщик!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7: '))
                if menu == '1':
                    read_file('solt.txt')
                elif menu == '2':
                    read_file('delivered.txt')
                elif menu == '3':
                    deleteOne = str(input(
                        'Какой заказ был доставлен? Введите название оборудование или его серийный номер '))
                elif menu == '4':
                    f=open('delivered.txt')
                    count=0
                    for line in f:
                        count +=1
                    print('Количество доставленных товаров',count)
                elif menu == '5':
                    f=open('solt.txt')
                    count=0
                    for line in f:
                        count +=1
                    print('Количество заказанных товаров',count)  
                elif menu == '6':
                    f=open('delivered.txt')
                    count=0
                    for line in f:
                        val1,val2=line.split(' ')
                        count+=int(val2)
                    print(count)
                elif menu == '7':
                    return print('Программа завершена, мы будем рады вашему возвращению!')
                else:
                    print('Введите пункт из меню')
                continue
        else:
            print('Я не понимаю вас')


def provider_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    f = open('provider.txt')
    for line in f:
        val1,val2 = line.split(' ')
        if val1 == login and val2 == password:
            while True:
                menu = str(input(
                    'Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 5: '))
                if menu == '1':
                    read_file('need_material.txt')
                elif menu == '2':
                    f=open('need_material.txt')
                    count=0
                    for line in f:
                        count+=1
                    print(count)
                    
                elif menu == '3':
                    # количество с самым большим количеством заказов(need_material.txt)
                    print(need_materialTxt)
                elif menu == '4':
                    # колчиство с самым меньшим количеством заказов(need_material.txt)
                    print(need_materialTxt)
                elif menu == '5':
                    return print('Программа завершена, мы будем рады вашему возвращению!')
                else:
                    print('Введите пункт из меню')
                continue
        else:
            print('Я вас не понимаю')


def typeOfAccount(arg):

    if arg.lower() == 'saleman':
        saleman_enter(arg)
    elif arg.lower() == 'delivery':
        delivery_enter(arg)
    elif arg.lower() == 'provider':
        provider_enter(arg)
    else:
        return print('Извините, но мы не нашли такой тип аккаунта, пожалуйста повторите.')


typeOfAccount(account)
