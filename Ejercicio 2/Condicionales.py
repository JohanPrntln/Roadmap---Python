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

# num=int(input("Ingresa un número: "))

# if(num>=20 and num<=50):
#     print("Esta el rango")
# else:
#     print("No esta en el rango")


# GRADUADO DE CONDICIONALES BASICAS QUE CHIMBA HUEVON 


# 6. Mayor de tres números

# num1=int(input("Ingrese primer número "))
# num2=int(input("Ingrese segundo número "))
# num3=int(input("Ingrese tercero número "))

# if(num1>num2 and num1>num3):
#     print(f"El primer número : ({num1}) es mayor")
# elif(num2>num1 and num2>num3):
#     print(f"El segundo número : ({num2}) es mayor")
# else:
#      print(f"El tercer número : ({num3}) es mayor")

# Ejercicio 1 - Clasificación de triángulos

# Pide al usuario tres lados.

# Determina:

# Si no forman un triángulo.
# Si es equilátero.   Todos los lados son iguales
# Si es isósceles.    Dos de sus lados son iguales
# Si es escaleno.     Todos los lados son diferentes

# Recuerda la condición:
# a + b > c
# a + c > b
# b + c > a

# a = int(input("Ingresa el primer lado del triangulo: "))
# b = int(input("Ingresa el segundo lado del triangulo: "))
# c = int(input("Ingresa el tercer lado del triangulo: "))

# operacion1 = a+b
# operacion2 = a+c
# operacion3 = b+c

# if(operacion1 > c and operacion2 > b and operacion3>a):
#     print("si joven tenemos un triangulo")
#     if(a == b and b == c and c==a ):
#         print("tenemos un triangulo equilátero")
#     elif( a == b and a != c ) ^ ( a == c and a != b ) ^ (b == c and b != a):
#         print("Tenemos un triangulo Isósceles")
#     else:
#         print("Tenemos un triagulo escaleno")
# else:
#     print("Disculpa no es un triangulo")
    

# Ejercicio 2 - Año bisiesto

# Pide un año.

# Un año es bisiesto si:

# es divisible entre 4
# excepto si es divisible entre 100
# a menos que también sea divisible entre 400

# significa que al dividir el primero entre el segundo, el resultado es una división exacta
# Por ejemplo:\(20\) es divisible por \(4\), porque al dividir \(20 \div 4\), el resultado es \(5\) y el residuo es \(0\).

# Ejemplos

# 2000 -> Bisiesto
# 1900 -> No
# 2024 -> Sí
# 2025 -> No

año=int(input("Ingresa un año: "))

# 1900 ÷ 4 = 475 no es bisiesto
# 2024 ÷ 4 = 506  es bisiesto 
prueba=2024%400
print(prueba)

#if(año % 4 == 0 ):

match año % 4:
    case 0 :
        if año % 100 : 
    case _ :





        


# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miércoles")
#     case _:
#         print("Día no válido")