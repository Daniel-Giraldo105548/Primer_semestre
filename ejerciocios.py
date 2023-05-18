# Ejercicios que mando carlistos

# 1
lista=["Mat", "Física", "Química", "Historia", "Lenguaje"]
print(lista)

# 2 
lista=["Mat", "Física", "Química", "Historia", "Lenguaje"]
for lista in lista:
    print("Yo estudio " + lista)

# 3 
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

