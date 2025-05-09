# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Importación de librerias
from funciones import *
from respaldarEnXML import *
from reporteHTML import *
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
            
            if not re.match(r"^(11|10|2|3|4|5|6|7|8|9|1)$",opcion):     #Creo que se puede quitar el ^
                raise ValueError
            os.system("cls")
            return opcion
        except ValueError:
            os.system("cls")
            print("Debe ingresar una opción válida.")
            input("Presione enter para continuar.")
            os.system("cls")

def elegirOpcion(archivo,lista):
    x=0
    p1,p2,p3=notas()
    while x != "11":
        x= pMenu()
        if x=="1":
            crearBD(archivo,p1,p2,p3)
            input("Presione enter para continuar.")
        elif x=="2":
            agregarEstudiante(archivo,p1,p2,p3)
            input("Presione enter para continuar.")
        elif x=="3":
            estilosCss()
            reporteHTML(archivo,lista)
            input("Presione enter para continuar.")
        elif x=="4":
            respaldoXML(archivo,lista)
            input("Presione enter para continuar.")
        elif x=="5":
            reporteGenero(archivo,p1,p2,p3)
            input("Presione enter para continuar.")
        elif x =="6":
            curvasHtml(archivo,lista)
            input("Presione enter para continuar.")
        elif x =="8":
            estilosCss()
            reporteHTML(archivo,lista)
            input("Presione enter para continuar.")
    return "Hasta Luego. . ."

nomArchivo="baseDeDatos"
lstBD=[]
print(elegirOpcion(nomArchivo,lstBD))

