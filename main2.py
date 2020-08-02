# Establecer la conexion a la base de datos
import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="",
     database="agenda"
)

# Para la creacion de la base de datos si no existe
def crear_base():
     
    cursor = None

    try:

        # crear la base de datos
        cursor = conn.cursor()
   
        cursor.execute("CREATE DATABASE IF NOT EXISTS agenda")

        # para comprobar que la base de datos existe
        cursor.execute("SHOW DATABASES")

        print("\n")
        print("###### Informacion de las bases de datos ######## \n",end="")
        print("\n")

        for bd in cursor:
            print(bd)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Se creo la base de datos exitosamente o ya existe......\n",end="")             

def crear_tabla():

    cursor = None

    try:

        cursor = conn.cursor()

        # Crear la tabla
        cursor.execute("CREATE TABLE IF NOT EXISTS libreta(" +
            "id int(10) auto_increment not null, " +
            "apellidos varchar(30) not null, " +
            "nombres varchar(30) not null, " +
            "direccion varchar(100) not null, " +
            "telefono varchar(10) not null, " +
            "email varchar(50) null, "
            "CONSTRAINT pk_libreta PRIMARY KEY(id)"
            ")")
        # verificar si la tabla se creo
        cursor.execute("SHOW TABLES")

        print("\n")
        print("##### Se verifica tabla creada ######\n",end="")
        print("\n")

        for tabla in cursor:
            print(tabla)
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Se creo la tabla exitosamente....!\n",end="")

def ingresar_datos(persona):

    cursor = None

    try:

        cursor = conn.cursor()

        # Ingresar datos a la tabla libreta
        cursor.executemany("INSERT INTO libreta(id,apellidos,nombres,direccion,telefono,email) " +
        "VALUES(null,%s,%s,%s,%s,%s)",persona)

        conn.commit()
        
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Se ingreso registros exitosamente....!\n",end="")

def consulta_registros():
    
    cursor = None

    try:

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libreta")

        registros = cursor.fetchall()

        for datos in registros:
            print("Id           :",datos[0])
            print("Apellidos    :",datos[1])
            print("Nombres      :",datos[2])
            print("Direccion    :",datos[3])
            print("Telefono     :",datos[4])
            print("Email        :",datos[5])
            print("\n")
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Consulta exitosamente...!\n",end="")

def borrar_registros():
    cursorcon = None
    cursoract = None
    codigo = None
  
    apellidos1 = input("Ingrese Apellidos a Eliminar : ")
    nombres1 = input("Ingrese nombres a Eliminar : ")
    
 
    try:

        cursorcon = conn.cursor()
        cursoract = conn.cursor()
        # Busca registro
        cadena1 = "SELECT * FROM libreta WHERE apellidos LIKE %s AND nombres LIKE %s"
        datos1 = (apellidos1,nombres1)

        cursorcon.execute(cadena1, datos1)
        # Mostrar registro
        registros = cursorcon.fetchall()

        for fila in registros:
            print("Id               :",fila[0])
            print("Apellidos        :",fila[1])
            print("Nombres          :",fila[2])
            print("Direccion        :",fila[3])
            print("Telefono         :",fila[4])
            print("Email            :",fila[5])
            print("\n")

        opcion1 = input("¿Esta Seguro eliminar Registro S/N : ")
        if opcion1 == 'S' or opcion1 == 's':

            print("\n")
            print("####### Se va a eliminar datos para actualizar ######\n",end="")
            print("\n")

            
            cadena = "DELETE FROM libreta WHERE apellidos = %s AND nombres = %s" 

            datos = (apellidos1, nombres1)
        
            cursoract.execute(cadena, datos)
        
            # Guardar los cambios
            conn.commit()
        else:
            print("No se procede a eliminar.....!\n",end="")    
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Fin de procedimiento.....!\n",end="")
   
    
def actualizar_registro():

    cursorcon = None
    cursoract = None
    codigo = None
  
    apellido1 = input("Ingrese Apellidos a buscar : ")
    nombres1 = input("Ingrese nombres a buscar : ")
    apellido2 = input("Ingrese Apellido a Corregir : ")
    nombre2 = input("Ingrese nombre a Corregir :")
    
 
    try:

        cursorcon = conn.cursor()
        cursoract = conn.cursor()
        # Busca registro
        cadena1 = "SELECT * FROM libreta WHERE apellidos LIKE %s AND nombres LIKE %s"
        datos1 = (apellido1,nombres1)

        cursorcon.execute(cadena1, datos1)
        # Mostrar registro
        registros = cursorcon.fetchall()

        for fila in registros:
            print("Id               :",fila[0])
            print("Apellidos        :",fila[1])
            print("Nombres          :",fila[2])
            print("Direccion        :",fila[3])
            print("Telefono         :",fila[4])
            print("Email            :",fila[5])
            print("\n")

        print("\n")
        print("####### Se va a ingresar datos para actualizar ######\n",end="")
        print("\n")

        codigo = int(input("Ingrese Codigo : "))

        cadena = "UPDATE libreta SET apellidos = %s, nombres = %s WHERE id = %s" 

        datos = (apellido2, nombre2, codigo)
     
        cursoract.execute(cadena, datos)
      
        # Guardar los cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            print("Se actualizo registro.....!\n",end="")
   
seguir = True

while seguir:
    crear_base()
    crear_tabla()
    #### menu principal
    print("\n")
    print("##### ###### menu principal ########\n",end="")
    print("\n")
    print("1.- Ingrese de datos automatizados por la computadora\n",end="")
    print("2.- Consulta de datos\n",end="")
    print("3.- Eliminacion de datos\n",end="")
    print("4.- Actualizacion de datos\n",end="")
    print("5.- Salir\n",end="")
    opcion = int(input("Digite su opcion 1-5 : "))

    verificar1 = isinstance(opcion,int)

    while not verificar1 or (opcion <= 0 or opcion > 5):
        opcion = int(input("Digite su opcion 1-5 : "))

    if opcion == 1:
        ape = input("Ingrese apellidos : ")
        nom = input("Ingrese nombres   : ")
        direccion = input("Ingrese Direccion : ")
        tele = input("Ingrese telefono : ")
        correo = input("Ingrese correo electronico : ")
        Persona = [(ape,nom,direccion,tele,correo)]
        ingresar_datos(Persona)
    if opcion == 2:
        consulta_registros()
    if opcion == 3:
        borrar_registros()
    if opcion == 4:
        actualizar_registro()
    if opcion == 5:
        seguir = False

