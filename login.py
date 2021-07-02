from usuario import Usuario
from update import Update
class LogIn():
    def __init__(self, db):
        self.__db=db

    def getDb(self):
        return self.__db

    def input(self, tipo):

        def validarInput(ingreso, valido):
            if ingreso in valido:
                return True
            else:
                if ingreso not in valido:
                    return False

        Log=False
        while Log==False:
            mail=input('Ingresa tu email: ')
            passW=input('Ingresa tu contraseña: ')
            if mail=='' or passW=='':
                print('Input vacío.')
                continue
            else:
                if mail!='' and passW!='':
                    sql='SELECT * FROM usuario WHERE email=%s'
                    val=(mail,)
                    self.getDb().cursor.execute(sql, val)
                    rows=self.getDb().cursor.fetchone()
                    if not rows:
                        print('Datos Incorrectos.')
                    else:
                        usuario=Usuario(rows[0],rows[1],rows[2],rows[3],rows[4])
                        pas=usuario.desencriptarPass(rows[4])
                        if pas==passW:
                            if tipo=='log':
                                validar=False
                                while validar==False:
                                    interface=input('¿Desea utilizar una interface gráfica? S/N: ')
                                    interface=interface.lower()
                                    valido=['s', 'n']
                                    validar=validarInput(interface, valido)
                                if interface=='s':
                                    usuario.menu_interfaz(self.getDb())
                                else:
                                    if interface=='n':
                                        usuario.menu_comando(self.getDb())
                            if tipo=='update':
                                    update=Update(self.getDb(), usuario)
                                    update.datos()
                            Log=True
                            break
                        else:
                            print('Datos Incorrectos.')