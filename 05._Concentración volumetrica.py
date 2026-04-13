//DESARROLLADORES: Ing. Ramirez Quispe, Robert Marlindo
//               : Ing. Córdova Julca, Guillermo Arturo
//LENGUAJE       : Python                          
//PROGRAMA       : Concentración volumetrica
v=700     //volumen de muestra en cm^3 (agua y solidos)
ws=0.32   //peso del material solido secado en horno N(nethon=kgxm/s^2)
ps=2650   //densidad del solido kg/m^3
pw=1000   //densidad del agua kg/m^3
g=9.807   //gravedad m/s^2
//conversiones
v_m3=v/100**3         //volumen total muestra en litros m^3
v_L=v*1000/(10**6)    //volumen total muestra en litros L
ws_kg=ws/g            //peso del material solido secado en horno en kg(kilogramo)
ws_mg=ws/g*10**6      //peso del material solido secado en horno en mg(miligramo)
vs_m3=ws_kg/ps        //volumen de solido seco en m^3
v_agua=v_m3-vs_m3     //volumen de agua en m^3
w_agua_kg=v_agua*pw   //peso del agua en kg
//G=ps/pw              //gravedad especifica adimensional
//Concentración volumétrica
cv=vs_m3/v_m3 //concentracion volumentrica adimensional Vs/Vt
//Concentración en peso
cw=ws_kg/(w_agua_kg+ws_kg)//concentracion en peso adimensional Ws/Wt
//concentracion en peso en partes por millon cpp
cw_ppm=10**6*cw //concentracion en peso en partes por millon cpp
//concentracion de solidos
C=ws_mg/v_L //concentracion de solidos mg/L
print("Volumen de muestra total V = ",round(v_m3,13)," m^3")
print("Volumen de muestra total V = ",round(v_L,13)," L")
print("Peso de solido seco ws = ",ws_kg," kg")
print("Peso de solido seco ws = ",ws_mg," mg")
print("Volumen de solidos Vs = ",vs_m3,"m^3")
print("Volumen de agua V = ",v_agua,"m^3")
print("Peso del agua = ",w_agua_kg,"kg")
print("====================")
print("Concentracion volumétrica Cv = ",cv,"m^3/m^3")
print("Concentracion en peso Cw = ",cw,"kg/kg")
print("Concentracion en solidos C = ",cw_ppm," ppm")
print("Concentracion de solidos C = ",C," mg/L")
