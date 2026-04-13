#DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//              : Ing. Córdova Julca, Guillermo Arturo
//PROGRAMA      : Transporte de fondo - Du Boys
//LENGUAJE      : Python
#datos
y=2.7003    #Tirante m
B=200       #Ancho m
s=0.0002    #Pendiente del fondo m/m
p=998.2335  #Peso especifico del agua kg/m3
#Abaco
x=4.001           #obtener del abaco x
Toc=0.092         #obtener del abaco kg/m^2
#Aplicacion de Du Boys
R=B*y/(B+2*y)
To=p*s*R         #esfuerzo cortante fondo kg/m2
Tf=x*To*(To-Toc) #Transporte de fondo kg/s/m
Tf_t=Tf*B        #transporte de fondo kg/s
print("Radio R= ", R, "m")
print("Esfuerzo cortante To = ", To, "kg/m^2")
print("Transporte de fondo tF = ", Tf,3, "kg/s/m")
print("Transporte de fondo tF  = ", Tf_t, "kg/s")
