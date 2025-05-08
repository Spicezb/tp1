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
from docx import Document

def notas():
    while True:
        try:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            porce1=int(input("Indique el porcentaje de la primer evaluación: "))
            porce2=int(input("Indique el porcentaje de la segundo evaluación: "))
            porce3=int(input("Indique el porcentaje de la tercer evaluación: "))
            if porce1+porce2+porce3 != 100:
                raise TypeError
            return porce1,porce2,porce3
        except TypeError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("El porcentaje Total de las 3 evaluaciones debe de ser igual a 100%.\n" \
            f"La suma de los porcentajes ingresados es de: {str(porce1+porce2+porce3)}.\n"
            "Por favor, Ingrese nuevamente los porcentajes.")
            input("Presione enter para continuar.")
            os.system("cls")
        except ValueError:
            print("******************** Crear Base de Datos ********************")
            os.system("cls")
            print("Debe ingresar valores válidos. Por ejemplo:\n" \
            "Indique el porcentaje de la primer evaluación: 35")
            input("Presione enter para continuar.")
            os.system("cls")

# funciones
def crearNotas(porce1,porce2,porce3):
    evalu1=random.randint(1, 100)
    evalu2=random.randint(1, 100)
    evalu3=random.randint(1, 100)
    notaFinal=round((evalu1*porce1/100)+(evalu2*porce2/100)+(evalu3*porce3/100),2)
    tupla=(evalu1,evalu2,evalu3,notaFinal,notaFinal)
    return tupla
# Crea el correo
def crearCorreo(nombre,carne):
    correo=nombre[0][:1]+nombre[1]+carne[6:]+"@estudiantec.cr"
    correo=correo.lower()
    return correo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
# Crea el Carnet
def crearCarne(ini, fin):
    lista=[]
    txtSedes=open("sedes.txt","r")   #debería de cerrar el archivo
    x=txtSedes.readlines()
    for i in range(len(x)):
        lista.append("0"+str(i+1))           #le metí +! porque se estabn creando carnets con sede 00 y qué pasqa si hay más de nueve sedes en el archivo que use la profe para revisar?
    rand=str(random.randint(0000,9999))
    while not re.match(r"\d{4}",rand):
        rand="0"+rand
    carnet=str(random.randint(ini,fin))+random.choice(lista)+rand
    return str(carnet)

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
def llenarBD(nomb,r,r2,notas):
    infoPerso=[]
    nombre=(nomb[0],nomb[1],nomb[2])
    genero=nomb[3]
    if genero == "Masculino" or genero == "True":
        genero=True
    else:
        genero=False
    carne= crearCarne(r,r2)
    correo = crearCorreo(nombre,str(carne))         
    infoPerso.append(nombre)
    infoPerso.append(genero)
    infoPerso.append(carne)
    infoPerso.append(correo)
    infoPerso.append(notas)
    return(infoPerso)

def cantidadEstu():
    conta=1
    while True:
        try:
            print("******************** Crear Base de Datos ********************")
            cantidadCrear=int(input("Digite la cantidad de estudiantes a crear: "))
            break
        except ValueError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("Debe de ingresar una cantidad válida.\nPor ejemplo:\n" \
            "Digite la cantidad de estudiantes a crear: 120\n" \
            "Digite el porcentaje a agregar de las fuentes: 5\n")
            input("Presione enter para continuar.")
            os.system("cls")
    while True:
        try:
            if conta != 1:
                print("******************** Crear Base de Datos ********************")
                print("Digite la cantidad de estudiantes a crear: "+str(cantidadCrear))
                porcentaje=int(input("Digite el porcentaje a agregar de las fuentes: "))
            else:
                conta+=1
                porcentaje=int(input("Digite el porcentaje a agregar de las fuentes: "))
            break
        except ValueError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("Debe de ingresar una cantidad válida.\nPor ejemplo:\n" \
            "Digite la cantidad de estudiantes a crear: 120\n" \
            "Digite el porcentaje a agregar de las fuentes: 5\n")
            input("Presione enter para continuar.")
            os.system("cls")
    os.system("cls")
    return (cantidadCrear,porcentaje)

def generaciones():
    conta=1
    while True:
        try:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("Ingrese el rango de años para generar los carnets")
            rango=int(input("Año inicial: "))
            if not 999<rango<10000:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("El año no es válido, debe ingresar un año de 4 dígitos.\nPor ejemplo: 2022")
            input("Presione enter para continuar.")
            os.system("cls")
    while True:
        try:
            if conta != 1:
                os.system("cls")
                print("******************** Crear Base de Datos ********************")
                print("Ingrese el rango de años para generar los carnets")
                print("Año inicial: "+str(rango))
                rango2=int(input("Año final: "))
            else:
                conta+=1
                rango2=int(input("Año final: "))
            
            if rango>rango2:
                raise TypeError
            elif rango2>9999:
                raise ValueError
            break
        except ValueError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("El año no es válido, debe ingresar un año de 4 dígitos.\nPor ejemplo: 2024")
            input("Presione enter para continuar.")
            os.system("cls")
        except TypeError:
            os.system("cls")
            print("******************** Crear Base de Datos ********************")
            print("El año final no puede ser menor que el inicial.\nIngrese por ejemplo:\n" \
            "Año inicial: 2022\nAño final: 2024")
            input("Presione enter para continuar.")
            os.system("cls")
    return (rango,rango2)

# Crea la base de datos
def crearBD(archivo,lista,p1,p2,p3):      #Creo que se puede quitar lista de parámetro
    lista=[]
    lstnombsconv=[]
    lol=open(archivo,"wb")
    cantiDeEstu=cantidadEstu()
    rangos=generaciones()
    #Creo el archivo de nombres
    txtNombresGenerados=open("Nombres.txt","w")
    for i in range(cantiDeEstu[0]):
        txtNombresGenerados.write(crearNombres())
    txtNombresGenerados.close()
    if ((cantiDeEstu[1]/100)*cantiDeEstu[0])%1 >= 0.5:
        redondeado=((cantiDeEstu[1]/100)*cantiDeEstu[0])+(((cantiDeEstu[1]/100)*cantiDeEstu[0])%1)-1
    else:
        redondeado=((cantiDeEstu[1]/100)*cantiDeEstu[0])-((cantiDeEstu[1]/100)*cantiDeEstu[0])%1
    #Extrae los nombres de los archivos
    nombresArchivo=escogerDeArchiNom(int(redondeado),lstnombsconv)
    nombresArchivo=escogerDeArchiEstu(cantiDeEstu[1],lstnombsconv)
    for i in range(len(nombresArchivo)):
        lista.append(llenarBD(nombresArchivo[i],rangos[0],rangos[1], crearNotas(p1,p2,p3)))
    pickle.dump(lista,lol)
    lol.close()
    os.system("cls")
    print("******************** Crear Base de Datos ********************")
    print("Base de datos creada y llenada exitosamente.")
    return True

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
    estudi.close()
    return list

def escogerDeArchiNom(porcentaje,lis):
    estu=open("Nombres.txt","r")
    for i in range(int(porcentaje)):
        linea=(estu.readline())
        tupla=tuple(linea.strip().split(","))
        lis.append(tupla)
    estu.close()
    return lis

def agregarEstudiante(archivo,p1,p2,p3):
    base=open(archivo,"rb")
    lista=pickle.load(base)
    while True:
        try:
            carne=input("Ingrese el carné del estudiante o digite 0 para cancelar:\n")
            if carne=="0":
                return ""
            elif not re.match(r"\d{10}$",carne):
                raise ValueError
            for i in lista:
                for j in i:
                    if j==carne:
                        return f"El estudiante con el carné {carne} ya se encuentra registrado\n"
            break
        except ValueError:
            print("El carné debe de tener 10 dígitos.")
    while True:
        try:
            nombre = tuple(input("Ingrese el nombre del estudiante con sus dos apellidos o digite 0 para cancelar:\n").split(" "))
            if nombre=="0":
                return ""
            elif len(nombre)!=3:
                raise ValueError
            break
        except ValueError:
            print("Tiene que ingresar un nombre con dos apellidos.\n")
    while True:
        try:
            genero = input("Indique el género del estudiante:\n0.Cancelar\n1. Femenino\n2. Masculino\n")
            if genero not in ("1","2","0"):
                raise ValueError("Debe escoger una de las dos opciones.\n")
            elif genero=="0":
                return ""
            elif genero==1:
                genero=False
            else:
                genero=True
            break
        except:
            print("Debe escoger una de las dos opciones.\n")
    while True:
        try:
            correo=input("Ingrese el correo del estudiante o digite 0 para cancelar")
            if correo=="0":
                return ""
            if not re.match(r"\w+@estudiantec.cr$",correo):
                raise ValueError("El correo debe terminar en @estudiantec.cr")
            for i in lista:
                for j in i:
                    if j==correo:
                        raise ValueError("El correo ingresado ya se encuentra ocupado por otra persona, inténtelo de nuevo.\n")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            x1=int(input("Ingrese la nota obtenida por el estudiante en el primer rubro o digite 101 para cancelar: "))
            x2=int(input("Ingrese la nota obtenida por el estudiante en el segundo rubro o digite 101 para cancelar: "))
            x3=int(input("Ingrese la nota obtenida por el estudiante en el tercer rubro o digite 101 para cancelar: "))
            for i in (x1,x2,x3):
                if i==101:
                    return ""
                elif i>100 or i<0:
                    raise ValueError
            prom=round((x1*p1/100)+(x2*p2/100)+(x3*p3/100),2)
            nota=(x1,x2,x3,prom,prom)
            break
        except ValueError:
            print("Las notas deben estar entre 0 y 100.\n")
    estudiante = [nombre,genero,carne,correo,nota]
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
    mujeres = Document()
    mujeres.add_heading("Reporte de Notas Mujeres", level=1)
    mujeres.add_paragraph("")
    hombres = Document()
    hombres.add_heading("Reporte de Notas Hombres", level=1)
    hombres.add_paragraph("")
    base=open(archivo,"rb")
    personas = pickle.load(base)
    personas.sort(key=obtenerNota,reverse=True)
    for i in personas:
        linea=f"{str(i[4][4])}, {str(i[4][0])} {str(i[4][1])} {str(i[4][2])}, {i[0][0]} {i[0][1]} {i[0][2]}, {i[2]}, {i[3]}"
        if i[1]==False:
            contadorMujeres+=1
            mujeres.add_paragraph(linea)
        else:
            contadorHombres+=1
            hombres.add_paragraph(linea)
    mujeres.add_paragraph(f"\nLos porcentajes de cada evaluación fueron {x1}%, {x2}% y {x3}% respectivamente, y la cantidad de mujeres es {contadorMujeres}.")
    hombres.add_paragraph(f"\nLos porcentajes de cada evaluación fueron {x1}%, {x2}% y {x3}% respectivamente, y la cantidad de hombres es {contadorHombres}.")
    base.close()
    mujeres.save("mujeres.docx")
    hombres.save("hombres.docx")
    return "Los archivos fueron agregados a la carpeta"

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
    base.close()
    return""

def curvasHtml(archivo, lista):
    while True:
        try:
            os.system("cls")
            print("******************** Gestionar Curva ********************")
            porcentaje=int(input("Ingrese el porcentaje de curva a aplicar: "))
            os.system("cls")
            if not 0<porcentaje<100:
                raise TypeError
            return curvaAprovado(archivo, lista, porcentaje)
        except TypeError:
            print("******************** Gestionar Curva ********************")
            print("El porcentaje debe ser mayor a 0 y menor que 100.")
            input("Presione enter para continuar.")
            os.system("cls")
        except ValueError:
            os.system("cls")
            print("******************** Gestionar Curva ********************")
            print("Debe ingresar valores válidos. Por ejemplo:\n" \
            "Indique el porcentaje de curva a aplicar: 5")
            input("Presione enter para continuar.")
            os.system("cls")

def examenPdf(archivo, lista):
    os.system("cls")
    print("******************** Aplazados en al menos 2 rubros ********************")
    crearPDF(archivo, lista)
    return True