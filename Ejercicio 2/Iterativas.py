#EStructuras iterativas
# que son las estructuras iterativas ?
    #son aquellas estructuras que nos permiten repetir instrucciones varias veces
#Que necesitamos conoces para ser dominar este tema de las Estructuras iterativas

# 1) Bucle while

# Repite mientras una condición sea verdadera.
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
print("Salio del bucle")

#-------------------------------------------------

# 2) Bucle for
#dentro del lenguaje de python tiene muchas adaptaciones segun nuestras necesidades
# pero la mayoria de veces lo vamos a utilizar para rrecorrer una estructura de datos o en su defecto rrecorrer una secuencia de algod

# Recorre elementos de una secuencia.
for numero in [1, 2, 3, 4, 5]:
    print(numero)


# Genera secuencias numéricas.
for i in range(100):
    print(i)
for i in range(3,20):
    print(i)
            #  i  f   p     paso = 2      1+2  =3  3+2 = 5 5+2 =7 7+2 = 9      
for i in range(0, 10, 2):
    print(i)


# Recorrer cadenas
nombre = "Python"

for letra in nombre:
    print(letra)

# Recorrer listas

frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)

# Recorrer tuplas
coordenadas = (10, 20)

for valor in coordenadas:
    print(valor)

# Recorrer conjuntos (set)

numeros = {1, 2, 3, 4}

for numero in numeros:
    print(numero)

# Recorrer diccionarios

persona = {
    "nombre": "Juan",
    "edad": 25,
    "fecha" : "25/07/89"
}

for clave in persona:
    print(clave)

for valor in persona.values():
    print(valor)

for clave, valor in persona.items():
    print(clave, valor)


# break
# Rompe el ciclo inmediatamente.

for i in range(10):
    if i == 5:
        break

    print(i)

#Continue
#salta una iteracion 
for i in range(10):
    if i == 3 or i ==7:
        continue

    print(i)

#pass
for i in range(5):
    pass

#else en ciclos 
for i in range(5):
    print(i)
else:
    print("Fin")

#bucle for con un else pero dentro del bucle for hay un break

for i in range(5):
    if i == 3:
        break
else:
    print("Nunca aparece")


#ciclos anidados 

for fila in range(3):
    for columna in range(3):
        print(fila, columna)

#Enumerar elementos (enumerate)
# Obtiene índice y valor.

frutas = ["pera", "uva", "mango"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)


#Iterar multiples secuencias (zip)

nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 25, 30]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

# Comprensión de listas

# Forma compacta de iterar.

cuadrados = [x ** 2 for x in range(10)]

print(cuadrados)


# Comprensión con condición

pares = [x for x in range(20)  if x % 2 == 0]

print(pares[9])

# Comprensión de conjuntos

cuadrados = {x ** 2 for x in range(10)}

# Comprensión de diccionarios