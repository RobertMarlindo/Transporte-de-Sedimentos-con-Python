//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Transporte de suspensión - Lane y Kalinske
// LENGUAJE      : Python
from math import e, sqrt
q=2.9099  //Caudal liquido especifico m3/s/m
Ca=0.0001 //Concentración de sedimento distancia a Kg. soligo/Kg.agua
W=0.05188 //Velocidad de caída correspondiente a d50. m/s
R=2.62930 //Radio hidraulico,m
s=0.0002  //Pendiente del cauce principal m/m
a=0.25    //Distancia de referencia de transporte de solido 
g=9.807   //Gravedad m/s2
n=0.025   //Rugosidad del material para escoger curva
p=998.23  //Densidad del agua kg/m3
PL=0.08   //Obtenemos de la curva
//calculo
//velocidad de corte
vc=sqrt(g*R*s)      //Velocidad de Corte m/s
//velocidad media
v=R**(2/3)*s**(1/2)/n
//relacion de velocidad de caida y corte
W_vc=W/vc         //para escoger en el eje X y calcular PL
//para escoger en la curva
n_R16=n/R**(1/6)  //para escoger curva y calcular PL
//concentracion de sedimentos
Ca_kgm3=Ca*p      //transformamos a kg/m3
qsw=q*Ca_kgm3*PL*e**(15*W*a/(vc*R))  //Caudal Solido en suspensión especifico  kg/s/m
print("===========")
print("Resultados")
print("===========")
print("Velocidad de corte V* = ",vc,"m/s")
print("Velocidad media V = ",v,"m/s")
print("w/vc para leer PL en el eje X  = ",W_vc)
print("n/n^(1/6) para escoger la curva para PL = ",n_R16)
print("Concentración de sedimento Ca = ",Ca_kgm3,"kg/m3")
