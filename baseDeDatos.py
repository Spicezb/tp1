def pMenu():
    print("1. Crear BD dinámica\n" \
        "2. Registrar un estudiante\n" \
        "3. Generar reporte HTML y .csv \n" \
        "4. Respaldar en XML \n" \
        "5. Reporte por género (.docx) \n" \
        "6. Gestionar curva \n" \
        "7. Envió de correos para reposición. \n" \
        "8. Aplazados en al menos 2 exámenes (.pdf) \n" \
        "9. Estadística por generación \n" \
        "10. Reporte por sede con buen rendimiento. \n11. Salir")
    opcion = int(input("Opción: "))
    return opcion
def elegirOpcion():
    x=0
    while x != 11:
        x= pMenu()
    return "Hasta Luego. . ."
print(elegirOpcion())