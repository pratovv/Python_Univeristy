saleman = {
    "login": "saleman",
    "password": "pa$$word123"
}
delivery = {
    "login": "delivery123",
    "password": "delivery123"
}
provider = {
    "login": "provider",
    "password": "provider123"
}

with open('sale.txt') as f:
    for line in f:
        saleTxt,second = line.strip().split(':')
# print(saleTxt,second)

with open('solt.txt') as f:
    for line in f:
        soltTxt = line.strip().split(',')
        
with open('buy.txt') as f:
    for line in f:
        buyTxt = line.strip().split(',')
        
with open('delivered.txt') as f:
    for line in f:
        deliveredTxt = line.strip().split(',')
        
with open('need_material.txt') as f:
    for line in f:
        need_materialTxt = line.strip().split(',')

account = str(input('Для запуска программы, пожалуйста введите тип аккаунта: >>> '))


def saleman_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    if saleman["password"]==password and saleman["login"]==login:
        while True:
            menu = str(input('Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 6: '))
            if menu == '1':
                print(saleTxt)
            elif menu == '2':
                Name = str(input('название товара для поиска:>>'))
                Date = str(input('Напишите дату для поиска:>>'))
                f=open ('sale.txt')
            elif menu == '3':
                print(soltTxt)
            elif menu == '4':
                print(buyTxt)
                Name = str(input('Название товра для заказа '))
                Quantity = str(input('Количество '))
            elif menu == '5':
                deleteOne = str(input('Какой заказ вы бы хотели удалить?>>> '))
            elif menu == '6':
                return print('Программа завершена, мы будем рады вашему возвращению! ')
            else:
                print('Введите пункт из меню ')
            continue
    else:
        print('Я не понимаю вас')


    


def delivery_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    if (delivery["password"]==password and delivery["login"]==login):
        while True:
            menu = str(input('Приветствую дорогой, Доставщик!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7: '))
            if menu == '1':
                print(soltTxt)
            elif menu =='2':
                print(deliveredTxt)
            elif menu =='3':
                deleteOne = str(input('Какой заказ был доставлен? Введите название оборудование или его серийный номер '))
            elif menu =='4':
                print(deliveredTxt) #количество доставленных товаров (quantity добавитть)
            elif menu =='5':
                print(soltTxt) #количество заказанных товаров(quantity добавить)
            elif menu =='6':
                print(deliveredTxt)#сколько получил за каждое оборудование (reduce)
            elif menu =='7':
                return print('Программа завершена, мы будем рады вашему возвращению!')
            else:
                print('Введите пункт из меню')
            continue
    else:
        print('Я не понимаю вас')
        


def provider_enter(arg):
    login = str(input('Введите логин '))
    password = str(input('Введите пароль '))
    if provider["password"]==password and provider["login"]==login:
        while True:
            menu = str(input('Приветствую дорогой, Продавец!Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 5: '))
            if menu =='1':
                print(need_materialTxt)
            elif menu =='2':
                print(need_materialTxt) #количество постовляемого товара (quantity need_material.txt)
            elif menu =='3':
                print(need_materialTxt) #количество с самым большим количеством заказов(need_material.txt)
            elif menu =='4':
                print(need_materialTxt) #колчиство с самым меньшим количеством заказов(need_material.txt)
            elif menu =='5':
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
