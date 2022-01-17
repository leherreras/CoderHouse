import sys

def par_o_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

while True:
    try:
        num = int(input("Digite um número par para salir del sistema: "))
    except:
        print("Error: debe introducir un numero")
        continue

    resultado = par_o_impar(num)
    print("El numero ingresado es:", resultado)
    if resultado == "par":
        print("Saliendo del bucle...")
        sys.exit()
print("Fin del programa")
