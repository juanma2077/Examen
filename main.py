#from usuario import Usuario
#from pedidoamistad import PedidoAmistad
#from amistad import Amistad
#from posteo import Posteo
#from imagenes import Imagenes
from login import LogIn
from registrar import Registrar
from baja import Baja

class Main():
    def __init__(self, db):
        self.__db=db

    def getDb(self):
        return self.__db

    def validarInput(self, ingreso, valido):
        if ingreso in valido:
            return True
        else:
            if ingreso not in valido:
                print('Input incorrecto')
                return False

    def validar(self):
        print('---------------------------')
        print('| LOGARTE= L              |')
        print('| REGISTRARTE= R          |')
        print('| DARTE DE BAJA= B        |')
        print('| MODIFICAR TUS DATOS= M  |')
        print('---------------------------')
        validar=False
        while validar==False:
            validos=['l', 'r', 'b', 'm']
            sel=input('Seleccione: ')
            sel=sel.lower()
            validar=self.validarInput(sel, validos)
        if sel=='l':
            log=LogIn(self.getDb())
            log.input('log')
        elif sel=='r':
            reg=Registrar(self.getDb())
            reg.datos()
        elif sel=='m':
            log=LogIn(self.getDb())
            log.input('update')
        else:
            if sel=='b':
                sebaja=Baja(self.getDb())
                sebaja.bajar()