correoOriginal = input("Ingresa tu correo electrónico: ")
nombreUsuario, _ = correoOriginal.split('@')
nuevoCorreo = nombreUsuario + '@ceu.es'
print("Tu nuevo correo electrónico es:", nuevoCorreo)
