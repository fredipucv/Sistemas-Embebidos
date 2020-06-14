

valor1 = int(input("Ingresa el primer valor: "))
valor2 = int(input("Ingresa el segundo valor: "))

if valor2 == pow(valor1,2):
    print("el segundo valor es el cuadrado exacto del primero")
else:
    print("el segundo valor no es el cuadrado exacto del primero")
    
if valor2 < pow(valor1,2):
    print("el segundo valor es menor que el cuadrado del primero")   
else: 
    print("el segundo valor es mayor que el cuadrado del primero")
    
