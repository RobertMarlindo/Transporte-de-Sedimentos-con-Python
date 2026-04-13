//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
//LENGUAJE       : Python                          
//PROGRAMA       : Densidad y Viscosidad del agua                               
//datos
T=20 //temperaruta del agua ºC
//calculo
pw=1000.*(1.-(T+288.941)*pow(T-3.986,2.)/(508929.2*(T+68.13)))//densidad del agua kg/m3
U=(1.14-0.031*(T-15)+0.00068*(T-15)**2)*10**-6                 //viscsidad cinematica m2/s
//resultado
print("Densidad del agua pw = ",pw,"kg/m3")
print("Viscsidad cinematica U = ",U,"m2/s")
