from random import randint



print("bienvenido a PysCrable")

def generar_universo(size):
    if size >=10 and size <=35:
        consonantes=round(size*0.6)
        vocales=round(size*0.4)
        stringsconsonantes="bcdfghjklmnpqrstvwxyz"
        stringsvocales="aeiou"
        c=0
        v=0
        universo=""
        proposicion=False
        while proposicion== False:
            letra=randint(1,2)
            if c < consonantes and letra==1:
                universo=universo+stringsconsonantes[randint(0,20)]
                c=c+1
            if v < vocales and letra==2:
                universo=universo+stringsvocales[randint(0,4)]
                v=v+1
            if c==consonantes and v== vocales:
                proposicion= True
    else:
        universo=""
    return(universo)

def vocales(palabra):
    v=0
    stringsvocales="aeiou"
    for recorrido in palabra:
        if recorrido in stringsvocales:
            v=v+1
    return(v)

def consonantes(palabra):
    c=0
    stringsconsonantes="bcdfghjklmnpqrstvwxyz"
    for recorrido in palabra:
        if recorrido in stringsconsonantes:
            c=c+1
    return(c)

def contiene(palabra,universo):
    c=0
    for caracter in palabra:
        if caracter in universo:
            c=c+1
    if c==len(palabra):
        condicion=1
    else:
        condicion=2
    return condicion

universo=""
while universo == "":
    size=int(input("ingrese tamaño del universo de letras "))
    universo=generar_universo(size)

print("Universo: ",universo)
palabras= input("ingrese sus 3 palabras separadas por un guión: ")

i=0
while i<len(palabras) and palabras[i]!="-":
    i=i+1
primera_palabra=palabras[:i]
i2=i+1
while i2<len(palabras) and palabras[i2]!="-":
    i2=i2+1
segunda_palabra=palabras[i+1:i2]
i3=i2+1
while i3<len(palabras) and palabras[i3]!="-":
    i3=i3+1
tercera_palabra=palabras[i2+1:i3]

turno=1
puntos=0
acumular=0
proposicion=False
while proposicion!=True:
    if turno==1:
        verdad1= contiene(primera_palabra,universo)
        verdad2= contiene(segunda_palabra,universo)
        verdad3= contiene(tercera_palabra,universo)
        if len(primera_palabra)>=3:
            if verdad1==1:
                puntos=10*len(primera_palabra)+5*vocales(primera_palabra)+3*consonantes(primera_palabra)
                acumular=puntos+acumular
                print(primera_palabra,"se puede generar con",universo)
                print("obtienes",puntos)
                proposicion=False
            else:
                print("Error,no hay las suficientes palabras para generar la palabra, perdió su intento")
                acumular=0
                proposicion=True
        else:
            print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
            acumular=0
            proposicion=True    
    if turno==2:
        if len(segunda_palabra)>=3:
            if verdad2==1:
                puntos=10*len(segunda_palabra)+5*vocales(segunda_palabra)+3*consonantes(segunda_palabra)
                acumular=puntos+acumular
                print(segunda_palabra,"se puede generar con",universo)
                print("obtienes",puntos)
                proposicion=False
            else:
                print("Error,no hay las suficientes palabras para generar la palabra, perdió su intento")
                acumular=0
                proposicion=True
        else:
            print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
            acumular=0
            proposicion=True
    if turno==3:
        if len(tercera_palabra)>=3:
                if verdad3==1:
                    puntos=10*len(tercera_palabra)+5*vocales(tercera_palabra)+3*consonantes(tercera_palabra)
                    acumular=puntos+acumular
                    print(tercera_palabra,"se puede generar con",universo)
                    print("obtienes",puntos)
                    proposicion=True
                else:
                    print("Error,no hay las suficientes palabras para generar la palabra, perdió su intento")
                    acumular=0
                    roposicion=True
        else:
            print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
            acumular=0
            proposicion=True
    turno=turno+1

print("Fin del intento, obtuviste un total de",acumular,"puntos")

