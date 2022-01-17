# comment
import sys
try:
    notas = sys.argv
    primer_nota=int(sys.argv[1])
    segunda_nota=int(sys.argv[2])
    if len(notas) == 3:
        if (primer_nota < 0 or primer_nota > 10) or (segunda_nota  < 0 or segunda_nota >10):
            print(f"Datos erroneos, las notas deben estar entre 1 y 10, los datos ingresados fueron, {primer_nota}, {segunda_nota}")
            print(f"{primer_nota}, {segunda_nota}, Datos erroneos, las notas deben estar entre 1 y 10, los datos ingresados fueron, {primer_nota}, {segunda_nota}")
        else:
            print("Datos ok")
            if (primer_nota > 7 and segunda_nota > 7):
                print("Promocionado", primer_nota, segunda_nota)
            elif primer_nota >= 4 and segunda_nota >= 4:
                print("Aprobado, debe rendir final, las notas fueron, {} y {}".format(primer_nota, segunda_nota))
            elif primer_nota < 4 and segunda_nota >= 4:
                print("Debe recuperar el primer parcial, las notas fueron, {1} y {0} ".format(segunda_nota, primer_nota))
            elif primer_nota >= 4 and segunda_nota < 4:
                print("Debe recuperar el segundo parcial, las notas fueron, {n1} y {n2}".format(n1=primer_nota, n2=segunda_nota))
            else:
                print("las notas {n1} y {n2} Desaprobado, las notas fueron, {n1} y {n2}".format(n1=primer_nota, n2=segunda_nota))
    else:
        print("Datos incorrectos, solo debe ingresar 2 valores")
except IndexError as e:
    print(e)

