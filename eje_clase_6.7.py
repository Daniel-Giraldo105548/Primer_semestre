# 6 
# Lista aleatoria
print("Lista \n")
import random
lista=[]  
num=()
print("Ingrese cuantos números aleatorios desea obtener")
n=int(input())
lista=[random.randint(0,10)for _ in range(n)]
print(lista)

# lista ordenada

print("\nOrdenar la lista de menor a mayor \n")

lista.sort()
print("La lista ordenada de menor a mayor es:", lista)

# lista repetida

print("\nLista repetida\n")

repeticiones = [lista.count(elemento) for elemento in set(lista)]
print(repeticiones)

# 7
# Gestor de notas 

nomEstu=input("¿Cúal es tu nombre (Estudiantes UM): ")
Edad=int(input("¿Cúal es tu edad?: "))
notaFin=float(input(nomEstu + " ¿Cúal fue tu  nota final?: "))
inasis=int(input(nomEstu + " ¿Cúantas inasistencias tuviste?: "))

if notaFin < 3.0:
    print("Pierde")
elif inasis > 12:
    print("pierde por inasistencias")
elif notaFin < 3.0 and inasis > 12:
    print("Cambie de carrera")
