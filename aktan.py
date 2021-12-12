import random 
name=input('name: ')
def gey(name):
    count=random.randint(1,2)
    if count == 1:
        print(f"{name} is gey!")
    elif count == 2:
        print(f"{name} is not gey!")
        
# gey(name)

def herSize(name):
    count=random.randint(1,25)
    print(f"{name}'s size of his dig is{count}sm")
    if count<=9:
        print('Мелкочленник')
    elif count>=10 and count<= 15:
        print('таксебечленник')
    elif count>=16 and count<=21:
        print('Пойдетчленник')
    elif count>=17:
        print('Огромночленник')
# herSize(name)


 