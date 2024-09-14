def validar_contraseña(contraseña):
    # Definir criterios
    longitud_minima = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    caracteres_especiales = "!@#$%^&*()-_+=<>?/{}[]|\\"

    # Verificar la longitud mínima
    if len(contraseña) < longitud_minima:
        return False

    # Iterar sobre cada caracter de la contraseña
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True

    # Verificar si cumple con todos los criterios
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False

# Solicitar al usuario que ingrese una contraseña
contraseña_usuario = input("Por favor, ingrese una contraseña: ")

# Validar la contraseña ingresada
if validar_contraseña(contraseña_usuario):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida. Asegúrate de que tenga al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial.")