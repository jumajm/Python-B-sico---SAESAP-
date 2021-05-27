print ("-----")
print ("Ejercicio 1")
h = int(input("Escriba la altura del triangulo(debes ser un numero entero positivo) "))
for i in range(h):
    for j in range(i+1):
            print ("*", end="")
    print("")



print ("-----")
print ("Ejercicio 2")

o = int(input("Ingrese un numero entero positivo"))

while o>0:
    print(o)
    o-=1



print ("-----")
print ("Ejercicio 3")

n = int(input("Escriba un numero entero"))
if n<1:
    print("los numeros negativos no pueden ser primos")
if n==0:
    print("escriba un numero entero positivo")
if n==1:
    print("1 es un numero primo")
i=2
while n%i !=0:
    i+=1
if i == n:
    print(str(n)," es primo")
else:
    print(str(n), " no es primo")