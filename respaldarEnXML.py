import pickle
def respaldoXML(archivo,lista):
    primerAnne=0
    ultimo=0
    f=open(archivo,"rb")
    lista = pickle.load(f)
    for i in lista:
            if int(i[2][:4])>=ultimo:
                ultimo=int(i[2][:4])
            elif primerAnne==0:
                primerAnne=int(i[2][:4])
            elif int(i[2][:4])<primerAnne:
                primerAnne=int(i[2][:4])
    abrir="respaldoXML.xml"
    codigo='<?xml version="1.0" encoding="UTF-8"?>\n<Estudiantes>\n'
    for i in range(primerAnne, ultimo+1):
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

    ol=open(abrir,"w", encoding="UTF-8")
    ol.write(codigo)
    ol.close()