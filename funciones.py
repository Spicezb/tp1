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
def crearCorreo(nombre,carne):
    c =nombre[0][:1]+nombre[1]+carne[5:]+"@estudiantec.cr"
    return c.lower()

def crearCarne(ini, fin):
    print(ini)
    carnet=str(random.randint(ini,fin))+random.choice(["01","02","03","04","05","06"])+str(random.randint(000,999))
    return carnet
def crearCarneAux(ini,fin):
    return crearCarne(ini, fin)
def crearCarneES(x):
    if x == True:
        print("Dijite el rango de años para generar los carnets")
        rango=int(input("Año inicial: "))
        rango2=int(input("Año final: "))
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
    carne= crearCarneES(True)
    correo = crearCorreo(nombrePersona,carne)
    print(correo)
    #notas= agregarNotas()
    infoPerso.append(nombrePersona)
    infoPerso.append(genero)
    infoPerso.append(carne)
    infoPerso.append(correo)
    return(infoPerso)

def crearBD(archivo,lista):
    lol=open(archivo,"wb")
    x=int(input(""))
    lista.append(crearNombres())
    pickle.dump(lista,lol)
    lol.close()
    return

def agregarEstudianteES():
    nombre="juan perez rojas"
    carnet="4321"
    # sede=
    # genero=
    correo=crearCorreo
    return correo

print(agregarEstudianteES())