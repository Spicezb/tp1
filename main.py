# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Importación de librerias
from funciones import *
from reporteHTML import *
from respaldarEnXML import *
def pMenu():
    """
    Funcion: es un print con el menu
    """
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
    opcion = int(input("Opción: "))
    return opcion

def elegirOpcion(archivo,lista):
    x=0
    x1=1
    x2=1
    x3=1
    while x != 11:
        x= pMenu()
        if x==1:
            crearBD(archivo,lista)
        elif x==2:
            agregarEstudiante(archivo,lista,x1,x2,x3)
        elif x==3:
            html(archivo,lista)
        elif x==4:
            respaldoXML(archivo,lista)
    return "Hasta Luego. . ."

nomArchivo="baseDeDatos"
lstBD=[]
print(elegirOpcion(nomArchivo,lstBD))

