import pickle

def estilosCss():
    ol="decorarHTML.css"
    codigo="""
        body{
        background: #FFC90E;
        }
        table {
            border: solid 2px black;
            background: #FFFFFF;
            font-family: Arial;
            color: #FFFFFF;
            text-align: center;
            vertical-align: middle;
            }
        caption{
            background: #0080B8;
            border: solid 2px black;
            }
        td {
            border: solid 2px black;
            padding: 7px 40px;
            }
        .tr1 {
            background: #0080B8;
            }
        tr {
            background: #00425E;
            }
            """
    guardar=open(ol,"w")
    guardar.write(codigo)
    guardar.close()
    return

def reporteHTML(archivo,lista):
    cambio=0
    f=open(archivo,"rb")
    lista = pickle.load(f)
    abrir="reporteHTML.html"
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
            <td>Nombre</td>
            <td>Apellido</td>
            <td>Genero</td>
            <td>Carne</td>
            <td>Correo</td>
            <td>Notas</td>
            <td>Estado</td>
		</tr>\n"""
    for i in lista:
        if cambio==0:
            codigo+="        <tr class='tr1'>\n"
            cambio=1
        else:
            codigo+="        <tr>\n"
            cambio=0
        codigo+="            <td>"+str(i[0][0])+"</td>\n"
        codigo+="            <td>"+str(i[0][1])+str(i[0][2])+"</td>\n"
        for x in range(1,len(i)):
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
    codigo+="        </tr>\n"
    codigo+="	</center></table>"
    ol=open(abrir,"w",encoding="UTF-8")
    ol.write(codigo)
    ol.close()
