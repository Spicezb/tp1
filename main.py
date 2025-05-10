# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2

# Importación de librerias
from funciones import *
from respaldarEnXML import *
from reporteHTML import *
from reporteCVS import *
import os 
import re

def pMenu():
    """
    Funcion: es un print con el menu
    """
    while True:
        try:
            os.system("cls")
            print("1. Crear BD dinámica\n" \
                "2. Registrar un estudiante\n" \
                "3. Generar reporte HTML y .csv \n" \
                "4. Respaldar en XML \n" \
                "5. Reporte por género (.docx) \n" \
                "6. Gestionar curva \n" \
                "7. Envió de correos para reposición. \n" \
                "8. Aplazados en al menos 2 exámenes (.pdf) \n" \
                "9. Estadística por generación \n" \
                "10. Reporte por sede con buen rendimiento. \n11. Salir")
            opcion = input("Opción: ")
            
            if not re.match(r"^(11|10|2|3|4|5|6|7|8|9|1)$",opcion):
                raise ValueError
            os.system("cls")
            return opcion
        except ValueError:
            os.system("cls")
            print("Debe ingresar una opción válida.")
            input("Presione enter para continuar.")
            os.system("cls")

def elegirOpcion(archivo,lista,sedes):
    x=0
    while x != "11":
        x= pMenu()
        if x=="1":
            crearBD(archivo)
            input("Presione enter para continuar.")
        elif x=="2":
            if comprobarBD(archivo) == True:
                print(agregarEstudianteAux(archivo))
            input("Presione enter para continuar.")
        elif x=="3":
            if comprobarBD(archivo) == True:
                estilosCss()
                reporteHTML(archivo,lista)
                crearReporteCVS(archivo,lista)
            input("Presione enter para continuar.")
        elif x=="4":
            if comprobarBD(archivo) == True:
                respaldoXML(archivo,lista)
            input("Presione enter para continuar.")
        elif x=="5":
            if comprobarBD(archivo) == True:
                reporteGenero(archivo)
            input("Presione enter para continuar.")
        elif x =="6":
            if comprobarBD(archivo) == True:
                curvasHtml(archivo,lista)
            input("Presione enter para continuar.")
        elif x == "7":
            if comprobarBD(archivo) == True:
                print(enviarCorreosAux(archivo))
            input("Presione enter para continuar.")
        elif x =="8":
            if comprobarBD(archivo) == True:
                crearPDF(archivo, lista)
            input("Presione enter para continuar.")
        elif x =="9":
            if comprobarBD(archivo) == True:
                reporteGeneracion(archivo)
            input("Presione enter para continuar.")
        elif x =="10":
            if comprobarBD(archivo) == True:
                reporteBuenRendimiento(archivo,sedes)
            input("Presione enter para continuar.")
    return "Hasta Luego. . ."

nomArchivo="baseDeDatos"
lstBD=[]
sedes="sedes.txt"
print(elegirOpcion(nomArchivo,lstBD,sedes))