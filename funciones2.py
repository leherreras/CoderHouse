def calculos(numero2: int, numero1: int = None) -> tuple:
    suma=numero1+numero2
    resta=numero1-numero2
    multiplicacion=numero1*numero2
    division=numero1/numero2
    return suma,resta,multiplicacion,division

print(calculos(numero2=2))

def suma(*args) -> int:
    return sum(args)

def suma2(**kargs) -> int:
    return sum(kargs.values())

def suma3(*args,**kargs) -> int:
    return suma(*args) + suma2(**kargs)
# print(suma(1,2,3,4,5))
# print(suma2(n1=1,n2=2,n3=3,n4=4))
# print(suma3(1,2,3,4,5,n1=1,n2=2,n3=3,n4=4))
