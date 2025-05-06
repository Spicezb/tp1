# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Importación de libre
from reporteHTML import estilosCss
import pickle

def curvaAprovado(archivo,lista):
# creación de variables.
    cambio=0                                            # Se utiliza para el cambio de color de la tabla.
    abrirBD=open(archivo,"rb")                          # Se utiliza para abrir la información de la Base de Datos.
    lista = pickle.load(abrirBD)                        
    curvarchivoHtml="curvaHTML.html"                      # Nombre del archivo .html.
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
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Curva</h3></td>
		</tr>\n"""
    # Se le ingresa la información al reporte.
    for i in lista:
        for x in i:
            print("Hola", i[4][-2])
            if float((i[4][-1])) < 60:
                if cambio==0:
                    codigo+="        <tr class='tr1'>\n"
                    cambio=1
                else:
                    codigo+="        <tr>\n"
                    cambio=0
                codigo+="            <td>"+str(i[0][0])+"</td>\n"
                codigo+="            <td>"+str(i[0][1])+str(i[0][2])+"</td>\n"
                codigo+="            <td>"+str(i[1])+"</td>\n"
                codigo+="            <td>"+str(i[2])+"</td>\n"
                codigo+="            <td>"+str(i[3])+"</td>\n"
                codigo+="            <td>"+str(i[4][:-1])+"</td>\n"
                codigo+="            <td>"+str(float(i[4][-1])+(float(i[4][-1]*(3/100))))+"</td>\n"
                break
                
    # Se guarda el codigo html dentro del documento.
    guardarHtml=open(curvarchivoHtml,"w",encoding="UTF-8")
    guardarHtml.write(codigo)
    guardarHtml.close()
    return print("El reporte de las notas fue creado exitosamente.\n" \
                "Puede acceder a él mediante el archivo ""reporteHTML"", ubicado en esta misma carpeta.")