import csv
import pickle
def crearReporteCVS(archivo,lista):
    abrir=open(archivo,"rb")
    lista=pickle.load(abrir)
    archivoCVS="reporteCVS.csv"
    guardarCVS=open(archivoCVS,mode='w', newline='',encoding="utf-8-sig")
    reporte=csv.writer(guardarCVS, delimiter=";")
    reporte.writerow(["Nombre","Apellidos","Género","Carné","Correo","Notas"])
    for i in range(len(lista)):
        if lista[i][1] == True:
            x="Masculino"
        else:
            x="Femenino"
        reporte.writerow([lista[i][0][0], lista[i][0][1]+" "+lista[i][0][2],x,lista[i][2],lista[i][3],lista[i][4]])