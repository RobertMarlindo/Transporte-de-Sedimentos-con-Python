#DESARROLLADORES : Ing. Ramirez Quispe, Robert Marlindo
#                : Ing. Córdova Julca, Guillermo Arturo
// PROGRAMA      : Soluciona la ecuación de Zanke
//               : Método de Bisección
// LENGUAJE      : Python
te=.055
a=0.000000001 # es mínimo valor que va tomar
b=te  # el limite  máximo es te, porque es menor teo
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
    #print(I+1,a,b,c)
teo=c
\end{lstlisting}