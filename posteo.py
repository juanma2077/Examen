class Posteo():
    def __init__ (self, posteoId, usuarioId, mensaje, foto):
        self.__posteoId=posteoId
        self.__usuarioId=usuarioId
        self.__mensaje=mensaje
        self.__foto=foto

    def getPosteoId(self):
        return self.__posteoId

    def getUsuarioId(self):
        return self.__usuarioId

    def getMensaje(self):
        return self.__mensaje

    def getFoto(self):
        return self.__foto

    def setPosteoId(self, posteoId):
        self.__posteoId=posteoId

    def setUsuarioId(self, usuarioId):
        self.__usuarioId=usuarioId

    def setMensaje(self, mensaje):
        self.__mensaje=mensaje

    def setFoto(self, foto):
        self.__foto=foto

    def save(self, db):
        sql='insert into posteo(posteoId, usuarioId, mensaje, foto) values (%s, %s, %s, %s)'
        val=(self.getPosteoId(), self.getUsuarioId(), self.getMensaje(), self.getFoto())
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def delete(self, db):
        sql='delete from posteo where posteoId=%s'
        val=(self.getPosteoId(),)
        db.cursor.execute(sql, val)
        db.getConexion().commit()
