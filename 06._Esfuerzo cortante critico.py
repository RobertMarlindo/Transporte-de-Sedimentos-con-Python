//DESARROLLADORES : Ing. Ramirez Quispe, Robert Marlindo
//                : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Esfuerzo cortante critico.
// LENGUAJE      : Python
from math import log10,sqrt
//Datos
//=======
D50=0.012       // diámetro de la partícula representativa en metros
ps=2650         // peso especifico del sólido kg/m3
g=9.807         // gravedad m/s2
T=20            // Temperatura del agua para peso especifico y viscosidad
//Calculo
p=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))) 
u=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6  
pr=(ps-p)/p               // densidad relativa
D=(pr*g/u**2)**(1/3)*D50  // D* para buscar en que rango 
if D>1 and D<=4:
    te=.24*D**(-1)
elif D>4 and D<=10:
    te=.14*D**(-.64)
elif D>10 and D<=20:
    te=.04*D**(-.1)
elif D>20 and D<=150:
    te=.013*D**(.29)
elif D>150:
    te=.055  
Toc=te*(ps-p)*D50 // esfuerzo cortante crítico
//Resultado
print("Esfuerzo cortante crítico Toc =",Toc,"kg/m2")
