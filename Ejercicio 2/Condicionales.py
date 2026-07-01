# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales,

# Que es una condicional ? 
"""
 Son instrucciones lógicas que permiten a un programa tomar decisiones (ej. «Si la contraseña es correcta, dar acceso; si no, mostrar error»)
"""
#Que tipos de condicionales existen en python ?
"""
condicionales simples, anidadas

"""
#if simple
# edad = 20

# if edad >= 18:
#     print("Eres mayor de edad")

#if simple per un poco mas avanzado 
# edad = 16

# if edad >= 18:
#     print("Mayor de edad")
# else:
#     print("Menor de edad")

#if bloque

# nota = 4.2

# if nota >= 4.5:
#     print("Excelente")
# elif nota >= 3.5:
#     print("Aprobó")
# elif nota >= 3.0:
#     print("Recuperación")
# else:
#     print("Reprobó")

#if anidados

# edad = 25
# tiene_licencia = True

# if edad >= 18:
#     if tiene_licencia:
#         print("Puede conducir")
#     else:
#         print("Necesita licencia")
# else:
#     print("Es menor de edad")

#condicionales de solo una linea (operador ternario)

# edad = 20

# mensaje = "Mayor" if edad >= 18 else "Menor"

#condicionales con operadores de expresiones logicas 
# edad = 22
# tiene_documento = True

# if edad >= 18 and tiene_documento:
#     print("Puede ingresar")

# if edad < 18 or not tiene_documento:
#     print("No puede ingresar")


#Comparacion encadenada

# x = 7

# if 1 <= x <= 10:
#     print("Está entre 1 y 10")

# if x >= 1 and x <= 10:
#     print("Está entre 1 y 10")

# #match case 

# dia = 3

# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miércoles")
#     case _:
#         print("Día no válido")




#1. Mayor de dos números
#Pide dos números e imprime cuál es mayor.


# n1 = int(input("ingresa el primer numero "))
# n2 = int(input("ingresa el segundo número "))


# if(n1 > n2):
#     print(f"El primer número : {n1} es mayor")
# else:
#     print(f"El segundo número: {n2} es mayor")



# 2. escribe un programa donde ingreses un Número y detecte si es positivo, negativo o cero
# Entrada:
# -8
# Salida:
# Negativo

# num=int(input("Ingresa un número positivo o negativo "))

# if(num > 0):
#     print("Es mayor a cero por ende es positivo")
# elif(num < 0):
#     print("El numero es negativo")
# else:
#     print("Es cero")

    
# 3. escribe un programa donde ingreses un Número y detecte si es Par o impar

# num1=int(input("Ingresa un número para verificar si es par o impar "))

# if(num1 % 2 == 0):
#     print("El número es par")
# elif(num1 % 2 !=0):
#     print("El número es impar")


# 4. Mayor de edad

# Si tiene 18 años o más puede entrar.

# edad=int(input("Ingrese su edad: "))

# if(edad >=18):
#     print("Puedes entrar")
# else:
#     print("No puedes entrar")

# 5. Número dentro de un rango

# Determina si un número está entre 20 y 50.

num=int(input("Ingresa un número: "))

if(num>=20 and num<=50):
    print("Esta el rango")
else:
    print("No esta en el rango")


# GRADUADO DE CONDICIONALES BASICAS QUE CHIMBA HUEVON 