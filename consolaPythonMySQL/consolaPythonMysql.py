import funciones

"""Muestra el menú principal y maneja la entrada del usuario."""
conexion = funciones.connect()

if conexion.is_connected():
    print("Conectado a la base de datos.")
    
    while True:
        print("\n--- Menú ---")
        print("1. Crear registro")
        print("2. Leer registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            funciones.crear_registro(conexion)
        elif opcion == '2':
            funciones.leer_registro(conexion)    
        elif opcion == '2':
            funciones.actualizar_registro(conexion)
        elif opcion == '3':
            funciones.eliminar_registro(conexion)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

    conexion.close()
    print("Conexión cerrada.")
else:
    print("Error al conectar a la base de datos.")