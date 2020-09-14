tiempox=int(input("ingrese el tiempo en segundos"))
tareazhh=int(input("ingresa el tiempo que tomara realizar la tarea en horas"))
tareazmm=int(input("ingresa el tiempo que tomara realizar la tarea en minutos"))
tareazss=int(input("ingresa el tiempo que tomara realizar la tarea en segundos"))
tareazmm=(tareazmm*60)
tareazhh=(tareazhh*3600)
tareaz=(tareazhh+tareazmm+tareazss)
if tiempox>=tareaz:
    print("see podra realizar la tareaz")
else:
    print("no se podra realizar la tarea")
