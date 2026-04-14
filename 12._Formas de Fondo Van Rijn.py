//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Formas de fondo - Van Rijn
// LENGUAJE      : Python
from math import log10,sqrt
print("============================")
print("Formas de fondo")
print("============================")
//datos
//=======
y=2.7003            //tirante del agua m calculado con RCanales
B=200               //base del canal
v=1.073             //velocidad m/s obtenido con Rcanales
Fr=0.2086           //Numero de froude de Rcanales opcional
D50=0.35/1000       //diametro particula d50 m(metros) para micras multipicar 10^6
D90=0.90/1000       //diametro particula d90 m(metros)
ps=2650             //peso espeficifico del sólido kg/m3
g=9.807             //gravedad m/s2
Te=20
R=B*y/(B+2*y)
//calcula funcion de T O ingresar peso espeficifico del agua kg/m3
u=(1.14-0.031*(Te-15)+0.00068*(Te-15)**2)*10**-6  //calcula funcion de T O viscosidad cinematica del fluido m2/s
p=1000.*(1.-(Te+288.941)*pow(Te-3.986,2.)/(508929.2*(Te+68.13)))
//Método de Van Rijn
//calculo de parametro de shiedls
//==== diagramas original =========
pr=(ps-p)/p //densidad ro
D=(pr*g/u**2)**(1/3)*D50 //D*
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
C=18*log10(12*R/(3*D90)) //parametro de chezy
T_bc=p*g*(v/C)**2
T=(T_bc-Tb_cr)/Tb_cr
print("Radio hidraulico R=",R,"m")
print("vicosidadp",u,"kg/m3")
print("densidad p",p,"kg/m3")
print("(ps-p)/p",(ps-p)/p,"-")
print("Tirante de agua y =",y,"m")
print("Velocidad de agua V =",v,"m/s")
print("densidad ro &=&",pr)
print("D* =",D)
print("Teta cr =",te)
print("Esfuerzo cortante critico Tb,cr =",Tb_cr,"N/m2")
print("18*log10(12*y/(3*D90)) C  =",C,"m^(1/2)/s")
print("Esfuerzo cortante critico Tb,c =",T_bc,"N/m2")
print("Valor de T  ",T)
//busca de la tabla
//lower  = abajo
if T>=0 and T<=3:
    if D>=1 and D<=10:
        print(" Pequeño megarizos 0<T<3; 1<D*<10")
    elif D>10:
        print(" Dunas 0<T<3; D*>10")
elif T>3 and T<=10:
    if D>=1 and D<=10:
        print(" megarizos y dunas 3<T<10; 1<D*<10")
    elif D>10:
        print(" Dunas 3<T<10; D*>10")
elif T>10 and T<=15:
    if D>=1 and D<=10:
        print(" Dunas 10<T<15; 1<D*<10")
    elif D>10:
        print(" Dunas 10<T<15; D*>10")       
//transition
if T>15 and T<=25:
    print(" Dunas lavadas, olas de san 15<T<25")   
//uppe r= arriba
if T>=25 and Fr<0.8:
    print(" olas simétricas de arena T>=25, Fr<0.8")
    print(" (symmetrical) sand waves")
elif T>=25 and Fr>=0.8:
    print(" cama plana y / o anti-dunas T>=25, Fr>=0.8")
    print(" plane bed and/or anti-dunes")  
