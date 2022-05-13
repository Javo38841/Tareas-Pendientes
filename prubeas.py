b=False
a=False
puntos=0
if len(primera_palabra)>=3:
    if primera_palabra in universo:
        puntos=10*len(primera_palabra)+5*vocales(primera_palabra)+3*consonantes(primera_palabra)
        a=True
else:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    print("Fin del intento, obtuviste un total de 0 puntos")
puntos1=0
if len(segunda_palabra)>=3 and a==True:
    if segunda_palabra in universo:
        puntos1=10*len(segunda_palabra)+5*vocales(segunda_palabra)+3*consonantes(segunda_palabra)
        b=True
else:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    print("Fin del intento, obtuviste un total de 0 puntos")
puntos2=0
if len(tercera_palabra)>=3 and b==True:
    if tercera_palabra in universo:
        puntos2=10*len(tercera_palabra)+5*vocales(tercera_palabra)+3*consonantes(tercera_palabra)
    print("Fin del intento, obtuviste un total de",(puntos+puntos1+puntos2))
else:
    print("Error, las palabras deben tener al menos 3 letras, perdió su intento")
    print("Fin del intento, obtuviste un total de 0 puntos")
