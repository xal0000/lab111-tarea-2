hh=int(input("ingrese la hora:  "))
mm=int(input("ingrese los minutos:  "))
ss=int(input("ingrese los segundos:  "))
if hh<24:
    if mm<59:
        if ss<59:
            ss=ss+1
            print(hh,":",mm,":",ss)
        else:
            ss==59
            ss=00
            mm=mm+1
            print(hh,":",mm,":",ss)
            if mm==59:
                hh=hh+1
                mm=00
                print(hh,":",mm,":",ss)
                if hh==23:
                    hh==00
                    print(hh,":",mm,":",ss)
                else:
                    print(hh,":",mm,":",ss)                         
            else:
                ss=00
                print(hh,":",mm,":",ss)        

    else:
        if ss==59:
            ss=00
            mm=00
            hh=hh+1
            print(hh,":",mm,":",ss)
           
    
        else:
            ss=ss+1
            print(hh,":",mm,":",ss)
else:
    print("introdusca una hora")
   
