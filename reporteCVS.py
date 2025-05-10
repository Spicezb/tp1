import csv
import os
import pickle
def crearReporteCVS(archivo,lista):
    """
    Funcionamiento:
    - Crea el reporte CVS con la iformacion de los estudiantes.
    Entradas:
    - archivo: Es el archivo de la base de datos.
    - lista: Es lista con la que se va a manejar la informaci;on de la base de datos.
    Salidas: 
    - Retorna un mensaje de que el archivo se creo correctamente.
    """
    try:
        abrir=open(archivo,"rb")
        lista=pickle.load(abrir)
        archivoCVS="reporteCVS.csv"
        guardarCVS=open(archivoCVS,mode='w', newline='',encoding="utf-8-sig")
        reporte=csv.writer(guardarCVS, delimiter=";")
        reporte.writerow(["Nombre","Apellidos","Género","Carné","Correo","Notas","Estado"])
        for i in range(len(lista)):
            if lista[i][1] == True:
                x="Masculino"
            else:
                x="Femenino"
            if lista[i][4][-1]<60:
                estado="Reprobado"
            elif lista[i][4][-1]<70:
                estado="Reposición"
            else:
                estado="Aprovado"
            reporte.writerow([lista[i][0][0], lista[i][0][1]+" "+lista[i][0][2],x,lista[i][2],lista[i][3],lista[i][4],estado])
    except PermissionError:
        os.system("cls")
        print("Debe cerrar el documento csv para generar uno nuevo.")