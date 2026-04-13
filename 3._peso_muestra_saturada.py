#====================================================
#DESARROLLADORES     : Ing. Ramirez Quispe, Robert Marlindo
#                    : Ing. Córdova Julca, Guillermo Arturo
#LENGUAJE            : Python                          
#PROGRAMA            : Peso de muestra saturado                      
#FECHA               : 10/06/2020 DD/MM/AA             
#LUGAR               : Ingeniería Hidráulica - Lima UNI
#CONSULTA            : ramirezquispe1@hotmail.com       
#====================================================
from math import pi
#datos
T=20       #temperatura
g=9.807    #gravedad m/s^2
P=0.3      #porosidad del material
Vt=1.4137  #volumen total de material
ps=2650    #peso específico del solido kg/m3
#densidad del agua
pw=round(1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13))),1)#densidad del agua kg/m3
#volumen de vacios
#para que se sature ello tendría que estar con agua
Vv=P*Vt
#volumen de solidos
#lo cual sería lo mismo Vs=Vt-Vv
#Vs=volumen de solidos sin los vacios
#Vt=Volumen total extraido de la calicata
#Vv=Volumne de vacios que tiene de acuerdo a Porosidad
Vs=Vt-P*Vt
#peso de material saturado
P_kg=pw*Vv+ps*Vs    #peso en kg saturado
print("densidad del agua pw = ",pw,"kg/m^3")
print("Volumen total Vt = ",Vt,"m^3")
print("Volumen de vacios Vv = ",Vv,"m^3")
print("Volumen de solidos Vs = ",Vs,"m^3")
print("Peso solido seco W = ",ps*Vs*g,"N")
print("Peso solido seco W = ",ps*Vs,"kg")
print("Peso solido saturado W = ",P_kg*g,"N")
print("Peso solido saturado W = ",P_kg,"Kg")
