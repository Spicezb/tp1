import pickle
def reporteHTML(archivo,lista):
    f=open(archivo,"rb")
    lista = pickle.load(f)
    abrir="reporteHTML.html"
    codigo="""
    <html>
    <head>
        <title>Reporte</title>
		<style>
			table {
				border: solid 2px black;
				}
			caption{
				border: solid 2px black;
				}
			td {
				border: solid 2px black;
				padding: 7px 40px;
				}
		</style>
    </head>
	<body>
	<center><table>
	<caption><h2><font face="Arial">Detalle de notas</h2></caption>
        <tr>
            <td><font face="Arial">Nombre</td>
            <td><font face="Arial">Apellido</td>
            <td><font face="Arial">Genero</td>
            <td><font face="Arial">Carne</td>
            <td><font face="Arial">Correo</td>
            <td><font face="Arial">Notas</td>
            <td><font face="Arial">Estado</td>
		</tr>\n"""

    for i in lista:
        codigo+="        <tr>\n"
        for x in i:
            codigo+="            <td><font face=""Arial"">"+str(x)+"</td>\n"
        codigo+="        </tr>\n"
    codigo+="	</center></table>"

    ol=open(abrir,"w")
    ol.write(codigo)
    ol.close()

