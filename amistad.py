class Amistad():
    def __init__ (self, amistadId, usuarioId1, usuarioId2):
        self.__amistadId=amistadId
        self.__usuarioId1=usuarioId1
        self.__usuarioId2=usuarioId2

    def getAmistadId(self):
        return self.__amistadId

    def getUsuarioId1(self):
        return self.__usuarioId1

    def getUsuarioId2(self):
        return self.__usuarioId2

    def setAmistadId(self, amistadId):
        self.__amistadId=amistadId

    def setUsuarioId1(self, usuarioId1):
        self.__usuarioId1=usuarioId1

    def setUsuarioId2(self, usuarioId2):
        self.__usuarioId2=usuarioId2

    def save(self, db):
        sql='insert into amistad(amistadId, usuarioId1, usuarioId2) values (%s, %s, %s)'
        val=(self.getAmistadId(), self.getUsuarioId1(), self.getUsuarioId2())
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def delete(self, db):
        sql='delete from amistad where amistadId=%s'
        val=(self.getAmistadId(),)
        db.cursor.execute(sql, val)
        db.getConexion().commit()