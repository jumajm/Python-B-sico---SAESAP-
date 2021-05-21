PESO = input ("Ingrese peso en kilogramos ")
ALTURA = input ("Ingrese su altura en metros ")

IMC = (float(PESO)/float(ALTURA)**2)
IMC = round(IMC,2)

print ("Su IMC es:",IMC)