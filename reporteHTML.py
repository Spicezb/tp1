# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Importación de librerias
import pickle
# funciones
def estilosCss():
    """
    Funcionamiento:
    - Crea un archivo en formato .css, donde se le va a guardar las configuraciones del diseño del HTML.
    Entradas:
    N/A.
    Salidas:
    - Retorna True al crearse existosamente, pero este no se va a necesitar en ninguna parte.
    """
    # Creación de variables
    archivoCss="decorarHTML.css"    # Nombre del archivo .css.
    codigoCss="""                   
        body{
        background: #FFC90E;
        }
        table {
            border: solid 2px black;
            background: #FFFFFF;
            font-family: Arial;
            color: #FFFFFF;
            text-align: center;
            }
        caption{
            background: #0080B8;
            border: solid 2px black;
            }
        .subTitulos{
        font-weight: bold;
        font-style: italic;  
        text-align: center;  
        margin: 0;           
        color: white;
        }
        td {
            border: solid 2px black;
            padding: 7px 40px;
            }
        .tr1 {
            background: #0080B8;
            border: solid 2px black;
            }
        tr {
            background: #00425E;
            border: solid 2px black;
            }
            """
    # Se guarda el codigo css dentro del documento.
    guardar=open(archivoCss,"w")
    guardar.write(codigoCss)
    guardar.close()
    return True

def reporteHTML(archivo,lista):
    """
    Funcionamiento:
    - Crea un archivo en formato .html, donde se le va a tener el codigo del reporte de las Notas.
    Entradas:
    - archivo(str): contiene la información toda la información de la Base de Datos.
    - lista(lst): es la lista que se usa para almacenar la información de la Base de Datos.
    Salidas:
    - Retorna un print al usuario, indicándole que el reporte se creó exitosamente y indicando dónde lo puede encontrar
    para poder acceder a él.
    """
    # creación de variables.
    cambio=0                                            # Se utiliza para el cambio de color de la tabla.
    abrirBD=open(archivo,"rb")                          # Se utiliza para abrir la información de la Base de Datos.
    lista = pickle.load(abrirBD)                    
    archivoHtml="reporteHTML.html"                      # Nombre del archivo .html.
    codigo="""
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte</title>
        <link rel="stylesheet" href="decorarHTML.css">
    </head>
	<body>
	<center><table>
	<caption><h2>Detalle de notas</h2></caption>
        <tr>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Nombre</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Apellido</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Genero</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Carne</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Correo</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Notas</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Estado</h3></td>
		</tr>\n"""
    # Se le ingresa la información al reporte.
    for i in lista:
        if cambio==0:
            codigo+="        <tr class='tr1'>\n"
            cambio=1
        else:
            codigo+="        <tr>\n"
            cambio=0
        codigo+="            <td>"+str(i[0][0])+"</td>\n"
        codigo+="            <td>"+str(i[0][1])+" "+str(i[0][2])+"</td>\n"
        if i[1]==True:
            codigo+="            <td>Masculino</td>\n"
        else:
            codigo+="            <td>Femenino</td>\n"
        for x in range(2,len(i)):
            if i[x]==i[4]:
                codigo+='            <td>'+str(i[x][:-1])+'</td>\n'
                if float(i[x][-1])<60:
                    codigo+="            <td>Reprobado</td>\n"
                elif 60<=float(i[x][-1])<70:
                    codigo+="            <td>Reposicion</td>\n"
                else:
                    codigo+="            <td>Aprobado</td>\n"
                break
            codigo+="            <td>"+str(i[x])+"</td>\n"
    codigo+="        </tr>\n	</center></table>"
    # Se guarda el codigo html dentro del documento.
    guardarHtml=open(archivoHtml,"w",encoding="UTF-8")
    guardarHtml.write(codigo)
    guardarHtml.close()
    return print("******************** Reporte de notas ********************\nEl reporte de las notas fue creado exitosamente.\n" \
                "Puede acceder a él mediante el archivo ""reporteHTML"" o ""reporteCSV.csv"", ubicados en esta misma carpeta.")
