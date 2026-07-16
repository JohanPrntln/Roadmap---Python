# #EStructuras iterativas
# # que son las estructuras iterativas ?
#     #son aquellas estructuras que nos permiten repetir instrucciones varias veces
# #Que necesitamos conoces para ser dominar este tema de las Estructuras iterativas

# # 1) Bucle while

# # Repite mientras una condición sea verdadera.
# contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1
# print("Salio del bucle")

# #-------------------------------------------------

# # 2) Bucle for
# #dentro del lenguaje de python tiene muchas adaptaciones segun nuestras necesidades
# # pero la mayoria de veces lo vamos a utilizar para rrecorrer una estructura de datos o en su defecto rrecorrer una secuencia de algod

# # Recorre elementos de una secuencia.
# for numero in [1, 2, 3, 4, 5]:
#     print(numero)


# # Genera secuencias numéricas.
# for i in range(100):
#     print(i)
# for i in range(3,20):
#     print(i)
#             #  i  f   p     paso = 2      1+2  =3  3+2 = 5 5+2 =7 7+2 = 9      
# for i in range(0, 10, 2):
#     print(i)


# # Recorrer cadenas
# nombre = "Python"

# for letra in nombre:
#     print(letra)

# # Recorrer listas

# frutas = ["manzana", "pera", "uva"]

# for fruta in frutas:
#     print(fruta)

# # Recorrer tuplas
# coordenadas = (10, 20)

# for valor in coordenadas:
#     print(valor)

# # Recorrer conjuntos (set)

# numeros = {1, 2, 3, 4}

# for numero in numeros:
#     print(numero)

# # Recorrer diccionarios

# persona = {
#     "nombre": "Juan",
#     "edad": 25,
#     "fecha" : "25/07/89"
# }

# for clave in persona:
#     print(clave)

# for valor in persona.values():
#     print(valor)

# for clave, valor in persona.items():
#     print(clave, valor)


# # break
# # Rompe el ciclo inmediatamente.

# for i in range(10):
#     if i == 5:
#         break

#     print(i)

# #Continue
# #salta una iteracion 
# for i in range(10):
#     if i == 3 or i ==7:
#         continue

#     print(i)

# #pass
# for i in range(5):
#     pass

# #else en ciclos 
# for i in range(5):
#     print(i)
# else:
#     print("Fin")

# #bucle for con un else pero dentro del bucle for hay un break

# for i in range(5):
#     if i == 3:
#         break
# else:
#     print("Nunca aparece")


# #ciclos anidados 

# for fila in range(3):
#     for columna in range(3):
#         print(fila, columna)

# #Enumerar elementos (enumerate)
# # Obtiene índice y valor.

# frutas = ["pera", "uva", "mango"]

# for indice, fruta in enumerate(frutas):
#     print(indice, fruta)


# #Iterar multiples secuencias (zip)

# nombres = ["Ana", "Luis", "Pedro"]
# edades = [20, 25, 30]

# for nombre, edad in zip(nombres, edades):
#     print(nombre, edad)

# # Comprensión de listas

# # Forma compacta de iterar.

# cuadrados = [x ** 2 for x in range(10)]

# print(cuadrados)


# # Comprensión con condición

# pares = [x for x in range(20)  if x % 2 == 0]

# print(pares[9])

# # Comprensión de conjuntos

# cuadrados = {x ** 2 for x in range(10)}

# # Comprensión de diccionarios

# dic = {x: x ** 2 for x in range(5)}


# # Iteradores
# # Un objeto iterable puede convertirse en iterador.
# numeros = [1, 2, 3]

# it = iter(numeros)

# print(next(it))
# print(next(it))
# print(next(it))

# # Generadores (yield)
# # Permiten producir valores bajo demanda.
# def contador():
#     n = 1

#     while True:
#         yield n
#         n += 1

# gen = contador()

# print(next(gen))
# print(next(gen))
# print(next(gen))


# # Expresiones generadoras
# cuadrados = (x ** 2 for x in range(10))

# for numero in cuadrados:
#     print(numero)


# # Funciones útiles para iterar

# len([1, 2, 3])

# sum([1, 2, 3])

# max([5, 10, 20])

# min([5, 10, 20])

# any([False, False, True])

# all([True, True, True])


# # Patrones clásicos de iterativas

# # Contador

# contador = 0

# for i in range(10):
#     contador += 1

# # Acumulador

# suma = 0

# for i in range(1, 6):
#     suma += i

# # Máximo

# numeros = [8, 3, 15, 2]

# mayor = numeros[0]

# for numero in numeros:
#     if numero > mayor:
#         mayor = numero

# # Mínimo

# numeros = [8, 3, 15, 2]

# menor = numeros[0]

# for numero in numeros:
#     if numero < menor:
#         menor = numero


# # Búsqueda

# objetivo = 15

# for numero in numeros:
#     if numero == objetivo:
#         print("Encontrado")
#         break


#---------Desarrollo-------------
# 1 Bucle while 
# el bucle while evalua una condicion y segun su resultado itera x instruccion

# Ejercicio 1: Contar del 1 al 10

# Muestra los números del 1 al 10 utilizando un bucle while.

# contador = 0

# while contador < 10 :
#     contador += 1 
#     print(contador)


# Ejercicio 2: Contar del 10 al 1

# Muestra los números del 10 al 1 en orden descendente.

# cont= 10

# while cont > 1 :
#     cont -= 1
#     print(cont)

# Ejercicio 3: Mostrar números pares

# Muestra todos los números pares entre 1 y 20.

# cont = 0

# while cont <= 20:
#     if cont % 2 == 0:
#         print(cont)
#     cont += 1


# Ejercicio 4: Mostrar números impares

# Muestra todos los números impares entre 1 y 20.

# cont = 0

# while cont <= 20:
#     if cont % 2 != 0:
#         print(cont)
#     cont +=1
    


# # Ejercicio 5: Tabla del 5

# # Muestra la tabla de multiplicar del 5 utilizando un while.

# # Ejemplo:

# # 5 x 1 = 5

# # 5 x 2 = 10

# # ...

# # 5 x 10 = 50

# cont = 0

# while cont <= 10: 
    
#     print(f"5 x {cont}: {5*cont} ")
#     cont+=1

# Nivel 2 - Acumuladores
# Ejercicio 6: Suma de números

# Solicita un número N y calcula la suma de los números desde 1 hasta N.

# Ejemplo:

# N = 5

# Resultado = 1 + 2 + 3 + 4 + 5 = 15

# cont = 0
# num = int(input("Ingrese un número: "))
# suma = 0

# while cont <= num:
#     suma = cont + suma
#     print(f"Resultado  ")   
#     cont+=1


# # cont = 0
# # num = int(input("Ingrese un número: "))
# # suma = 0
# # imprimir = ""

# # while cont <= num:
# #     suma = cont + suma
# #     imprimir += str(cont)
# #     if cont == num:
# #         break

# #     imprimir += " + "   
# #     cont+=1
# # print(imprimir + f" = {suma}")



# Ejercicio 7: Suma de números pares

# # Calcula la suma de todos los números pares entre 1 y 100.

# cont = 0
# acum = 0
# num = 100

# while cont <= num:
#     if(cont % 2 == 0):
#         acum = cont + acum
#         print(acum)
#     cont+=1

# # Ejercicio 8: Producto de números

# # Solicita un número N y calcula el producto de los números desde 1 hasta N.

# # Ejemplo:

# # N = 5

# # Resultado = 1 × 2 × 3 × 4 × 5 = 120

# # num = int(input("Ingrese un número: "))
# # cont = 1
# # acum = 1

# # while cont <= num:
# #     acum = cont * acum
# #     cont += 1
# #     print(acum)

# # Ejercicio 9: Promedio de notas

# # Solicita 5 notas y calcula el promedio.

# cont = 0

# acum = 0
# while cont < 5:
#     cont+=1

#     nota = float(input(f"Ingrese nota {cont}: "))

#     acum = nota + acum


# promedio = acum / cont
# print(f"El promedio de sus notas es : {promedio}")
   
   

# Ejercicio 13: Edad válida

# Pide una edad y no permitas valores menores que 0 o mayores que 120, si ingresa una edad invalida no permitas que salga del bluce


# a = True

# while a: 
#     edad = int(input("Ingrese edad: "))
#     if (0 < edad < 120):
#         print("Acceso aprobado")
#         a = False
#     else:
#         print("Acceso denegado")

 

    
# Nivel 4 - Patrones
# Ejercicio 16: Dibujar línea

# # Solicita un número N y muestra N asteriscos.

# num = int(input("Ingrese un número: "))
# cont = 0
# string = ""

# while cont < num:
#     cont+=1
#     string+="*"
# print(f"El número de asteriscos dibujados son {num} y se ve asi : {string}")




# Ejercicio 17: Triángulo rectángulo

# Solicita un número N. 4

#*
#**
#***
# #****

# num = int(input("Ingrese un número para dibujar el triángulo rectángulo: "))
# cont = 0
# string = ""

# while cont < num:
#     cont += 1
#     conta2 = 0

#     while conta2 < cont:      
#             conta2 +=1
#             string += "*"

#     string += "\n"

# print(string)
   

# Ejercicio 18: Triángulo rectangulo invertido

# Ejemplo para N = 5:

num = int(input("Ingrese un número para dibujar el triángulo rectángulo invertido: "))
cont = 0
string = ""

while cont < num:
    string += "*" *num
    string += "\n"
    num -=1

print(string)