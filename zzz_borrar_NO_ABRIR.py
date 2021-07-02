import mysql.connector

#service mysql stop
#sudo /opt/lampp/lampp start

class db():
    def __init__(self, dicc):
        self.conexion=mysql.connector.Connect(**dicc) ## *** es para conectar con  diccionario
        #self.conexion=mysql.connector.Connect() ## *** es para conectar con  diccionario
        self.cursor=self.conexion.cursor()

    def getCursor(self):
        return self.cursor

    def getConexion(self):
        return self.conexion

dicc={
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : ''
    }

check=db(dicc)
checkCursor=check.cursor

checkCursor.execute('SHOW DATABASES')
for base in checkCursor:
    i=base[0]
    print(i)
lista=[]
checkCursor.execute('SHOW DATABASES')
for base in checkCursor:
    i=base[0]
    if i[0:3]=='soc' or i[0:3]=='Soc' or i[0:2]=='yo' or i[0:3]=='Han' or i[0:3]=='Muf' or i[0:3]=='bas' or i[0:2]=='ba' or i[0:2]=='Ba' or i[0:2]=='BA' or i[0:3]=='red' or i[0:2]=='bd' or i[0:1]=='b' or i[0:2]=='mu' or i[0:2]=='Mu':
        lista.append(i)
print(lista)
for i in lista:
    execution='DROP DATABASE '+i
    checkCursor.execute(execution)
execution='DROP DATABASE '+'nase2'
checkCursor.execute(execution)