from usuario import Usuario
from pedidoamistad import PedidoAmistad
from amistad import Amistad
from posteo import Posteo

class Baja():
    def __init__(self, db):
        self.__db=db

    def getDb(self):
        return self.__db

    def validarInput(self, ingreso, valido):
        if ingreso in valido:
            return True
        else:
            if ingreso not in valido:
                return False

    def bajar(self):
        bajar=False
        while bajar==False:
            mail=input('Ingresa tu mail: ')
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
                            deBaja=False
                            while deBaja==False:
                                seguro=input('¿Estás seguro que quieres darte de baja? S/N: ')
                                seguro=seguro.lower()
                                valido=['s', 'n']
                                deBaja=self.validarInput(seguro, valido)
                            if seguro=='s':

                                sql='SELECT * FROM pedidoamistad WHERE solicitanteId=%s'
                                val=(usuario.getUsuarioId(),)
                                self.getDb().cursor.execute(sql, val)
                                registro=self.getDb().cursor.fetchall()
                                for registros in registro:
                                    pedido=PedidoAmistad(registros[0], registros[1], registros[2])
                                    pedido.delete(self.getDb())

                                sql='SELECT * FROM pedidoamistad WHERE solicitadoId=%s'
                                val=(usuario.getUsuarioId(),)
                                self.getDb().cursor.execute(sql, val)
                                registro=self.getDb().cursor.fetchall()
                                for registros in registro:
                                    pedido=PedidoAmistad(registros[0], registros[1], registros[2])
                                    pedido.delete(self.getDb())

                                sql='SELECT * FROM amistad WHERE usuarioId1=%s'
                                val=(usuario.getUsuarioId(),)
                                self.getDb().cursor.execute(sql, val)
                                registro=self.getDb().cursor.fetchall()
                                for registros in registro:
                                    objeto=Amistad(registros[0], registros[1], registros[2])
                                    objeto.delete(self.getDb())

                                sql='SELECT * FROM amistad WHERE usuarioId2=%s'
                                val=(usuario.getUsuarioId(),)
                                self.getDb().cursor.execute(sql, val)
                                registro=self.getDb().cursor.fetchall()
                                for registros in registro:
                                    objeto=Amistad(registros[0], registros[1], registros[2])
                                    objeto.delete(self.getDb())

                                sql='SELECT * FROM posteo WHERE usuarioId=%s'
                                val=(usuario.getUsuarioId(),)
                                self.getDb().cursor.execute(sql, val)
                                registro=self.getDb().cursor.fetchall()
                                for registros in registro:
                                    objeto=Posteo(registros[0], registros[1], registros[2], registros[3])
                                    objeto.delete(self.getDb())

                                usuario.delete(self.getDb())

                                print('Te diste de baja.')

                            else:
                                if seguro=='n':
                                    print('No te has dado de baja')
                            bajar=True
                            break
                        else:
                            print('Datos Incorrectos.')