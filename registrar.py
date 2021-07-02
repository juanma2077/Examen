from usuario import Usuario
from generar_id import GenerarId

class Registrar():
    def __init__(self, db):
        self.__db=db

    def getDb(self):
        return self.__db

    def datos(self):
        datos=False
        while datos==False:
            resultadoValidacion=self.validar()
            datos=resultadoValidacion[0]
        self.registro(resultadoValidacion[1])

    def inputs(self):
        dicc=[]
        nombre=input('Ingrese nombre: ')
        dicc.append(nombre)
        avatar=input('Ingrese avatar (www): ')
        dicc.append(avatar)
        email=input('Ingrese email: ')
        dicc.append(email)
        password=input('Ingrese password (mínimo 4 caracteres): ')
        dicc.append(password)
        return dicc

    def validar(self):

        errores=[]
        dic=self.inputs()

        if dic[0]=='':
            error='Nombre vacío'
            errores.append(error)
        if dic[0]!='':
            sql='SELECT nombre FROM usuario WHERE nombre=%s'
            nom=dic[0]
            val=(nom,)
            self.getDb().cursor.execute(sql, val)
            Nom=self.getDb().cursor.fetchone()
            if Nom!=None:
               error='Nombre existente.'
               errores.append(error)
            else:
                None
        if dic[1]=='':
            error='Avatar vacío'
            errores.append(error)
        if dic[2]=='':
            error='Email vacío'
            errores.append(error)
        if dic[2]!='':
            sql='SELECT email FROM usuario where email=%s'
            mail=dic[2]
            val=(mail,)
            self.getDb().cursor.execute(sql, val)
            maiil=self.getDb().cursor.fetchone()
            if maiil!=None:
                error='Email existente.'
                errores.append(error)
            else:
                None
        if dic[3]=='' or len(dic[3])<3:
            error='Password vacío o con pocos caracteres'
            errores.append(error)

        if len(errores)==0:
            return True, dic
        else:
            print(errores)
            return False, errores

    def registro(self, dicci):
        ide=GenerarId(self.getDb(), 'U')
        idd=ide.generar()
        usuario=Usuario(idd, dicci[0], dicci[1], dicci[2], dicci[3])
        usuario.save(self.getDb())
        print('Usuario Registrado')