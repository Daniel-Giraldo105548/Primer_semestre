##AREA DE DESCRIPCIÓN 
##PROGRAMADO POR: Daniel Giraldo Giraldo
##FECHA: 11/03/2023
##ESTE PROGRAMA: Calcula el salario de un empleado mensual  en base a las horas trabajas a la semana 

print("***********************************************************************************")
print("Calcular el salario mensual de un empleado en base a las horas trabajas a la semana")
print("*********************************************************************************** \n")

##AREA DE ENTRADA DE DATOS
nom = input("Introduce tu nombre: ")
horTra = int(input( nom + " introduce las horas trabajaste a la semana: "))
valHor = float(input( nom + " introduce el valor de las horas trabajadas a la semana: "))

##AREA DE PROCESOS
if horTra > 40:
   sueldo = horTra * 1.5 * valHor * 4 
   print(nom + " el sueldo de este mes es de: ", sueldo)
    
elif horTra:
    sueldo = horTra * valHor * 4
    print(nom + " el sueldo de este mes es de: ", sueldo)

else:
    print("Intenta de nuevo: ")

