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

# 10/3 = 3.3333  el objetivo es tener el resultado completo el decimal
# 10//3 = 3      el objetivo es eliminar la parte decimal del resulado
# 10%3 = 1       el modulo devuelve el residuo de la division

a = 8+9
b = 5-2
c = 9*10
d = 5/3
e = 100//10
f = 45%15
g = 5**2

#Operadores Logicos and (y) - or (o) - not (no)
"""
Operadores LógicosCombinan múltiples condiciones para construir expresiones lógicas complejas
and: Devuelve True si ambas condiciones son verdaderas.
or: Devuelve True si al menos una condición es verdadera.
not: Invierte el valor booleano (ej. not True es False).
"""

#condicional simple
if(c==901 or f==0):
    print ("Se hizo real")

#condicionales en bloque
if(a ==17 and b==3): # se tienen que cumplir las dos condiciones para que nos de un true
    print("Hola a = 17 y b =3 misterio resuelto")
elif(a ==17):       
    print("el de arriba estaba equivocado")
elif(c==901 or f==0): 
    print("se hizo real")
else:
    print("ninguna de las anteriores condiciones son verdaderas")
#fin bloque de condiciones en bloque

print("fuera de las condicionales en bloque")

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

# is lo que valida es la posicion en la memoria va vb (va != vb) (va is not vb) = true b = c (b is not c) false (c is b) true
b.append(5)
for i in range(len(c)):
    print(c[i])

#padre / hija a, hijo b       hijo a is hijo b        false     porque estan en distintos lugares en la memoria
if(b is c) :
    print("b es igual a c")

y=[0,1,2,3]

z=[4]


if(z[0] in y):
    print("no es y")

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
    
    
d1=[5,7,1,6]
d2=d1
d3=[5] 
if(d2 is d1):
    print("d2 apunta a d1, porque comparten el mismo lugar en la memoria")  
    
if(d3 is not d2):
    print("d3 no es d2 porque, no comparten el mismo lugar de memoria")
    
d4=[2007,"febrero","8","Johan"]
d5="8"
d6=2008

if(d5 in d4):
    print("d5 es 8 y d4 contiene el 8 por lo tanto d5 esta en d4")
    
if(d6 not in d4):
    print("d6 no esta dentro de d4") 

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
if ( ~ a==5 ):
    print("nada")

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

