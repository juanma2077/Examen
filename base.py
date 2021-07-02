import mysql.connector
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

dbconf={
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'baseY'
    }

class Db():
    def __init__(self):
        self.conexion=mysql.connector.Connect(**dbconf) ## *** es para conectar con  diccionario
        #self.conexion=mysql.connector.Connect() ## *** es para conectar con  diccionario
        self.cursor=self.conexion.cursor()

    def getCursor(self):
        return self.cursor

    def getConexion(self):
        return self.conexion

dba=Db()
Cursor=dba.cursor

validarVerlo=False
while validarVerlo==False:
    ver=input('¿Desea Ver la Base en pantalla? s/n: ')
    ver=ver.lower()
    sn=['s', 'n']
    validarVerlo=validarInput(ver, sn)
if ver=='s':
    printBase(dba)
else:
    if ver=='n':
        None

inicio=Main(dba)
inicio.validar()