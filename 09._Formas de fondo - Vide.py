
//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Formas de fondo - Vide
// LENGUAJE      : Python
from math import log10,sqrt
//datos
//=======
//tres primeros solo va shiels Toc y correguir con zANG
y=2.7003
B=200
D50=.35/1000    //diametro de la particula representativa en metros
ps=2650         //peso espeficifico del sólido kg/m3
g=9.807         //gravedad m/s2
s=0.0002        //pendiente del fondo del río
T=20            //Temperatural del agua para peso especifico y viscosidad
R=B*y/(B+2*y)
//calcula funcion de T O ingresar peso espeficifico del agua kg/m3
u=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6  //calcula funcion de T O viscosidad cinematica del fluido m2/s
p=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))) 
//Indice de inestabilidad
vc=(g*R*s)**.5
Re=vc*D50/u
//Indice de movilidad
To=p*R*s
IM=To/((ps-p)*D50)
print("Velocidad de corte vc=",vc,"m/s")
print("Indice de inestabilidad Re = ",Re)
print("Esfuerzo cortante en el fondo To=",To,"kg/m2")
print("Indice de movilidad IM = ",IM)
