# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 23/04/2025 a las 12:00
# Ultima modificación: 09/05/2025 a las 22:20
# Versión de python: 3.13.2

#importación de librerías
from fpdf import FPDF
import pickle
import os
# IMPORTANTE se debe de descargar la libreria fpdf.
def crearPDF(archivo,lista):
    """
    Funcionamiento:
    - Crea el archivo PDF con la información de los estudiantes aplazados en 2 o más exámenes.
    Entradas:
    - archivo: contiene el archivo donde se guarda la información de la base de datos.
    - lista: es donde se maneja la información de la base de datos.
    Salidas:
    - Retorna un mensaje avisando que el PDF se creó correctamente.
    """
    try:
        os.system("cls")
        print("******************** Aplazados en al menos 2 rubros ********************")
        conta=0
        conta2=0
        conta3=0
        notaMin=0
        notaMan=0
        abrirBD=open(archivo,"rb")                          # Se utiliza para abrir la información de la Base de Datos.
        lista = pickle.load(abrirBD)
        pdfAplazados= FPDF()                                # Se crea el objeto PDF.
        pdfAplazados.add_page()                             # Se pone una página.
        pdfAplazados.set_font('Arial', 'B', 16)             # Se le da formato a las letras.
        pdfAplazados.cell(0, 10, 'Aplazados en al menos 2 rubros', ln=True, align='C')          # Se le agrega información
        pdfAplazados.ln(5)
        pdfAplazados.set_font('Arial', 'B', 14)
        pdfAplazados.cell(0, 10, 'Información de estudiantes aplazados: ', ln=True, align='L')
        pdfAplazados.ln(1)
        pdfAplazados.set_font('Arial', '', 12)
        for i in range(len(lista)):                         # Se pregunta por la cantidad de notas menores a 70
            for x in range(0,3):
                if float(lista[i][4][x]) < 70:
                        conta+=1
                        if notaMan<int(lista[i][4][x])<70:
                            notaMan=int(lista[i][4][x])
                        elif notaMin==0:
                            notaMin=int(lista[i][4][x])
                        elif int(lista[i][4][x])<notaMin:
                            notaMin=int(lista[i][4][x])
            if conta >= 2:                                  # Se cuentan los estudiantes con solo 2 reprobados.
                if conta==2:
                    conta2+=1
                else:                                       # Se cuentan los de 3 reprobados.
                    conta3+=1
                infoEstu= str(lista[i][4][0])+", "+str(lista[i][4][1])+", "+str(lista[i][4][2])+", "+ \
                str(lista[i][0][0])+", "+str(lista[i][0][1])+" "+str(lista[i][0][2])+", "+str(lista[i][2])+", "+str(lista[i][3]+".")
                pdfAplazados.cell(0,10,infoEstu, ln=True, align='L')
            conta=0                                         # Se le va metiendo la información correspondiente al PDF.
        pdfAplazados.cell(0, 10, '* Un total de '+str(conta2+conta3)+' estudiantes tuvieron este inconveniente para un porcentaje de '\
                        +str(round(((conta2+conta3)/len(lista))*100,2))+', segun el total de', ln=True, align='L')
        pdfAplazados.cell(0, 10, str(len(lista))+' estudiantes en la base de datos.', ln=True, align='L')
        pdfAplazados.cell(0, 10, '* Reporte de nota minima: '+str(notaMin), ln=True, align='L')
        pdfAplazados.cell(0, 10, '* Reporte de nota maxima inferior a 70: '+str(notaMan), ln=True, align='L')
        pdfAplazados.cell(0,10,"* Cantidad de estudiantes reprobados en 2 examenes: "+str(conta2), ln=True, align='L')
        pdfAplazados.cell(0,10,"* Cantidad de estudiantes reprobados en 3 examenes: "+str(conta3), ln=True, align='L')
        pdfAplazados.output('reporteAplazados.pdf')                                                  # Se crea el PDF.

        return print("El reporte de las notas fue creado exitosamente.\n" \
                    "Puede acceder a él mediante el archivo ""reporteAplazados"", ubicado en esta misma carpeta.")
    except PermissionError:
            os.system("cls")
            print("Debe cerrar el documento PDF para generar uno nuevo.")
            
