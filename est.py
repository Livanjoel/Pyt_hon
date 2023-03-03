
num1 = int(input("Ingrese el primer numero: ")) #recibe un valor de la consola
num2 = int(input("Ingrese el segundo numero: ")) #input() recibe un valor de la consola  

print("******EJEMPLO IF*******")
if num1 > num2: #si num1 es mayor que num2
    print(num1, "es mayor que", num2) #imprime num1 es mayor que num2
elif num1 == num2: #si no y num1 es igual a num2
    print(num1, "es igual que", num2) #imprime num1 es igual que num2
else: #si no
    print(num2, "es mayor que", num1) #imprime num2 es mayor que num1  

def evaluacion(nota): #definicion de la funcion evaluacion
    valoracion = "aprobado" #valoracion es igual a aprobado
    if nota < 5: #si nota es menor que 5
        valoracion = "suspenso" #valoracion es igual a suspenso
    return valoracion
print(evaluacion(int(input("Ingrese la nota: ")))) #llama a la funcion evaluacion y le pasa el valor de la consola   

print("*********EJEMPLO ELSE*********")
edad = int(input("Ingrese su edad: ")) #recibe un valor de la consola

if edad >= 18: #si edad es mayor o igual a 18
    print("Es mayor de edad") #imprime es mayor de edad
else: #si no    
    print("Es menor de edad") #imprime es menor de edad