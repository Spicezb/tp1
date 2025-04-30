# def agregarEstudiante(nombre,carnet,sede,genero,correo,apellidos):


def agregarEstudianteES():
    nombre="juan perez rojas"
    carnet="4321"
    # sede=
    # genero=
    correo=f"{nombre[0]}{nombre[nombre.find(" ")+1:nombre.find(" ",nombre.find(" ")+1)]}{carnet[-4:]}@estudiantec.cr"
    return correo

print(agregarEstudianteES())

