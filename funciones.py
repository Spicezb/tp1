# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Se debe instalar las librerías names, fpdf y python-docx

# Importación de librerias
import names 
import re
import random
import pickle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from respaldarEnXML import *
from aplazados import *
from generarCurva import *
from docx import Document
from datetime import datetime

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

def crearNotas(porce1,porce2,porce3):
    evalu1=random.randint(1, 100)
    evalu2=random.randint(1, 100)
    evalu3=random.randint(1, 100)
    notaFinal=round((evalu1*porce1/100)+(evalu2*porce2/100)+(evalu3*porce3/100),2)
    tupla=(evalu1,evalu2,evalu3,notaFinal,notaFinal)
    return tupla

def crearCorreo(nombre,carne):
    correo=nombre[0][:1]+nombre[1]+carne[6:]+"@estudiantec.cr"
    correo=correo.lower()
    return correo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

def crearCarne(ini, fin):
    lista=[]
    txtSedes=open("sedes.txt","r")         #debería cerrar el archivo     sea necio hp
    x=txtSedes.readlines()
    for i in range(len(x)):
        if i+1<10:
            lista.append("0"+str(i+1))
        else:
            lista.append(str(i+1))          #le metí +! porque se estabn creando carnets con sede 00 y qué pasqa si hay más de nueve sedes en el archivo que use la profe para revisar?
    rand=str(random.randint(0000,9999))
    while not re.match(r"\d{4}",rand):
        rand="0"+rand
    carnet=str(random.randint(ini,fin))+random.choice(lista)+rand
    txtSedes.close()
    return str(carnet)
# Crea el nombre de los estudiantes
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
    nombrePersona=""                                    # Se crea la variable que contendra el nombre creado.
    genero=random.choice(("male","female"))             # Se pide que escoja un genero para que cree los nombres basados a este género.
    persona=names.get_first_name(gender=genero)         # Se crea el nombre.
    primerApe=names.get_last_name()                     
    segundoApe=names.get_last_name()                    # Se crean los 2 apellifos
    if genero=="male":
        genero = True
    else:
        genero= False                                   # Al tener los generos en ingles, se pasan booleano para trabajar mejor.
    nombrePersona = f"{persona},{primerApe},{segundoApe},{genero}\n"    # Crea la información completa del nombre.
    return nombrePersona

# Se va llenando la base de datos con la informacion de cada persona.
def llenarBD(nomb,rango,rango2,notas):
    """
    Funcionamiento:
    - Se encarga de llenar la información de cada persona y retornala para ser agregada en la base de datos. 
    Entradas:
    - nomb(tuple): contiene el nombre, apellidos y genero de cada persona.
    - rango(int): contiene el año incial de los carnés.
    - rango2(int): contiene el año final de los carnés.
    - notas(tuple): contiene las notas aleatorias creadas por el sistema.
    Salidas:
    - Retorna la lista con la información de cada persona.
    """
    infoPerso=[]                                        # Lista con la información
    nombre=(nomb[0],nomb[1],nomb[2])                    # Se desgloza la tupla, para obtener el nombre y el apellido de la persona
    genero=nomb[3]                                      # Se obtiene el genero
    if genero == "Masculino" or genero == "True":
        genero=True                                     # Como la libreía names crea los generos en ingles, se igualan todos los generos a un valor Booleano.
    else:
        genero=False
    carne= crearCarne(rango,rango2)
    correo = crearCorreo(nombre,str(carne))         
    infoPerso.append(nombre)
    infoPerso.append(genero)                            # Se agregan todos los valores a la lista que llena la Base de datos.
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
def crearBD(archivo,porce1,porce2,porce3):
    """
    Funcionamiento:
    - Crea la base de Datos donde se va a estar almacenando la información del programa.
    Entradas:
    - archivo(str): contiene la información toda la información de la Base de Datos.
    - porce1: contiene el primer porcentaje de las evaluaciones.
    - porce2: contiene el primer porcentaje de las evaluaciones.
    - porce3: contiene el primer porcentaje de las evaluaciones.
    Salidas:
    - Retorna un True al realizar el proceso correctamente, pero este no se usa ni se ve en ninguna parte. Antes de el True, 
    si se le muestra al usuario que la Base de datos se creo correctamente.
    """
    # Definición de variables
    lista=[]                                        # Lista que va a almacenar la información.
    lstnombsconv=[]                                 # Lista que contiene los nombres de las 2 fuentes distintas.
    abrirAr=open(archivo,"wb")                      # Crea el archivo binario.
    cantiDeEstu=cantidadEstu()                      # Contiene la cantidad de estudiantes, dada por la funcion cantidadEstu.
    rangos=generaciones()                           # Contiene los rangos de las generaciones a crear.
    txtNombresGenerados=open("nombres.txt","w")     # Crea el archivo de nombres generados por el programa.
    # Se le crean los nombres aleatorios.
    for i in range(cantiDeEstu[0]):
        txtNombresGenerados.write(crearNombres())
    txtNombresGenerados.close()
    # Se da la cantidad de estudiantes a agregar de la fuente que nosotros creamos.
    nombresArchivo=escogerDeArchi("nombres.txt",cantiDeEstu[1],lstnombsconv)                                  # Se agregan los nombres creados por nosotros.
    nombresArchivo.extend(escogerDeArchi("estudiantes.txt",cantiDeEstu[1],lstnombsconv))                      # Se agregan los nombres de la fuente de estudiantes, dada por la profe.
    # Se agregan todos los elementos a la lista de la base de datos.
    for i in range(len(nombresArchivo)):
        lista.append(llenarBD(nombresArchivo[i],rangos[0],rangos[1], crearNotas(porce1,porce2,porce3)))
    pickle.dump(lista,abrirAr)
    abrirAr.close()
    os.system("cls")
    print("******************** Crear Base de Datos ********************")
    print("Base de datos creada y llenada exitosamente.")
    return True
# Da el porcentaje redondeado
def porcentajeDeEstudiantes(nombreArchivo,porcentaje):
    """
    Funcionamiento:
    - Indica el porcentaje de nombres que se debe de escoger de cada archivo.
    Entradas:
    - porcentaje (int): contiene la cantidad de porcentaje de estudiantes que se va a utilizar en las 2 fuentes.
    - nombreArchivo (str): contiene el nombre del archivo a usar. 
    Salidas:
    - Retorna el porcentaje real y redondeado de la cantidad de estudiantes a agregar dependiendo la fuente.
    """
    conta=0                                                                         # Lleva el conteo de las lineas del archivo.
    archivo=open(nombreArchivo, "r", encoding="utf-8")                              # Se abre el archivo correspondiente.
    for i in archivo:
        conta+=1                                                                    # Se obtiene la cantidad de lineas del archivo.
    if ((porcentaje/100)*conta)%1 >= 0.5:
        conta=((porcentaje/100)*conta)+(((porcentaje/100)*conta)%1)-1               # Operaciones para sacar el porcentaje.
    else:
        conta=((porcentaje/100)*conta)-((porcentaje/100)*conta)%1
    archivo.close()
    return conta
# Se escogen los nombres de los archivos.
def escogerDeArchi(nombreArchivo,porcentaje,lis):
    """
    Funcionamiento:
    - Escoge la cantidad de nombres según el porcentaje dado, desde el archivo correspondiente.
    Entradas:
    - nombreArchivo (str): contiene el nombre del archivo.
    - porcentaje (int): contiene el porcentaje de estudiantes que se va a utilizar en las 2 fuentes.
    - lis (list): lista que contiene información y la agrega a la base de datos. 
    Salidas:
    - Retorna la lista de los nombres que se escogieron aleatoriamente.
    """
    conta=porcentajeDeEstudiantes(nombreArchivo, porcentaje)                # Contiene la cantidad de estudiantes que hay que escoger.
    estudi=open(nombreArchivo,"r",encoding="utf-8")                         # Abre el contenido del archivo donde hay que sacar los nombres.
    lineas=estudi.readlines()
    estudiante=random.sample(lineas,int(conta))                             # Se saca un estudiante random, sin posibilidad de repetirse.(Esto por el random.sample, que escoge un valor
    for i in range(int(conta)):                                             # random único entre todas las lineas, n cantidad de veces, en este caso escoge conta cantidad de nombres unicos)
        tupla=tuple(estudiante[i].strip().split(","))                       # Se agrega uno por uno los estudiantes escogidos de forma aleatoria, el strip es para limpiar caracteres y   
        lis.append(tupla)                                                   # el split para separar las palabras cuando exite una coma.
    estudi.close()
    return lis

def agregarEstudiante(archivo,estudiante):
    base=open(archivo,"rb")
    lista=pickle.load(base)
    lista.append(estudiante)
    base.close()
    nuevaBase=open(archivo,"wb")
    pickle.dump(lista,nuevaBase)
    nuevaBase.close()
    return "El estudiante ha sido agregado."

def agregarEstudianteAux(archivo,p1,p2,p3):
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
            if nombre==("0"):
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
    base.close()
    nuevaBase=open(archivo,"wb")
    pickle.dump(lista,nuevaBase)
    nuevaBase.close()
    return "El estudiante ha sido agregado."

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
    return print("Los archivos fueron agregados a la carpeta")

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

def enviarCorreos(archivo,fecha,hora):
    base=open(archivo,"rb")
    lista=pickle.load(base)
    correoRemitente = "xaviccr@gmail.com"
    contrasenna = "tqge uhju oxon ibgu" #Es la contraseña que se utiliza para ingresar al correo.
    for i in lista:
        if 60<=i[4][4]<70:
            correoEstufechante = i[3]
            asunto = "Examen de reposición"
            mensaje = f"Se le comunica que usted deberá realizar un examen de reposición el día {fecha} a las {hora}"
            msg = MIMEMultipart()
            msg["From"] = correoRemitente
            msg["To"] = correoEstufechante
            msg["Subject"] = asunto
            msg.attach(MIMEText(mensaje, 'plain'))
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()
            servidor.login(correoRemitente,contrasenna)
            servidor.send_message(msg)
            servidor.quit()
    base.close()
    return "Los correos para reposición han sido enviados"

def enviarCorreosAux(archivo):
    """
    Funcionamiento:
    - Pide al usuario la fecha y la hora en la que se va a realizar el examen de reposición.
    """
    while True:
        try:
            fecha=input("Ingrese el día en que se va a realizar el examen de reposición con el formato dd/mm/aaaa:\n")
            if not re.match(r"^((0[1-9]|1\d|2\d)/(0[1-9]|1[0-2])|(30)/(0[1,3-9]|1[0-2])|31/(0[13578]|1[02]))/(\d{4})$",fecha):
                raise ValueError("La fecha no cumple con el formato requerido de dd/mm/aaaa, recuerde que el mes no puede ser mayor a 12 y que solo ciertos meses tienen 31 días.\n")
            elif int(fecha[0:2]) == 29 and int(fecha[3:5]) == 2:
                if not ((int(fecha[6:]) % 4 == 0 and int(fecha[6:]) % 100 != 0) or (int(fecha[6:]) % 400 == 0)):
                    raise ValueError("\nLa fecha no es válida, pues el año ingresado no es bisiesto\n")
            dia, mes, anno = int(fecha[:2]), int(fecha[3:5]), int(fecha[6:])
            if datetime(anno, mes, dia)<=datetime.now():
                raise ValueError("Debe ingresar una fecha posterior a la de hoy.\n")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            hora=input("Ingrese la hora en un formato de 24 horas, o sea, hh:mm:\n")
            if not re.match(r"^([01]\d|2[0-3]):[0-5]\d$",hora):
                raise ValueError
            break
        except ValueError:
            print("La hora no concuerda con el formato de 24 horas\n")
    return enviarCorreos(archivo,fecha,hora)

def reporteBuenRendimiento(archivo,sedes):
    """
    Funcionamiento:
    - Pide al usuario ingresar un número de sede e imprime los estudiantes de esa sede que obtuvieron notas mayores a 70.
    Entradas:
    - archivo: Es el archivo de la base de datos.
    - sedes: Es el archivo que contiene las sedes.
    Salidas: 
    - Imprime el nombre y el carné de los estudiantes.
    """
    codigos=[]
    estudiantes=[]
    base=open(archivo,"rb")
    lista=pickle.load(base)
    sedes=open(sedes,"r",encoding="utf-8")
    contador=0
    for i,linea in enumerate(sedes):
        print(f"Sede {i+1}, {linea}")    
        if len(str(i))==1 and i!=9:
            codigos.append(f"0{i+1}")
        else: 
            codigos.append(i+1)
    while True:
        try:
            sede=input("\nIngrese el número de la sede de la que desea generar el reporte:\n")
            if len(sede)==1:
                sede="0"+sede
            if sede not in codigos:
                raise ValueError
            break
        except ValueError:
            print("Tiene que digitar el código de una de las sedes antes mostradas.\n")
    for i in lista:
        if i[2][4:6] == sede:
            if i[4][0]>=70 and i[4][1]>=70 and i[4][2]>=70:
                contador+=1
                estudiante=f"{contador}. {i[0][0]} {i[0][1]} {i[0][2]}, {i[2]}"
                estudiantes.append(estudiante)
    if len(estudiantes)==0:
        print("\nNo existen estudiantes con buen rendimiento en dicha sede.\n")
    else:
        print("\nLos estudiantes que demostraron un buen rendimiento en la sede solicitada fueron:\n")
        for i in estudiantes:
            print(i)
    base.close()
    return ""
