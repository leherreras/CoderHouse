import traceback


while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        resultado = n/m
        if resultado ==1:
            raise IndexError("Error: El resultado es 1")
    except ZeroDivisionError as e:
        print(traceback.format_exc())
    else:
        print("Todo ha funcionado correctamente")
        break # Importante romper la iteración si todo ha salido bien
    finally:
        print("Siempre se ejecuta esta parte")