#DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
#               : Ing. Córdova Julca, Guillermo Arturo
# PROGRAMA      : Formas de fondo - Simons y Richardson
# LENGUAJE      : Python
from math import log10,sqrt
#datos
#=======
#tres primeros solo va shiels Toc y correguir con zANG
d50=0.35   #diametro medio en mm
y=2.7003   #tirante del agua m
B=200      #base del canal m
g=9.807    #gravedad m/s2
s=0.0002   #pendiente del fondo del río
v=1.073    #velocidad del agua
T=20       #Temperatural del agua para peso especifico y viscosidad

R=B*y/(B+2*y)
#calcula funcion de T O ingresar peso espeficifico del agua kg/m3
p=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))) 
#Indice Simons
To=g*p*R*s
Tov=To*v
print("Esfuerzo cortante en el fondo To=",To,"N/m2")
print("Indice de Simons = ",Tov,"N/sm")
print("Diametro de particula = ",d50,"mm")
