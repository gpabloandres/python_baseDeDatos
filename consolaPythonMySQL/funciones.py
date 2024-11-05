import mysql.connector
from mysql.connector import Error

def connect():
    """Establece la conexión con la base de datos."""
    return mysql.connector.connect(
        host='localhost',
        user='root',         # Cambia a tu usuario de MySQL
        password='',   # Cambia a tu contraseña de MySQL
        database='test' # Cambia al nombre de tu base de datos
    )

def crear_registro(conexion):
    """Agrega un registro a la tabla."""
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el email: ")
    
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO users (user_name, email) VALUES (%s, %s)", (nombre_usuario, email))
    connection.commit()
    print("Registro agregado exitosamente.")
    cursor.close()

def leer_registro(conexion):
    """Muestra todos los registros de la tabla."""
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    
    if records:
        print("\n--- Registros en la tabla 'users' ---")
        for row in records:
            print(f"ID: {row[0]}, Nombre_usuario: {row[1]}, Email: {row[2]}")
    else:
        print("No hay registros en la tabla.")
    
    cursor.close()

def actualizar_registro(conexion):
    """Edita un registro en la tabla."""
    registro_id = int(input("Ingrese el ID del registro que desea editar: "))
    nuevo_nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
    nuevo_email = input("Ingrese el nuevo email: ")
    
    cursor = conexion.cursor()
    cursor.execute("UPDATE users SET user_name = %s, email = %s WHERE id = %s", (nuevo_nombre_usuario, nuevo_email, registro_id))
    conexion.commit()
    print("Registro actualizado exitosamente.")
    cursor.close()

def eliminar_registro(conexion):
    """Elimina un registro de la tabla."""
    registro_id = int(input("Ingrese el ID del registro que desea eliminar: "))
    
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (registro_id,))
    conexion.commit()
    print("Registro eliminado exitosamente.")
    cursor.close()