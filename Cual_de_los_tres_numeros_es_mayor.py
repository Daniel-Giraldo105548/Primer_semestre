##Area de descripción
##Programado por: Daniel Giraldo Giraldo
##Fecha: 12/03/2023
##Este programa: Calcula el mayor número de tres

##Titulo
print("****************************************")
print("Calcular el número mayor de tres números")
print("**************************************** \n")

##Entrada de datos y declaración de variabale
nom = input("Digite su nombre: ")
num_uno = int(input( nom + " digite el primer número: "))
num_dos = int(input( nom + " digite el segundo número: "))
num_tre = int(input( nom + " digite el tercer número: "))

##Proceso y salida
if num_uno > num_dos:
    print(nom + " el número  mayor es: ", num_uno)
elif num_uno < num_dos:
    print(nom + " el número  mayor es: ", num_dos)
elif num_uno < num_tre:
    print(nom + " el número  mayor es: ", num_uno)
elif num_uno > num_tre:
    print(nom + " el número  mayor es: ", num_tre)
elif num_dos > num_tre:
    print(nom + " el número  mayor es: ", num_dos)
elif num_dos < num_tre:
    print(nom + " el número  mayor es: ", num_tre)
elif num_tre > num_uno:
    print(nom + " el número mayor es: ", num_tre)
elif num_tre < num_uno:
    print(nom + " el número mayor es: ", num_uno)
elif num_tre > num_dos:
    print(nom + " el número mayor es: ", num_tre)
elif num_tre < num_dos:
    print(nom + " el número mayor es: ", num_dos)
else:
    print(nom + " los números son iguales: ")
