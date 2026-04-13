//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Tirante normal - Engelund y Hansen
// LENGUAJE      : Python
from math import log10,log,sqrt,exp
print("============================")
print("Formas de fondo")
print("============================")
//datos
//=======
Q=579.69      //Caudal que transorta, solo sirve para validad al final
y=2.61076     //Tirante del agua m calculado con RCanales
B=200         //base del canal
S=0.0002      //pendiente del fondo del canal
D50=0.35/1000 //diametro particula d50 m(metros) para micras multipicar 10^6
D90=0.90/1000 //diametro particula d90 m(metros)
ps=2650       //peso espeficifico del sólido kg/m3
Te=20         //temperatura del agua
g=9.807       //gravedad m/s2
R=(B*y)/(B+2*y)    //se considera radio hidraulico que el tirante en canal ancho
u=(1.14-0.031*(Te-15)+0.00068*(Te-15)**2)*10**-6   fluido m2/s
p=1000.*(1.-(Te+288.941)*pow(Te-3.986,2.)/(508929.2*(Te+68.13)))
s=ps/p
pr=(ps-p)/p    //densidad ro
v=Q/(B*y)  
//calculo
//=======    
vc=sqrt(g*R*S) //velocidad de corte
?=round(vc**2/((s-1)*g*D50),1)
print("Desnidad del agua ",p,"kg/m3")
print("Velocidad de corte vc=",vc,"m/s")
print("Radio Hidraulico = ",R,"m")
print("ps/p s = ",s)
print("Densidad relativa (ps-p)/p p' =",pr)
print("Velocidad v = ",v,"m/s")
print("? = ",?)
if ?<0.7:
    ?p=0.06+0.4*?**2
    print("?' = ",?p,"Regimen bajo")
elif ?>=0.7 and ?<1:
    ?p=?
    print("?' = ",?p,"Regimen alto")
elif ?>=1:
    ?p=(0.3+0.7*?**-1.8)**-.56
    print("?' = ",?p,"Regimen alto")    
vcp=sqrt(?p*(s-1)*g*D50) 
hp=vcp**2/(g*S)
C=2.5*sqrt(g)*(hp/y)**.5*log(12*hp/(2.5*D50))
vv=C*(R*S)**.5 
QQ=vv*B*y
print("sqrt(?p*(s-1)*g*D50) velocidad corte v' = ",vcp,"m/s")
print("vcp**2/(g*S) h' = ",hp,"m")
print("Coeficiente de Chezy C = ",C,"m^(1/2)/s")
print("Velocidad del agua V = ",vv,"m/s")
print("Caudal  Q = ",QQ,"m^3/s")
print("Manning  n = ",R**(1/6)/C)
print("Manning  n = ",(B*y)**(5/3)*(B+2*y)**(-2/3)*S**(1/2)/Q)
