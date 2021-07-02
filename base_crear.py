import mysql.connector
from usuario import Usuario
from pedidoamistad import PedidoAmistad
from amistad import Amistad
from posteo import Posteo
from imagenes import Imagenes
from main import Main

#service mysql stop
#sudo /opt/lampp/lampp start

def validarInput(ingreso, valido):
    if ingreso in valido:
        return True
    else:
        if ingreso not in valido:
            print('Input incorrecto')
            return False

def printBase(base):
    Cursor=base.cursor

    print('-------------')
    print('Tabla usuario')
    print('-------------')
    Cursor.execute('select * from usuario')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('-------------------')
    print('Tabla pedidoamistad')
    print('-------------------')
    Cursor.execute('select * from pedidoamistad')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('-------------')
    print('Tabla amistad')
    print('-------------')
    Cursor.execute('select * from amistad')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('-------------')
    print('Tabla posteo')
    print('-------------')
    Cursor.execute('select *  from posteo')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('-------------------')
    print('Tabla imagen posteo')
    print('-------------------')
    Cursor.execute('select * from imagenPosteo')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('---------------')
    print('RUTA DE LA BASE')
    print('---------------')
    Cursor.execute('select @@datadir;')
    resultado=Cursor.fetchall()
    for i in resultado:
        print(i)
    print('---------------')
    print('---------------')

class Db():
    def __init__(self, dicc):
        self.conexion=mysql.connector.Connect(**dicc) ## *** es para conectar con  diccionario
        #self.conexion=mysql.connector.Connect() ## *** es para conectar con  diccionario
        self.cursor=self.conexion.cursor()

    def getCursor(self):
        return self.cursor

    def getConexion(self):
        return self.conexion

def Base(nombreBase):

    dicc={
        'host' : 'localhost',
        'user' : 'root',
        'password' : '',
        'database' : ''
        }

    check=Db(dicc)
    checkCursor=check.cursor
    checkCursor.execute('SHOW DATABASES')
    for base in checkCursor:
        if base[0]==nombreBase:
            Existe=True
            break
        Existe=False

    if Existe==False:
        execution='CREATE DATABASE '+nombreBase
        checkCursor.execute(execution)
        dicc1={
            'host' : 'localhost',
            'user' : 'root',
            'password' : '',
            'database' : nombreBase
            }
        dba=Db(dicc1)
        mycursor=dba.cursor
        mycursor.execute("CREATE TABLE usuario(usuarioId VARCHAR(9) PRIMARY KEY, nombre VARCHAR(50), avatar VARCHAR(150), email VARCHAR(80), password TEXT)")
        mycursor.execute("CREATE TABLE pedidoamistad(pedidoId VARCHAR(9) PRIMARY KEY, solicitanteId VARCHAR(10), solicitadoId VARCHAR(10))")
        mycursor.execute("CREATE TABLE amistad(amistadId VARCHAR(9) PRIMARY KEY, usuarioId1 VARCHAR(10), usuarioId2 VARCHAR(10))")
        mycursor.execute("CREATE TABLE posteo(posteoId VARCHAR(9) PRIMARY KEY, usuarioId VARCHAR(10), mensaje VARCHAR(100), foto VARCHAR(80))")
        mycursor.execute("CREATE TABLE imagenPosteo(nombre VARCHAR(20) PRIMARY KEY, direccion VARCHAR(150))")
        usuario1=Usuario('U-AA-1000','Juan', 'juan.png', 'juan@gmail.com', 'juanC')
        usuario1.save(dba)
        usuario2=Usuario('U-AA-1001','Pedro', 'pedro.jpg', 'pedro@gmail.com', 'pedroC')
        usuario2.save(dba)
        usuario3=Usuario('U-AA-1002','Pablo', 'pablo.jpg', 'pablo@gmail.com', 'pabloC')
        usuario3.save(dba)
        usuario4=Usuario('U-AA-1003','María', 'maria.png', 'maria@gmail.com', 'mariaC')
        usuario4.save(dba)
        usuario5=Usuario('U-AA-1004','Julieta', 'julieta.png', 'julieta@gmail.com', 'julietaC')
        usuario5.save(dba)
        usuario6=Usuario('U-AA-1005','Jimena', 'jimena.png', 'jimena@gmail.com', 'jimenaC')
        usuario6.save(dba)
        usuario7=Usuario('U-AA-1006','Agustina', 'agustina.jpg', 'agustina@gmail.com', 'agustinaC')
        usuario7.save(dba)
        usuario8=Usuario('U-AA-1007','Nicolás', 'nicolas.jpg', 'nicolas@gmail.com', 'nicolasC')
        usuario8.save(dba)
        usuario9=Usuario('U-AA-1008','Julia', 'julia.jpg', 'julia@gmail.com', 'juliaC')
        usuario9.save(dba)
        pamistad1=PedidoAmistad('P-AA-1000','U-AA-1002','U-AA-1000')
        pamistad1.save(dba)
        pamistad2=PedidoAmistad('P-AA-1001','U-AA-1003','U-AA-1000')
        pamistad2.save(dba)
        pamistad3=PedidoAmistad('P-AA-1002','U-AA-1000','U-AA-1004')
        pamistad3.save(dba)
        amistad1=Amistad('A-AA-1000','U-AA-1000', 'U-AA-1001')
        amistad1.save(dba)
        amistad2=Amistad('A-AA-1001','U-AA-1008', 'U-AA-1000')
        amistad2.save(dba)
        posteo1=Posteo('R-AA-1001', 'U-AA-1000', 'Mi guitarra.', 'guitarra.jpg')
        posteo1.save(dba)
        posteo2=Posteo('R-AA-1002', 'U-AA-1007', 'Fui a la playa.', 'playa.jpg')
        posteo2.save(dba)
        posteo3=Posteo('R-AA-1003', 'U-AA-1001', 'Hago ski.', 'esquiar.jpg')
        posteo3.save(dba)
        posteo4=Posteo('R-AA-1004', 'U-AA-1000', 'Estudio Python.', 'python.jpg')
        posteo4.save(dba)
        imagentorta=Imagenes('torta', 'torta.jpg')
        imagentorta.save(dba)
        imagenpaul=Imagenes('guitarra_electrica', 'guitarra_electrica.png')
        imagenpaul.save(dba)
        imagenasado=Imagenes('asado', 'asado.jpg')
        imagenasado.save(dba)
        imagensurf=Imagenes('surf', 'surf.jpg')
        imagensurf.save(dba)
        mensaje='Base de datos '+nombreBase+' creada y conectada.'

    else:
        if Existe==True:
            dicc1={
            'host' : 'localhost',
            'user' : 'root',
            'password' : '',
            'database' : nombreBase
            }
        dba=Db(dicc1)
        mensaje='Base de datos '+nombreBase+' conectada.'

    return mensaje, dba, nombreBase

print('''
-------------------------------------------------------------------------------------------------------
Al ingresar el nombre de la base, chequea si la base existe.
Si ya existe, se conecta directamente.
Si no existe, la crea con ese nombre desde este archivo con su estructura de tablas y algunos registros.
--------------------------------------------------------------------------------------------------------
''')

nombre=input('Ingrese nombre de la base: ')
LaBase=Base(nombre)
mensaje=LaBase[0]

validarVerlo=False
while validarVerlo==False:
    ver=input('¿Desea Ver la Base en pantalla? s/n: ')
    ver=ver.lower()
    sn=['s', 'n']
    validarVerlo=validarInput(ver, sn)
if ver=='s':
    printBase(LaBase[1])
else:
    if ver=='n':
        None

print(mensaje)
inicio=Main(LaBase[1])
inicio.validar()