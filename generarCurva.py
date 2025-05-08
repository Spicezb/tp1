# Trabajo realizado Por Luis Guillermo Alfaro Chacón y Xavier Céspedes Alvarado.
# Fecha de inicio: 29/04/2025 a las 12:00
#
# Versión de python: 3.13.2
# Importación de libre
from reporteHTML import estilosCss
import pickle

def guardar(curvRepro, curvRepa, curvApro):
    curvarchivoReprovados="curvaReprovadosHTML.html"                   
    curvarchivoReposicion="curvaReposicionHTML.html"                      
    curvarchivoAprovados="curvaAprovadosHTML.html"
    archivos=[curvarchivoReprovados, curvarchivoReposicion, curvarchivoAprovados]
    codigos=[curvRepro, curvRepa,curvApro]
    for i in range(len(archivos)):          
        guardarHtml=open(archivos[i],"w",encoding="UTF-8")
        guardarHtml.write(str(codigos[i]))
        guardarHtml.close()

def agregarInfo(lista,cambio, pocern):
    for i in lista:
        for x in i:
            codigo=""
            if cambio==0:
                codigo+="        <tr class='tr1'>\n"
                cambio=1
            else:
                codigo+="        <tr>\n"
                cambio=0
            codigo+="            <td>"+str(lista[0][0])+"</td>\n"
            codigo+="            <td>"+str(lista[0][1])+" "+str(lista[0][2])+"</td>\n"
            codigo+="            <td>"+str(lista[1])+"</td>\n"
            codigo+="            <td>"+str(lista[2])+"</td>\n"
            codigo+="            <td>"+str(lista[3])+"</td>\n"
            codigo+="            <td>"+str(lista[4][:-1])+"</td>\n"
            codigo+="            <td>"+str(round(float(lista[4][-1])+(float(lista[4][-1]*(pocern/100))),2))+"</td>\n"
            return codigo

def curvaAprovado(archivo,lista, porcen):
# creación de variables.
    cambio1=0
    cambio2=0
    cambio3=0                                            # Se utiliza para el cambio de color de la tabla.
    abrirBD=open(archivo,"rb")                          # Se utiliza para abrir la información de la Base de Datos.
    lista = pickle.load(abrirBD)                        
    codCurvRepro="""
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte Estudiantes</title>
        <link rel="stylesheet" href="decorarHTML.css">
    </head>
	<body>
	<center><table>
	
        <tr>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Nombre</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Apellido</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Genero</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Carne</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Correo</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Notas</h3></td>
            <td class="subTitulos"><h3 style="margin: 0; padding: 0;">Curva</h3></td>
		</tr>\n"""
    codCurvRepo=codCurvRepro
    codCurvRepo+="<caption><h2>Estudiantes Reposicion</h2></caption>"
    codCurvApro=codCurvRepro
    codCurvApro+="<caption><h2>Estudiantes Aprobados</h2></caption>"
    codCurvRepro+="<caption><h2>Estudiantes Reprobados</h2></caption>"
    # Se le ingresa la información al reporte de los aprobadps.
    for i in lista:
        for x in i:
            if float(i[4][-1])+float(i[4][-1])*(porcen/100) < 60:
                codCurvRepro+=agregarInfo(i, cambio1, porcen)
                if cambio1 == 0:
                    cambio1=1
                else:
                    cambio1=0
                break
            elif float(i[4][-1])+float(i[4][-1])*(porcen/100) < 70:
                codCurvRepo+=agregarInfo(i, cambio2, porcen)
                if cambio2 == 0:
                    cambio2=1
                else:
                    cambio2=0
                break
            elif float(i[4][-1])+float(i[4][-1])*(porcen/100) > 70:
                codCurvApro+=agregarInfo(i, cambio3, porcen)
                if cambio3 == 0:
                    cambio3=1
                else:
                    cambio3=0
                break
    # Se guarda el codigo html dentro del documento.
    guardar(codCurvRepro,codCurvRepo,codCurvApro)
    return print("******************** Gestionar Curva ********************\nLos reporte de las curvas de notas fueron creados exitosamente.\n" \
                "Puede acceder a él mediante el archivo ""curvaAprobadosHTML"",""curvaReposicionHTML"",""curvaReprobadosHTML"", ubicado en esta misma carpeta.")