#25/06/2026
#
# EJERCICIO:

#  
#
# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#


# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

#Operadores Aritmeticos +, -, *, /, %, **, //

# 10/3 = 3.3333  el objetivo es tener el resultado completo 
# 10//3 = 3      el objetivo es eliminar la parte decimal del resulado
# 10%3 = 1       el modulo devuelve el residuo de la division

a = 8+9
b = 5-2
c = 9*10
d = 5/3
e = 100//10
f = 45%15
g = 5**2

#Operadores Logicos and - or - not
"""
Operadores LógicosCombinan múltiples condiciones para construir expresiones lógicas complejas
and: Devuelve True si ambas condiciones son verdaderas.
or: Devuelve True si al menos una condición es verdadera.
not: Invierte el valor booleano (ej. not True es False).
"""

#condicional simple
if(c==901 or f==0):
    print ("Se hizo real")

#condicionales anidadas
if(a ==17 and b==3): # se tienen que cumplir las dos condiciones para que nos de un true
    print("Hola a = 17 y b =3 misterio resuelto")
elif(a ==17):       
    print("el de arriba estaba equivocado")
elif(c==901 or f==0): 
    print("se hizo real")
else:
    print("ninguna de las anteriores condiciones son verdaderas")

print("fuera de las condicionales anidadas")

if(not a==17):
    print ("Esta bien, pero no")
    
if(not a==16):
    print("esto da verdadero")
    


# if (condicion) verdadero true o false false
#   #    logica   #
#   #             #
#   ###############  




# Operadores de comparacion o relacionales
"""
 Operadores de Comparación (o Relacionales)Comparan dos valores y siempre devuelven un resultado booleano (True o False).
 Igual a: == (ej. 5 == 5 es True)
 Diferente de: !=
 Mayor que: >
 Menor que: <
 Mayor o igual que: >=
 Menor o igual que: <=
"""

if(a<b):
    print("a es menor que b")
if(b<a):
    print("b es menor que a")
if(g<=a):
    print("g es menor a 17 o es 17")
if(a>=b):
    print ("ñññññ")
if (a==17):
    print ("Siuuu")
if (a!=b):
    print ("Stunt life")
    
# Operados de Identidad y Pertenencia
"""
Operadores de Identidad y Pertenencia

Verifican si dos variables apuntan al mismo objeto en memoria, o si un valor existe dentro de una secuencia.

Identidad: is y is not (ej. x is y)
Pertenencia: in y not in (ej. 'a' in 'manzana')
"""
c = [10,2,3] #efx00001
a = [1,2,3]  #efx00002
b = c        #efx00001


#string son arrays array con otro array
manzana = "manzana"
#0
i = ['M','a','n','z','a','n','a']
caracter_a = 'c'
p = ['a']

y = ['1','2','3','4','5']
z = ['6']

if (z[0] not in y):
    print ("Jose candela")


if(p[0] in i):
    print("sisas el caracter a se encuentra en el string manzana")

print(b[0])

if(a is b):
    print("los dos objetos apuntan al mismo objeto")
elif(a is not b):
    print("a no es b o son dos variables que apuntan a un lugar de la memoria diferente")
    
    
#Bits
#basicamente es otra forma de escribir los operadores logicos pero con mayor simplicidad
"""""
Operadores a Nivel de Bits (Bitwise)Operan directamente con la representación binaria de los enteros.
AND: &
OR: |
XOR: ^
NOT: ~
Desplazamiento a la izquierda: <<
Desplazamiento a la derecha: >>
"""
# Asegúrate de que las variables tengan valores asignados antes del if
a = 5
b = 10
c = 3
f = 8

if (a < b) & (f > c):
    print("a es menor que b y f es mayor que c")
    
if (a==17 | b==4):
    print("a es True y b es False ya que el | es equivalente a OR ")

if (5<b or c>2):
    print("las dos condicionales dieron verdadero")
if (5<b) ^ (c>2):
    print("parce pues las dos dieron positivo por ende esto da negativo solo puede pasar una")

#para que sirven el dezplasamiento de bits
#Desplazamiento de bits izquierda para multiplicar, derecha para dividir. Estan 1=2. 0 = neutro
 
print(13<<1)

#(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
#   Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.

#vamos hacer un ejemplo utilzando condicionales, todos los tipos de condicionales que nos permite el lenguaje de programacion python

