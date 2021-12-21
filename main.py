from os import name, remove
from utils.delivery import *
from utils.provider import *
from utils.saleman import *

def read_file(file):
    f = open(file)
    for line in f:
        print(line[:-1])

account = str(
    input('Для запуска программы, пожалуйста введите тип аккаунта: >>> '))

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
