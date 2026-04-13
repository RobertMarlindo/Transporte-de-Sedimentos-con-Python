//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Transporte de suspensión - Einstein
// LENGUAJE      : Python
q=2.9099    //Caudal especifico m3/s/m
Ca=0.0001   //Concentración 
W=0.05188   //Velocidad de caída 
R=2.62930   //Radio hidráulico
s=0.0002    //Pendiente del ca
g=9.807     //Gravedad 
D65=.00045  //D65 metros m 
n=0.025     //Rugosidad del
p=998.23    //Densidad del agua kg/m3
U=1*10**-6  //Viscosidad cinematica
x=1.3       //Leer de monograma 
I1=0.32     //Leer de monograma 
I2=-2.7     //Leer de monograma 
vc=sqrt(g*R*s)  
a=2*D65         
Ca_kgm3=Ca*p    
?=D65/x
?=11.6*U/vc 
v_x=D65/? 
Z=W/(0.4*vc)   //para leer valor de I1
A=2*D65/R      //para leer valor de I2
qsw=11.6*vc*Ca_kgm3*a*(2.303*log10(30.2*R/?)*I1+I2) 
