##Programado por: Daniel Giraldo
##Fecha: 17/03/2023
##Version: 1.0
##Programa que calcula la nota de un estudiante de la UD

##Titulo
print("**********************")
print("Calculador de notas UD")
print("********************** \n")

##Entrada de datos
NomEst = input("Digite el nombre del estudiante: ")
Codi = int(input("Digite el codigo del estudiante: "))
notUno = float(input("Digite la nota del parcial: "))
notDos = float(input("Digite la nota de la tarea: "))
notTres = float(input("Digite la nota de trabajo en clase: "))
notCuatro = float(input("Digite la nota del comportamineto en clase: "))

##Procesos y salida 
nota = notUno * 0.3 + notDos * 0.35 + notTres * 0.2 + notCuatro * 0.15 

if nota == 3.0:
    print("PASA")
    print("El estudiante",NomEst,"con el codigo",Codi,"pasa con una nota de",nota)
    print("PASAS")
elif nota < 3.0:
    print("NO PASA")
    print("El estudiante",NomEst,"con el codigo",Codi,"No pasa con una nota de",nota)
    print("RECUPERAR")
else:
    print("La nota del estudiante", NomEst, "es de",nota)

##Recordatorio
print("La nota minima para pasar es de 3.0.")
