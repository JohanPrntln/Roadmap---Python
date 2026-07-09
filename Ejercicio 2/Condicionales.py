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

# año=int(input("Ingresa un año: "))

# # 1900 ÷ 4 = 475 no es bisiesto
# # 2024 ÷ 4 = 506  es bisiesto 


# #if(año % 4 == 0 ):

# match año % 4:
#     case 0 :
#         if año % 100 == 0 : 
#             if año % 400 == 0 :
#                 print("Es bisiesto") 
#             else:
#                 print("No es bisiesto")
#     case _ :
#         print("No es bisiesto")





        


# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miércoles")
#     case _:
#         print("Día no válido")

# Ejercicio 3 - Calculadora de impuestos

# Pide el salario.

# Si gana

# 0 - 2.000.000        -> 0%
# 2.000.001 - 4.000.000 -> 10%
# 4.000.001 - 8.000.000 -> 20%
# Más de 8.000.000      -> 30%

# Debes mostrar

# Impuesto
# Salario neto

# salario=int(input("Ingrese su salario: "))

# match salario:
#     case salario if 0 <= salario <= 2000000:
#         print(f"Salario neto: {salario} \n Impuesto aplicado 0%")
#     case salario if 2000001 <= salario <= 4000000:
#         impuesto = 0.10 * salario
#         salarioNeto = salario - impuesto
#         print(f"Salario neto : {salarioNeto} \n Impuesto aplicado del 10%")
#     case salario if 4000001 <= salario <= 8000000:
#         impuesto = 0.20 * salario 
#         salarioNeto = salario - impuesto
#         print(f"Salario neto : {salarioNeto} \n Impuesto aplicado del 20%")
#     case salario if salario >= 8000000:
#         impuesto = 0.30 * salario 
#         salarioNeto = salario - impuesto
#         print(f"Salario neto : {salarioNeto} \n Impuesto aplicado del 30%")

# Ejercicio 4 - Login

# Hay un usuario y contraseña correctos.

# usuario = "admin"
# password = "1234"

# Pide ambos.

# Debes validar:

# usuario correcto y contraseña correcta
# usuario correcto pero contraseña incorrecta
# usuario inexistente

# usuarioExistente = "admin"
# passwordExistente = "1234"

# usuario = input("Ingrese su usario: ")
# password = input("Ingrese su contraseña: ")

# if (usuario == usuarioExistente) & (password == passwordExistente):
#     print(f"usuario correcto y contraseña correcta \n \n HOLAA ")
    
# elif (usuario == usuarioExistente) & (password != passwordExistente):
#     print("usuario correcto pero contraseña incorrecta")
# elif (usuario != usuarioExistente) & (password != passwordExistente):
#     print("usuario inexistente")



# Ejercicio 8 - Validación de contraseña

# Debe cumplir:

# mínimo 8 caracteres
# una mayúscula
# una minúscula
# un número

# Mostrar exactamente qué regla incumple.

# Ejemplo

# Le falta un número

# o

# Contraseña válida

# # Las regex (o expresiones regulares) son secuencias de caracteres que forman un patrón de búsqueda. Se utilizan principalmente para encontrar, validar, extraer o reemplazar texto dentro de cadenas de datos de manera rápida y eficiente
# import re
# mayuscula = r"[A-Z]+"
# minuscula = r"[a-z]+"
# numero = r"[0-9]+"
# password = input("Ingrese contraseña: ")


# if password.__len__() < 8 :
#     print(" tu contraseña debe tener mínimo 8 caracteres")
# else:
#     print("tu contraseña tiene 8 caracteres")
# if re.search(mayuscula, password):
#     print("Si contiene una Mayuscula")
# else:
#     print("No contiene mayuscula")
# if re.search(minuscula, password):
#     print("Si contiene minuscula")
# else:
#     print("No contiene minuscula")
# if re.search(numero, password):
#     print("Si contiene número")
# else: 
#     print("No contiene número")



# Ejercicio 20 - El "jefe" de condicionales

# Construye un sistema de admisión para una universidad.

# Pide:

# Edad
# Puntaje del examen
# Promedio del colegio
# Tiene beca (S/N)

# Reglas:

# Si es menor de 16 años → Rechazado.
# Si el puntaje es menor de 250 → Rechazado.
# Si el promedio es menor de 3.5 → Rechazado, excepto si tiene beca.
# Si el puntaje es mayor o igual a 400 y el promedio es mayor o igual a 4.5 → Admitido con honores.
# Si cumple los requisitos mínimos → Admitido.

# Este ejercicio requiere combinar varias condiciones, usar if, elif, else de forma organizada y validar el orden de las reglas.
# print("SISTEMA DE ADMINSION PARA LA UNIVERSIDAD")

# Edad=int(input("Ingrese su edad: "))


# if(Edad > 16):
#     puntex=int(input("Ingrese el puntaje del examen: "))
#     print("Cumple con la Edad")

#     if(puntex >= 250):
#         print("Cumple con el puntaje")
#         prom=float(input("Ingresa tu promedio del colegio: "))

#         if(prom >=4.5 and puntex >= 400):

#             print("Felicidades admitido con honores")
        
#         elif(prom >= 3.5):
            
#             print("Cumple con el promedio")
#         else:
            
#              beca=input("Tiene beca?: S / N : ")
             
#              if (prom < 3.5 and beca == "S"):
                 
#                print("Admitido por beca")
               
#              else:
                 
#                  print(" no fue admitido")
            
            
#     else:
#         print("No cumples con el puntaje minimo")
    
    
    

# else:
#     print("Rechazado, eres menor de 16 años")
