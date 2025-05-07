# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# SE DEBE DE INSTALAR LA LIBRÍA NAMES!!!!

# Importación de librerias
import names 
import re
import random
import pickle
from reporteHTML import *
from respaldarEnXML import *
from aplazados import *
from generarCurva import *

# funciones
def crearNotas(x1,x2,x3):
    if x1+x2+x3 !=100:
        print("Los tres rubros a evaluar deben sumar 100.")  #hacer la validacion en el input
    x=random.randint(1, 100)
    d=random.randint(1, 100)
    l=random.randint(1, 100)
    w=round((x*x1/100)+(d*x1/100)+(l*x1/100),2)
    tupla=(x,d,l,w,w)
    return tupla
# Crea el correo
def crearCorreo(nombre,carne):
    correo =nombre[0][:1]+nombre[1]+carne[6:]+"@estudiantec.cr"
    return correo.lower()
# Crea el Carnet
def crearCarne(ini, fin):
    rand=str(random.randint(0000,9999))
    while not re.match(r"\d{4}",rand):
        rand="0"+rand
    carnet=str(random.randint(ini,fin))+random.choice(["01","02","03","04","05","06"])+rand
    return str(carnet)

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
# Crea las personas y las envia para meterlas a la base de datos
def llenarBD(nomb,r,r2,x1,x2,x3):
    infoPerso=[]
    nombre=(nomb[0],nomb[1],nomb[2])
    genero=nomb[3]
    if genero == "Masculino" or genero == "True":
        genero=True
    else:
        genero=False
    carne= crearCarneAux(r,r2)
    correo = crearCorreo(nombre,str(carne))         
    notas= crearNotas(x1,x2,x3)
    infoPerso.append(nombre)
    infoPerso.append(genero)
    infoPerso.append(carne)
    infoPerso.append(correo)
    infoPerso.append(notas)
    return(infoPerso)

def generaciones():
    rango=int(input("Año inicial: "))
    rango2=int(input("Año final: "))
    return (rango,rango2)
# Crea la base de datos
def crearBD(archivo,lista):
    lstnombsconv=[]
    lol=open(archivo,"wb")
    cantidadCrear=int(input("Digite la cantidad de de estudiantes a crear: "))
    porcentaje=int(input("Digite el porcentaje a agregar de las fuentes: "))
    print("Dijite el rango de años para generar los carnets")
    rangos=generaciones()
    x1=int(input("Indique el porcentaje de la primer evaluacion:"))
    x2=int(input("Indique el porcentaje de la segundo evaluacion:"))
    x3=int(input("Indique el porcentaje de la tercer evaluacion: "))
    #Creo el archivo de nombres
    txtNombresGenerados=open("Nombres.txt","w")
    for i in range(cantidadCrear):
        txtNombresGenerados.write(crearNombres())
    txtNombresGenerados.close()
    if ((porcentaje/100)*cantidadCrear)%1 >= 0.5:
        redondeado=((porcentaje/100)*cantidadCrear)+(((porcentaje/100)*cantidadCrear)%1)-1
    else:
        redondeado=((porcentaje/100)*cantidadCrear)-((porcentaje/100)*cantidadCrear)%1
    #Extrae los nombres de los archivos
    nombresArchivo=escogerDeArchiNom(int(redondeado),lstnombsconv)
    nombresArchivo=escogerDeArchiEstu(porcentaje,lstnombsconv)
    for i in range(len(nombresArchivo)):
        lista.append(llenarBD(nombresArchivo[i],rangos[0],rangos[1], x1,x2,x3))
    pickle.dump(lista,lol)
    lol.close()
    return "Base de datos creada y llenada . . ."

def escogerDeArchiEstu(porcentaje,list):
    conta=0
    estudi=open("estudiantes.txt","r",encoding="utf-8")
    for i in estudi:
        conta+=1
    if ((porcentaje/100)*conta)%1 >= 0.5:
        conta=((porcentaje/100)*conta)+(((porcentaje/100)*conta)%1)-1
    else:
        conta=((porcentaje/100)*conta)-((porcentaje/100)*conta)%1
    estudi.close()
    estudi=open("estudiantes.txt","r",encoding="utf-8")
    lineas=estudi.readlines()
    for i in range(int(conta)):
        x=random.sample(lineas,1)
        linea=(x[0])
        tupla=tuple(linea.strip().split(","))
        list.append(tupla)
        print(tupla)
    estudi.close()
    return list

def escogerDeArchiNom(porcentaje,lis):
    estu=open("Nombres.txt","r")
    for i in range(int(porcentaje)):
        linea=(estu.readline())
        tupla=tuple(linea.strip().split(","))
        print(tupla)
        lis.append(tupla)
    estu.close()
    return lis

def agregarEstudiante(archivo,x1,x2,x3):
    """
    Funcionamiento:
    - Recibe la información del estudiante mediante inputs y lo agrega a la base de datos.
    Entradas:
    - x1,x2,x3(int): Son los porcentajes que vale cada rubro para asignar las notas. 
    """
    while True:
        try:
            nombre = tuple(input("Ingrese el nombre del estudiante con sus dos apellidos:\n").split(" "))
            if len(nombre)!=3:
                raise ValueError("Tiene que ingresar un nombre con dos apellidos.\n")
            genero = input("Indique el género del estudiante:\n1. Femenino\n2. Masculino")
            if genero not in ("1","2"):
                raise ValueError("Debe escoger una de las dos opciones.\n")
            gen = int(input("Indique la generación del estudiante:\n"))
            if len(str(gen))!=4:
                raise ValueError("La generación debe ser un año de 4 dígitos.\n")
            break
        except ValueError as e:
            print(e)
    carne = crearCarne(gen,gen)
    correo = crearCorreo(nombre,carne)
    notas = crearNotas(x1,x2,x3)
    if genero == "1":
        genero = False
    else:
        genero = True
    estudiante = [nombre,genero,carne,correo,notas]
    base=open(archivo,"rb")
    lista=pickle.load(base)
    lista.append(estudiante)
    base.close()
    nuevaBase=open(archivo,"wb")
    pickle.dump(lista,nuevaBase)
    nuevaBase.close()
    return "El estudiante ha sido agregado."

def html(archivo,lista):
    estilosCss()
    reporteHTML(archivo,lista)

def respaldar(archivo,lista):
    return respaldoXML(archivo,lista)

def obtenerNota(i):
    return i[4][4] 

def reporteGenero(archivo,x1,x2,x3):
    contadorHombres=0
    contadorMujeres=0
    mujeres=open("mujeres.docx", "w")
    mujeres.write("Reporte de Notas Mujeres\n\n")
    hombres=open("hombres.docx", "w")
    hombres.write("Reporte de Notas Hombres\n\n")
    base=open(archivo,"rb")
    personas = pickle.load(base)
    personas.sort(key=obtenerNota,reverse=True)
    for i in personas:
        if i[1]==False:
            contadorMujeres+=1
            mujeres.write(f"{i[4][4]}, {i[4][0]} {i[4][1]} {i[4][2]}, {i[0][0]} {i[0][1]} {i[0][2]}, {i[2]}, {i[3]}\n")
        else:
            contadorHombres+=1
            hombres.write(f"{i[4][4]}, {i[4][0]} {i[4][1]} {i[4][2]}, {i[0][0]} {i[0][1]} {i[0][2]}, {i[2]}, {i[3]}\n")
    mujeres.write(f"\nLos porcentajes de cada evaluación fueron {x1}, {x2} y {x3} respectivamente, y la cantidad de mujeres es {contadorMujeres}.")
    hombres.write(f"\nLos porcentajes de cada evaluación fueron {x1}, {x2} y {x3} respectivamente, y la cantidad de hombres es {contadorHombres}.")
    base.close()
    hombres.close()
    mujeres.close()
    return ""

def reporteGeneracion(archivo):
    apTotales=0
    rpTotales=0
    reTotales=0
    gens=[]
    gensFinal=[]
    base=open(archivo,"rb")
    lista=pickle.load(base)
    for i in lista:
        if i[2][:4] not in gens:
            gens.append(int(i[2][:4]))
    gens.sort()
    for i in gens:
        gensFinal.append([0,0,0])
    for i in lista:
        if i[4][4]>=70:
            gensFinal[gens.index(int(i[2][:4]))][0]+=1
        elif 60<=i[4][4]<70:
            gensFinal[gens.index(int(i[2][:4]))][1]+=1
        else:
            gensFinal[gens.index(int(i[2][:4]))][2]+=1
    print("Generación\tAprobados\tReposición\tRebrobados\tTotales")
    for i in range(len(gens)):
        print(f"   {gens[i]}\t\t    {gensFinal[i][0]}\t\t    {gensFinal[i][1]}\t\t    {gensFinal[i][2]}\t\t   {gensFinal[i][0]+gensFinal[i][1]+gensFinal[i][2]}")
        apTotales+=gensFinal[i][0]
        rpTotales+=gensFinal[i][1]
        reTotales+=gensFinal[i][2]
    total = apTotales+rpTotales+reTotales
    print(f"  Totales\t    {apTotales}\t\t    {rpTotales}\t\t    {reTotales}\t\t   {total}")
    return""

def curvasHtml(archivo, lista):
    porcentaje=int(input("Ingrese el porcentaje de curva a aplicar: "))
    return curvaAprovado(archivo, lista, porcentaje)

def examenPdf(archivo, lista):
    crearPDF(archivo, lista)
    return 