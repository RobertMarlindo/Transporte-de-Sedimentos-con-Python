//====================================================
//DESARROLLADORES     : Ing. Ramirez Quispe, Robert Marlindo
//                    : Ing. Córdova Julca, Guillermo Arturo
//LENGUAJE            : Python                          
//PROGRAMA            : Granulometría                            
//FECHA               : 10/06/2020 DD/MM/AA             
//LUGAR               : Ingeniería Hidráulica - Lima UNI
//CONSULTA            : ramirezquispe1@hotmail.com       
//====================================================
import matplotlib.pyplot as plt
import sys
import xlwt
import xlrd,datetime
import xlsxwriter


//datos diametro de particulas y porcenta que pasa
//=====================
dmm=[0.072, 0.15,   0.3, 0.42,	0.59,	1.3,	2.8,	4.9]//diametro en milimetros
xpa=[0    , 7,	    18,   38,	57,	89,	96,	99]//porcentaje que pasa
ld=[50,65,90]//diámetros en donde quieres interpolar

//lista para graficar la escala logaritmica
//========================
XX=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
XL=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10]

//calcula los diametros de las lista ld
//lo que asignaste
//===================
dc=[]//lista de diametros
for J in range(len(ld)):
    dp=ld[J]
    for  I in range(len(xpa)-1):
        if xpa[I]<=dp<xpa[I+1]:
            a=xpa[I]
            b=dmm[I]
            c=xpa[I+1]
            d=dmm[I+1]
            xmm=(d-b)*(dp-a)/(c-a)+b //diametro
            dc.append(xmm)
            break
    print("d"+str(dp) +" = "+str(round(xmm,4))," mm")


//diametro efectivo
//de acuerdo que se le dio al comienzo la lista de diametros
//lo calcula muy aparte
//===================
defe=0   
for J in range(len(xpa)-1):
    dp=(xpa[J+1]+xpa[J])/2
    for  I in range(len(xpa)-1):
        if xpa[I]<=dp<xpa[I+1]:
            a=xpa[I]
            b=dmm[I]
            c=xpa[I+1]
            d=dmm[I+1]
            xmm=(d-b)*(dp-a)/(c-a)+b //diametro
            defe=defe+(xpa[J+1]-xpa[J])*xmm
            break
defe=defe/100    
print("d efectivo = "+str(round(defe,4))+"mm")

//Desviación estandar y Coeficiente de gradación
//teniendo en cuenta d16,d50 y d84
//================================
desta=[16,50,84]
ldimm=[]//diametro para cada caso
for J in range(len(desta)):
    dp=desta[J]
    for  I in range(len(xpa)-1):
        if xpa[I]<=dp<xpa[I+1]:
            a=xpa[I]
            b=dmm[I]
            c=xpa[I+1]
            d=dmm[I+1]
            xmm=(d-b)*(dp-a)/(c-a)+b //diametro
            ldimm.append(xmm)
            break
    print("d"+str(dp) +" = "+str(round(xmm,4)),"mm")
Gg=(ldimm[2]/ldimm[0])**(.5)               //Desviación estandar
Gr=.5*(ldimm[2]/ldimm[1]+ldimm[1]/ldimm[0])//Coeficiente de gradación 
print("Desviación estandar  Gg  ="+str(round(Gg,4)))
if Gr<3:    
    print("Coeficiente de gradación Gr = "+str(round(Gr,4))+" material mal graduado < 3mm")

else:    
    print("Coeficiente de gradación Gr = "+str(round(Gr,4))+" material bien graduado >3mm")

//ggrafica la granulometria
//==============================
plt.plot(dmm,xpa, marker='o', linestyle=':', color='b',label = "Granulometría") //perfil de agua


//grafica d5, d15, d25 ...
//==============================
"""
LL=["d50","d90",]
CL=["r","b","g"]
for I in range(len(dc)):
    plt.plot([dc[I],dc[I]],[0,ld[I]], linestyle='--', color=CL[I],label = LL[I]) //graficar los diametros
    plt.plot([0,dc[I]],[ld[I],ld[I]], linestyle='--', color=CL[I]) //graficar los diametros
//==============================
    

//grafica d16, d50, d84
//==============================
LL=["d16","d50","d80"]
CL=["r","b","g"]
print(ldimm)
for I in range(len(ldimm)):
    plt.plot([ldimm[I],ldimm[I]],[0,desta[I]],  linestyle='--', color=CL[I],label = LL[I]) //graficar los diametros
    plt.plot([0,ldimm[I]],[ldimm[I],desta[I]], linestyle='--', color=CL[I]) //graficar los diametros
//==============================
"""

//grafica diámetro efectivo
//==============================    
plt.plot([defe,defe],[0,ld[0]], linestyle='--', color='g',label = "Diámetro efectivo") //diametro efectivo

plt.xscale('log') //escala logarimitca
//plt.title('Granulometría' , fontsize=16)
plt.xlabel("Diámetro de material (mm)")   // Establece el título del eje x 
plt.ylabel("% que pasa")   // Establece el título del eje y
plt.grid(True)  // Activa cuadrícula del gráfico pero no se muestra
plt.xticks(XL)  
plt.legend(loc="best") 
plt.show()    

