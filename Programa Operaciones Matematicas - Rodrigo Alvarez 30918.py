from cmath import pi
import math

print ("Suma de dos numeros: ")
x = int(input("Numero uno: "))
y = int(input("Numero dos: "))
suma = x+y
print("La suma de los dos numeros es: ", suma)

print ("Resta de dos numeros: ")
x = int(input("Numero uno: "))
y = int(input("Numero dos: "))
resta = x-y
print("La resta de los dos numeros es: ",  resta)

print("Multiplicacion de dos numeros: ")
x = int(input("Numero uno: "))
y = int(input("Numero dos: "))
multiplicacion = x*y
print("La multiplicacion de los dos numeros: ", multiplicacion)


print("Division de dos numeros: ")
x = int(input("Numero uno: "))
y = int(input("Numero dos: "))
division = x/y 
print("La division de los dos numeros es: ", division)

print("Raíz cuadrada")
x = int(input("Numero a sacar raíz cuadrada: "))
raiz = math.sqrt(x)
print("La raíz cuadrada de ",x," es ",raiz)

print("Sacar el área de un círculo: ")
r = int(input("ingresa el radio del círculo: "))
areacirculo = r*r
areacirculo = areacirculo*math.pi
print("El área del círculo es: ",areacirculo)