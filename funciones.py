# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# <<<<<<< HEAD
# # def agregarEstudiante(nombre,carnet,sede,genero,correo,apellidos):


# Importación de librerias
import names
import re
import random
import pickle
# funciones
def crearNotas(x1,x2,x3):
    if x1+x2+x3 !=100:
        print("no se puede")
    x=random.randint(1, 100)
    d=random.randint(1, 100)
    l=random.randint(1, 100)
    w=(round(x*x1/100,2)+round(d*x1/100,2)+round(l*x1/100,2))
    y=w
    tupla=(x,d,l,w,w)
    return tupla

def crearCorreo(nombre,carne):
    correo =nombre[0][:1]+nombre[1]+carne[6:]+"@estudiantec.cr"
    return correo.lower()

def crearCarne(ini, fin):
    rand=str(random.randint(0000,9999))
    while not re.match(r"\d{4}",rand):
        rand="0"+rand
    carnet=str(random.randint(ini,fin))+random.choice(["01","02","03","04","05","06"])+rand
    return carnet

def crearCarneAux(ini,fin):
    return crearCarne(ini,fin)

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
    nombrePersona=""
    genero=random.choice(("male","female"))
    persona=names.get_first_name(gender=genero)
    pA=names.get_last_name()
    sA=names.get_last_name()
    if genero=="male":
        genero = True
    else:
        genero= False
    nombrePersona = f"{persona},{pA},{sA},{genero}\n"
    return nombrePersona

def llenarBD(r,r2,x1,x2,x3):
    infoPerso=[]
    carne= crearCarneAux(r,r2)
    correo = crearCorreo(nombrePersona,str(carne))         # nombrePersona no est{a definido, ni genero
    notas= crearNotas(x1,x2,x3)
    infoPerso.append(nombrePersona)
    infoPerso.append(genero)
    infoPerso.append(carne)
    infoPerso.append(correo)
    infoPerso.append(notas)
    return(infoPerso)

def crearBD(archivo,lista):
    jamal=[]
    lol=open(archivo,"wb")
    cantidadCrear=int(input("Digite la cantidad de de estudiantes a crear: "))
    porcentaje=int(input("Digite el porcentaje a agregar de las fuentes: "))
    """    print("Dijite el rango de años para generar los carnets")
    rango=int(input("Año inicial: "))
    rango2=int(input("Año final: "))
    x1=int(input("Indique el porcentaje de la primer evaluacion:"))
    x2=int(input("Indique el porcentaje de la segundo evaluacion:"))
    x3=int(input("Indique el porcentaje de la tercer evaluacion: "))"""

    txtNombresGenerados=open("Nombres.txt","w")
    for i in range(cantidadCrear):
        txtNombresGenerados.write(crearNombres())
    txtNombresGenerados.close

    txtNombresGenerados=open("Nombres.txt","r")
    for i in range(cantidadCrear):
        linea=(txtNombresGenerados.readline())
        alput=tuple(linea.strip().split(","))
        jamal.append(alput)
    print(jamal)
    print(random.sample(jamal,porcentaje))
    txtNombresGenerados.close

    print(abrir())
    pickle.dump(lista,lol)
    lol.close()
    return

def abrir2():
    ansuu=[]
    estudi=open("estudiantes.txt","r")
    for i in range(4):
        linea=(estudi.readline())
        tupla=tuple(linea.strip().split(","))
        ansuu.append(tupla)
    print(ansuu)
    return

def abrir():
    asnu=[]
    estu=open("Nombres.txt","r")
    for i in range(4):
        linea=(estu.readline())
        tupla=tuple(linea.strip().split(","))
        asnu.append(tupla)
    print(asnu)

def agregarEstudianteES():
    nombre="juan perez rojas"
    carnet="4321"
    # sede=
    # genero=
    correo=crearCorreo
    return correo

print(agregarEstudianteES())