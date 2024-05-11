#Semana 1
numero1 = int (input("Ingrese el primer numero: ")) 
numero2 = int (input("Ingrese el segundo numero: ")) 
numero3 = int (input("Ingrese el tercer numero: ")) 

if numero1 >= numero2 and numero1 >=numero3:
    print("El numero mayor es el: ",numero1)
elif numero2 >= numero1 and numero2 >=numero3:
    print("El numero mayor es el: ",numero2)
elif numero3 >= numero1 and numero3 >=numero2:
    print("El numero mayor es el: ",numero3)
    
