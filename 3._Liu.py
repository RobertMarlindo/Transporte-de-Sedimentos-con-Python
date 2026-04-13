#DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
#               : Ing. Córdova Julca, Guillermo Arturo
# PROGRAMA      : Formas de fondo - Liu
# LENGUAJE      : Python
from math import log10,sqrt
print("Criterio de shields iniciación de movimiento")
#datos
#=======
#tres primeros solo va shiels Toc y correguir con zANG
y=2.7003
B=200
D50=.35/1000       #diametro de la particula representativa en metros
ps=2650         #peso espeficifico del sólido kg/m3
g=9.807         #gravedad m/s2
S=0.0002        #pendiente del fondo del río
T=20            #Temperatural del agua para peso especifico y viscosidad
R=B*y/(B+2*y)
#calcula funcion de T O ingresar peso espeficifico del agua kg/m3
u=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6  #calcula funcion de T o viscosidad cinematica del fluido m2/s
p=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))) 
#Indice de inestabilidad
vc=(g*R*S)**.5
Re=vc*D50/u
#indice movilidad
#particulas no esfericas
#===========
d50=D50*1000
s=ps/p
if  d50>0.001 and d50<=0.1:
    ws=(s-1)*g*(0.001*d50)**2/(18*u)
elif d50>0.1 and d50<=1:
    ws=10*u/(0.001*d50)*((1+0.01*(s-1)*g*(0.001*d50)**3/u**2)**.5-1)
elif d50>1:
    ws=1.1*((s-1)*g*0.001*d50)**.5  
print("Densidad del agua p= ",p,"kg/m3")
print("ps/p= ",ps/p,"kg/m3")
print("Velocidad de corte vc=",vc,"m/s")
print("Indice de inestabilidad Re = ",Re)
print("Velocidad de caida ws = ",ws," m/s")
print("Indice movilidad vc/ws = ",vc/ws)
