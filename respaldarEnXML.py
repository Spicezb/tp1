# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
# 
# Versión de python: 3.13.2
# Importación de librerias
import pickle
# funciones
def respaldoXML(archivo,lista):
    """
    Funcionamiento:
    - Crea un archivo en formato .xml, donde va a tener un respaldo de toda la información.
    Entradas:
    - archivo(str): contiene la información toda la información de la Base de Datos.
    - lista(lst): es la lista que se usa para almacenar la información de la Base de Datos.
    Salidas:
    - Retorna un print al usuario, indicándole que el respaldo se creó exitosamente y indicando dónde lo puede encontrar
    para poder acceder a él.
    """
    # Creación de variables.
    annoinicial=0                                    # Contiene el rango inicial de los años.
    annofinal=0                                      # Contiene el rango final de los años.
    archivoXML="respaldoXML.xml"                    # Nombre del archivo xml
    abrirBD=open(archivo,"rb")                      # Se utiliza para abrir la información de la Base de Datos.
    lista = pickle.load(abrirBD)
    # Define los rangos de años de las generaciones.
    for i in lista:
            if int(i[2][:4])>=annofinal:
                annofinal=int(i[2][:4])
            elif annoinicial==0:
                annoinicial=int(i[2][:4])
            elif int(i[2][:4])<annoinicial:
                annoinicial=int(i[2][:4])
    codigo='<?xml version="1.0" encoding="UTF-8"?>\n<Estudiantes>\n' # Se va escribiendo todo el codifo, dentro de esta variable código.
    for i in range(annoinicial, annofinal+1):
        codigo+="        <Generacion anno='"+str(i)+"'>\n"
        for t in lista:
            if int(t[2][:4]) == i:
                codigo+="                <Estudiante carne='"+t[2]+"'>\n"
                codigo+="                        <nombre>"+t[0][0]+t[0][1]+t[0][2]+"</nombre>\n"
                codigo+="                        <genero>"+str(t[1])+"</genero>\n"
                codigo+="                        <correo>"+t[3]+"</correo>\n"
                codigo+="                        <notas>"+str(t[4][:-1])+"</notas>\n"
                codigo+="                </Estudiante>\n"
        codigo+="        </Generacion>\n"
    codigo+="</Estudiantes>"
    # Se guarda el codigo xml dentro del documento.
    ol=open(archivoXML,"w", encoding="UTF-8")
    ol.write(codigo)
    ol.close()
    return print("El respaldo de la información fue creado exitosamente...\n" \
                "Puede ingresar a el mediante el archivo respaldoXML, ubicado en esta misma carpeta.")