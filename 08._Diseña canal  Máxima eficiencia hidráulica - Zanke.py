//DESARROLLADORES : Ing. Ramirez Quispe, Robert Marlindo
//                : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Diseña canal  Máxima eficiencia hidráulica
//               : Riesgo Zanke
//               : Método de Newton
// LENGUAJE      : Python
from math import log10,sqrt,atan,pi,tan,cos,log,exp
//datos esfuerzo cortante
//=======
D50=0.045       // diámetro de la partícula representativa en metros
D90=0.090       // diámetro D90
ps=2650         // peso especifico del sólido kg/m3
s=0.0015        // pendiente del fondo del río
g=9.807         // gravedad m/s2
T=20            // temperatura
R=2             // Zanke % confiabilidad
//calcula función de T O ingresar peso especifico del agua kg/m3
p=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))) 
u=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6  // calcula función de T O viscosidad cinemática del fluido m2/s
// dato para canal
fi=37       // ángulo de reposo de la partícula
z=3         // talud del canal 2H:1V la parte de vertical
Q=50        // caudal en m3/s
F=0.85      // 0.75 ?.y.S depende de la talud para canal
//calculo de parámetro de shiedls
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
nom=["Shields","Shields y Zanke riesgo(R)"]
for J in range(2):   
    Toc=te*(ps-p)*D50 // esfuerzo cortante critico
    y=Toc/(p*s) // altura del nivel de agua
    k=2*D90 // rugosidad del río
    c=18*log10(12*y/k) //c de chezy
    v=c*sqrt(y*s)
    q=v*y //q=Q/B=(v*A)/B=(v*B*y)/B=v*y caudal específico
    //======================
    // empleando la fórmula de Zanke 2%
    // método de biseccion en el rango de [0.000000001,te]
    a=0.000000001 // es mínimo valor que va tomar
    b=te  // el limite superior se pone porque sera menor a ello
    for I in range(100):
        c=(a+b)/2
        fa=R/100-(10*(a/te)**-9+1)**-1
        fb=R/100-(10*(b/te)**-9+1)**-1
        fc=R/100-(10*(c/te)**-9+1)**-1
        if fa*fc>0:
            a=c
        else:
            b=c
        if abs(fc)<.00001:
            break
        //print(I+1,a,b,c)
    print("====================")
    print(nom[J])
    print("====================")
    print("densidad ro =",pr)
    print("D* =",D)
    print("cr =",te)
    print("esfuerzo cortante critico Toc =",Toc,"kg/m2")
    print("altura de agua equivalente y =",y,"m")
    print("rugosidad del rio k =",k)
    print("chezyo c =",c)
    print("Velocidad del fluido =",v,"m/s")
    print("caudal específico =",q,"m3/s/m")
    te=c //?cr cambia con Zanke riesgo(R)
// esfuerzo cortante en la orillas
alf=atan(1/z)
ka=cos(alf)*(1-tan(alf)**2/tan(fi*180/pi)**2)**.5
Toc_orr=ka*Toc
yo=Toc_orr/(F*p*s) //altura del nivel de agua de acuerd a orrillas
print("===============")
print("talud esfuerzo cortante Toc")
print("===============")
print("inclinación de talud alfa = ",alf*180/pi)
print("ka = ",ka)
print("Toc orrillas = ",Toc_orr)
print("y acuerdo a orillas = ",yo)
//dimensionamiento de canal
k=2*D90
//=====================
//tirante proponer y te encuentra la base
//=====================
//Newthon para calcular tirante
AA=6/k
BB=18*sqrt(s/2)*(2*sqrt(1+z**2)-z)
y=0.99
yf=0.98
for I in range(40):
    y=yf
    fx=BB*y**(5/2)*log10(AA*y)-Q
    dfx=5/2*BB*y**(3/2)*log10(AA*y)+BB*y**(5/2)/(y*log(10))
    yf=y-fx/dfx
    if abs(y-yf)<.00001:
        break    
//=====================
y=yf   
B=2*y*(sqrt(1+z**2)-z)
A=B*y+z*y**2
P=B+2*y*(1+z**2)**.5
R=A/P
c=18*log10(12*R/k) //c de chezy
v=c*sqrt(R*s)    
Q=A*v
print("===============")
print("Diseño de canal")
print("===============")
print("Tirante calculado y= ",y,"m")
print("Base calculado B= ",B,"m")
print("Espejo T= ",B+2*z*yo,"m")
print("Area A= ",A,"m2")
print("Perimetro P= ",P,"m")
print("Radio Hidraulica R= ",R,"m")
print("Rugosidad ks= ",k)
print("chezy  c= ",c,"m^(1/2)/s")
print("veocidad v= ",v,"m/s")
print("caudal Q= ",Q,"m/s")
if Toc_orr>p*R*s:
    print("Ok cumple")
else:
    print("no cumple")
print("To= ",p*R*s,"kg/m2")
print("b/y= ",2*(sqrt(1+z**2)-z)-B/y,"debe ser cero")
