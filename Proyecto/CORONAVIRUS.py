import os
os.system("cls")
#Definir las variables
op='0'
datos=[]
inf=0
prom=0
graves=0
#Saludamos al usuario que va a ocupar el programa
print("\n\t\t\t\tBienvenido al señalizador de covid\n\n\n\n")
while(op!='2'):
    print('\n')
    #Primer menu
    print(" 1)Llenar\n 2)Recolectar datos")
    op=input("escoge una opción")
    if op=='1':
        #Pedimos información necesaria
        edad=input("Edad paciente")
        rango=input("Rango en el estudio [0-1]:")
        tos=input("¿Tiene tos?     1)no     2)sí")
        fiebre=input("¿Tiene fiebre?     1)no     2)sí")
        #Dividimos la población en casos positivos y negativos
        if float(rango)>=0.8:
            inf=inf+1
            prom=prom+int(edad)
            if int(tos)==2:
                revision="Síntomas leves"
            if int(fiebre)==2:
                revision="Síntomas leves"
            if int(tos+fiebre)==4:
                revision="Síntomas graves"
                graves=graves+1
        else:
            revision="Sin síntomas"
            
        #Sirve para arreglar al renglón nuestros datos
        reg=edad+','+rango+','+fiebre+','+tos+','+revision+'\n'
        datos.append(reg)
    elif op=='2':
        print("Vuelva pronto")
    else:
        print("Opción no procesada")
print(datos)
#llamamos al excel
a=open("bd.csv","a")
a.writelines(datos)
a.close()
prom=prom+int(edad)
#Dependiendo del semaforo se darán las indicaciones necesarias
if inf==0:
    print("El semaforo es verde, Se permiten todas las actividades, incluidas las escolares.")
elif inf>=1 and inf<=30:
   print("El semaforo es amarillo, Todas las actividades laborales están permitidas, cuidando a las personas con mayor riesgo de presentar un cuadro grave de COVID-19. El espacio público abierto se abre de forma regular, y los espacios públicos cerrados se pueden abrir con aforo reducido. Como en otros colores del semáforo, estas actividades deben realizarse con medidas básicas de prevención y máximo cuidado a las personas con mayor riesgo de presentar un cuadro grave de COVID-19.") 
elif inf>=31 and inf<=70 :
  print("El semaforo es naranja, Además de las actividades económicas esenciales, se permitirá que las empresas de las actividades económicas no esenciales trabajen con el 30% del personal para su funcionamiento, siempre tomando en cuenta las medidas de cuidado máximo para las personas con mayor riesgo de presentar un cuadro grave de COVID-19, se abrirán los espacios públicos abiertos con un aforo (cantidad de personas) reducido.")
elif inf>=71 and inf<=100:
    print("El semaforo es rojo,Se permitirán únicamente las actividades económicas esenciales, asimismo se permitirá también que las personas puedan salir a caminar alrededor de sus domicilios durante el día.")

print("El número de infectados graves es",graves)
print("El número de infectado es",inf)
#Abrimos excel
a=open("bd.csv","r")
infor=a.read()
a.read()
a.close()
prom=prom/inf
print("Edad promedio de los infectados",prom)
