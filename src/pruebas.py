import random

try:
    n1= int(input("Dame un numero: "))
    n2= int(input("Dame un numero: "))
    ran=random.randint(n1, n2)
    print("El numero random es: "+str(ran))
except ValueError:
    print("jaja te mamaste")