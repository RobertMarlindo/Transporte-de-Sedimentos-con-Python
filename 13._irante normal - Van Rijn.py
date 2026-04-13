//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Tirante normal - Van Rijn
// LENGUAJE      : Python
from math import log10,sqrt,exp
print("============================")
print("Formas de fondo")
print("============================")
//datos
//=======
y=2.7003        //Tirante del agua m calculado con RCanales
Q=579.69        //Caudal que transorta, 
Fr=0.2086       //numero de froude 
B=200           //base del canal
S=0.0002        //pendiente del fondo del canal
D50=0.35/1000   //diametro particula d50 m(metros) 
D90=0.90/1000   //diametro particula d90 m(metros)
ps=2650         //peso espeficifico del sólido kg/m3
Te=20           //temperatura del agua
g=9.807         //gravedad m/s2
?d=0.7          //van rjin
//v=1.073383753249639 //velocidad del flujo
R=(B*y)/(B+2*y) 
A=B*y          
u=(1.14-0.031*(Te-15)+0.00068*(Te-15)**2)*10**-6  
p=1000.*(1.-(Te+288.941)*pow(Te-3.986,2.)/(508929.2*(Te+68.13)))
s=ps/p
pr=(ps-p)/p //densidad ro
v=Q/A       //velocida para lo que se propuso
print("Densidad del agua p=",p,"kg/m3")
print("Radio Hidraulico = ",R,"m")
print("ps/p s = ",s)
print("Densidad relativa (ps-p)/p p' =",pr)
print("Velocidad v = ",v,"m/s")
//rugosidad asocionada al grano k's,c
print("\n Rugosidad asocionada al grano k's,c")
print("============================")
vc=sqrt(g*R*S)        //velocidad de corte m/s 
?=vc**2/((s-1)*g*D50) //teta para formas de granos
print("Velocidad de corte  vc* = ",vc,"m/s")
print("? = ",?)
if ?<1:
    ksc=3*D90
    print("Rugosidad al grando ?<1 k'sc = ",ksc)
else:
    ksc=3*?*D90
    print("Rugosidad al grando ?>=1 k'sc = ",ksc) 
//rugosidad de la altura asociada a la formas de fondo
//==== diagramas original =========
print("\nTipo de duna asociado")
print("============================")
D=(pr*g/u**2)**(1/3)*D50 //D*
C=18*log10(12*R/ksc)     //parametro de chezy para granos de fondo
T_bc=p*g*(v/C)**2        //Tb,c
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
Tb_cr=te*(ps-p)*g*D50    //esfuerzo cortante critico
T=(T_bc-Tb_cr)/Tb_cr
//T=2 //como nos da en el problema defrente aplicamos ello
print("D* =",D)
print("C´ = 18*log10(12*y/(3*D90))   =",C," m^(1/2)/s")
print("Esfuerzo cortante  T'b,c =",T_bc/g," kg/m2")
print("?cr =",te)
print("Esfuerzo cortante  T'b,cr =",Tb_cr/g," kg/m2")
print("Valor de T = ",T)
//busca de la tabla
//lower  = abajo
if T>=0 and T<=3:
    if D>=1 and D<=10:
        print("Pequeño megarizos 0<T<3; 1<D*<10")
    elif D>10:
        print("Dunas 0<T<3; D*>10")
elif T>3 and T<=10:
    if D>=1 and D<=10:
        print("Megarizos y dunas 3<T<10; 1<D*<10")
    elif D>10:
        print("Dunas 3<T<10; D*>10")
elif T>10 and T<=15:
    if D>=1 and D<=10:
        print("Dunas 10<T<15; 1<D*<10")
    elif D>10:
        print("Dunas 10<T<15; D*>10")     
//Transición
if T>15 and T<=25:
    print("Dunas lavadas, olas de san 15<T<25")   
//uppe r= arriba
if T>=25 and Fr<0.8:
    print("Olas simétricas de arena T>=25, Fr<0.8")
    print("(Symmetrical) sand waves")
elif T>=25 and Fr>=0.8:
    print("Cama plana y / o anti-dunas T>=25, Fr>=0.8")
    print("Plane bed and/or anti-dunes")   
//dimensiones de las dunas
print("\nRugosidad asocionada a la forma k''s,c")
print("============================")
?d=0.11*y*(D50/y)**.3*(1-exp(-.5*T))*(25-T)
?d=7.3*y
ksd=1.1*?d*?d*(1-exp(-25*?d/?d))
print("?d = ",?d)
print("?d = ",?d)
print("?d50 = ",?d)
print("Rugosidad a la forma k''s,c = ",ksd)
//Rugosidad total del rio
print("\nRugosidad absoluta ksc=k's,c+k''s,c")
print("============================")
k=ksc+ksd
Cc=18*log10(12*R/k)
vv=Cc*(R*S)**.5 //velocidad por chezy V=C*(R*S)^0.5
QQ=vv*A
print("Rugosidad absoluta k = ",k)
print("Coeficiente de Chezy Cc = ",Cc)
print("Velocidad del agua V = ",v,"m/s")
print("Caudal  Q = ",QQ,"m^3/s")
print("Manning  n = ",R**(1/6)/Cc)
print("Manning  n = ",(B*y)**(5/3)*(B+2*y)**(-2/3)*S**(1/2)/Q)
