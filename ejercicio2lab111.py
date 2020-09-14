from math import sqrt                               

a=int(input("ingrese el coeficiente del numero que acompaña a la variable al cuadrado:" ))
b=int(input("ingrese el coeficiente del numero que acompaña ala variable de grado uno:"))
c=int(input("ingrese el termino independiente"))
determinante=b**2-4*a*c                                 #nos aseguramos que la determinante sea mayor 
if determinante>0:                                      #si es mayor que cero entonces tendra 2 soluciones
    x_1=((-b+sqrt(b**2-4*a*c))/(2*a))
    x_2=((-b-sqrt(b**2-4*a*c))/(2*a))
    print("la primera solucion es:",x_1,"la segunda solucion es:",x_2)
elif determinante==0:                               #si la determinante es = a cero solo tendra 1 solucion
    x_1=-b/(2*a)
    print(x_1)
else:
    print("el numero es imaginario1")                       