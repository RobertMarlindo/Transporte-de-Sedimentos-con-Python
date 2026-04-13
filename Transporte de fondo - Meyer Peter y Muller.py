#DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
#               : Ing. Córdova Julca, Guillermo Arturo
# PROGRAMA      : Transporte de fondo - Meyer Peter y Muller
# LENGUAJE      : Python
#datos
#=======
#T=20ºC
#=======
#datos
y=2.7003      #tirante m
B=200         #ancho m
D50=0.00035   #d50
D90=0.00090   #d90
S=0.0002      #pendiente del fondo m/m
ps=2650       #densidad del solido kg/m^3
p=998.2335    #peso especifico del agua kg/m3
ns=0.025      #rugosidad de Manning  n total
R=(B*y)/(B+2*y)   #radio hidraulico  
To=p*S*R          #esfuerzo cortante en el fondo kg/m2
kr=26/D90**(1/6)  
nr=1/kr
ks=1/ns
u=(ks/kr)**1.5       
Toc=0.047*(ps-p)*D50 #Esfuerzo cortante critico 
tf_agua=0.79*(u*To-Toc)**1.5 #transporte de solido con agua
tF=ps/(ps-p)*tf_agua #transporte de solido sin agua
print("Esfuerzo cortante  fondo To = ", To, "kg/m^2")
print("Formas y grano ks = 1/n = ", 1/ns ," ns  = ",ns)
print("Granos kr = ", kr," nr  = ",nr)
print("Coeficiente de rizos u = ", u)
print("Esfuerzo cortante critico Meyer  = ", Toc,"kg/m2")
print("Transporte de solido  agua = ", tf_agua,"kg/s/m")
print("Transporte de solido  sin agua = ", tF,"kg/s/m")
print("Transporte de solido  en ancho = ", tF*B,"kg/s")
