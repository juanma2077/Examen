import random

class GenerarId():
    def __init__(self, db, tipo):
        self.__db=db
        self.__tipo=tipo

    def getBase(self):
        return self.__db

    def getTipo(self):
        return self.__tipo

    def generar(self):
        tipo=self.getTipo().upper()
        letras=['A', 'B', 'C', 'E', 'F', 'G']
        claveExiste=True
        while claveExiste==True:
            a=tipo+'-'
            b=random.choice(letras)
            c=random.choice(letras)
            d='-'
            e=random.randint(1000, 9999)
            ID=a+b+c+d+str(e)
            base=self.getBase()
            if tipo=='U':
                sql='SELECT usuarioId FROM usuario'
            elif tipo=='A':
                sql='SELECT amistadId FROM amistad'
            elif tipo=='P':
                sql='SELECT pedidoId FROM pedidoamistad'
            elif tipo=='P':
                sql='SELECT pedidoId FROM pedidoamistad'
            else:
                if tipo=='R':
                    sql='SELECT posteoId FROM posteo'
            base.cursor.execute(sql)
            Reg=base.cursor.fetchall()
            for i in Reg:
                if i==ID:
                    claveExiste=True
                    break
                claveExiste=False
            return ID