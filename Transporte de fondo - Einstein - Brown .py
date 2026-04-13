#DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
#               : Ing. Córdova Julca, Guillermo Arturo
# PROGRAMA      : Transporte de fondo - Du Boys
# LENGUAJE      : Python
#datos
y=2.7003       #tirante en metros m o el radio hidráulico
B=200          #ancho del cauce en metros m
D50=0.00035    #D50 en metros 
D90=0.00090    #D90 en metro 
s=0.0002       #pendiente del fondo m/m
ps=2650        #densidad del solido kg/m^3
p=998.233      #peso especifico del agua kg/m3
U=1.001*10**-6 #viscosidad cinemática del agua m2/s
g=9.807        #gravedad m/s2
#calculo
R=(B*y)/(B+2*y) #radio hidráulico 
#proceso de calculo
To=p*s*R         #esfuerzo cortante en el fondo kg/m2
yy=(ps-p)*D50/To #parametro de shields
if yy<5.5:
    fi=40*(1/yy)**3 
else:
    fi=e**(-0.391*yy)/0.465 
sr=ps/p #densidad relativa
F=(2/3+36*U**2/(g*D50**3*(sr-1)))**.5-(36*U**2/(g*D50**2*(sr-1)))**.5 #otro factor
tF=fi*ps*F*(g*(sr-1)*D50**3)**.5 #inversa 1/n 
print("Esfuerzo cortante critico Toc = ", To, "kg/m^2")
print("(ps-p)*D50/To yy = ", yy)
print("fi = ", fi)
print("sr = ", sr)
print("F = ", F)
print("Transporte de solido de fondo  = ", tF,"kg/s/m")
print("Transporte de solido de fondo  = ", tF*B,"kg/s")
