#que es un bit ? binary digit = digito binario
#Que es un binario ? dos componentes que son el 0, 1
"""
128  64  32  16  8  4  2  1

                    1  0  1  
                    
                    1  1  1 

                    0  1  0    
                 1  1  1  1

                 1  1  0  1
"""

a = 0b101
b = 0b111
c= 0b1111
print (a)

"""""
Operadores a Nivel de Bits (Bitwise)Operan directamente con la representación binaria de los enteros.
NOT: ~      nos da el opuesto -1
AND: &      multiplicacion de binarios
OR: |       suma de binarios
XOR: ^      suma binaria
Desplazamiento a la izquierda: <<
Desplazamiento a la derecha: >>
"""
"""
en suma binaria los bits iguales operados dan como resultado 0 y los diferentes dan como resultado 1
"""
#Operadores a nivel de bits
print(~ a)
print(a & b)
print(bin(a & b))
print(a | b |c)
print(bin(a | b| c))
print(a ^ b ^ c )
print(bin(a ^ b ^ c))

#DESPLAZAMIENTO DE BITS

print(a<<1)
print(a>>1)