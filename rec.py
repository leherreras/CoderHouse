def cuenta_regresiva(numero):
    print(numero)
    numero -= 1
    if numero > 0:
        cuenta_regresiva(numero)
    else:
        print("Boooom!")

cuenta_regresiva(5)

def factorial(numero):
    if numero > 1:
        numero =numero * factorial(numero-1) # 5 * 4 * factorial(3)
    return numero


numero = 5
print("Valor inicial->", numero)
res = factorial(numero)
print("Valor final->", res)