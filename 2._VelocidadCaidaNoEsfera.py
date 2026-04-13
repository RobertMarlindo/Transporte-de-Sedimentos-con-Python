//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
//LENGUAJE       : Python                          
//PROGRAMA       : Velocidad de caida                          
//datos
T=20       //Temperaruta del agua ºC
d50=0.35   //Diametro particula mm
s=2.65     //Gravedad especifica (2.65) o pesos especifico peso especifico/densidad del agua
g=9.807    //Aceleración de la gravedad (m/s^2)
//calculo
U=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6  //viscsidad cinematica m2/s
if  d50>0.001 and d50<=0.1:
    ws=(s-1)*g*(0.001*d50)**2/(18*U)
elif d50>0.1 and d50<=1:
    ws=10*U/(0.001*d50)*((1+0.01*(s-1)*g*(0.001*d50)**3/U**2)**.5-1)
elif d50>1:
    ws=1.1*((s-1)*g*0.001*d50)**.5
//resultado
print("viscosidad cinematica U = ",U,"m^2/s")
print("Velocidad de caida ws = ",ws," m/s")



