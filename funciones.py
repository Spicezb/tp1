# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# <<<<<<< HEAD
# # def agregarEstudiante(nombre,carnet,sede,genero,correo,apellidos):


# Importación de librerias
import names
import random
import pickle
# funciones
def crearCarne():
    return
def crearCarneAux(ini,fin):
    return crearCarne()
def crearCarneES(x):
    if x == True:
        print("Dijite el rango de años para generar los carnets")
        rango=input("Año inicial: ")
        rango2=input("Año final: ")
        return crearCarneAux(rango, rango2)
    else:
        return

def crearNombres():
    """
    Funcionamiento:
    Se crean nombres de manera aleatoria, gracias a la libreia names y random, donde se le asigna un genero al nombre,
    y se crea el nombre dependiendo del genero dado. Luego la informacion se almacena por separado.
    Entradas:
    N/A
    Salidas:
    Se retorna una lista con una tupla que contiene el nombre y los apellidos, y el genero por aparte, este de manera Booleana
    """
    nombrePersona=()
    infoPerso=[]
    genero=random.choice(("male","female"))
    persona=names.get_first_name(gender=genero)
    pA=names.get_last_name()
    sA=names.get_last_name()
    if genero=="male":
        genero = True
    else:
        genero= False
    nombrePersona = (persona, pA, sA)
    carne= crearCarne()
    correo= crearCorreo(True)
    notas= agregarNotas()
    infoPerso.append(nombrePersona)
    infoPerso.append(genero)
    return(infoPerso)

def crearBD(archivo,lista):
    lol=open(archivo,"wb")
    lista.append(crearNombres())
    pickle.dump(lista,lol)
    lol.close()
    return

def agregarEstudianteES():
    nombre="juan perez rojas"
    carnet="4321"
    # sede=
    # genero=
    correo=f"{nombre[0]}{nombre[nombre.find(" ")+1:nombre.find(" ",nombre.find(" ")+1)]}{carnet[-4:]}@estudiantec.cr"
    return correo

print(agregarEstudianteES())