# coding : utf - 8

#definição de constante
pi = 3.14159

# codigo

lado1, lado2, lado3 = (input().split())
lado1, lado2, lado3 = [float(lado1), float(lado2), float(lado3)]

areatriangulo  = (lado1*lado3)/2.0
areacirculo = pi*(lado3 ** 2)
areatrapezio = (lado3*(lado1 + lado2))/2.0
areaquadrado = lado2**2
arearet = lado1 * lado2

print("TRIANGULO: %.3f" %areatriangulo)
print("CIRCULO: %.3f" %areacirculo)
print("TRAPEZIO: %.3f" %areatrapezio)
print("QUADRADO: %.3f" %areaquadrado)
print("RETANGULO: %.3f" %arearet)