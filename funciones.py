import sys

def suma_dos_numeros(numero1: int, numero2: int) -> int:
    # Acciones a realizar
    if type(numero1) == int and type(numero2) == int:
        resultado = numero1 + numero2
    else:
        return
    return resultado

try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
except ValueError:
    print("Error: los valores deben ser numeros enteros")
    sys.exit(1)

resultado_suma = suma_dos_numeros(n1, n2)
print(resultado_suma)