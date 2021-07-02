class PedidoAmistad():
    def __init__(self, pedidoId, solicitanteId, solicitadoId):
        self.__pedidoId=pedidoId
        self.__solicitanteId=solicitanteId
        self.__solicitadoId=solicitadoId

    def getPedidoId(self):
        return self.__pedidoId

    def getSolicitanteId(self):
        return self.__solicitanteId

    def getSolicitadoId(self):
        return self.__solicitadoId

    def setPedidoId(self, pedidoId):
        self.__pedidoId=pedidoId

    def setSolicitanteId(self, solicitanteId):
        self.__solicitanteId=solicitanteId

    def setSolicitadoId(self, solicitadoId):
        self.__solicitadoId=solicitadoId

    def save(self, db):
        sql='insert into pedidoamistad(pedidoId, solicitanteId, solicitadoId) values (%s, %s, %s)'
        val=(self.getPedidoId(), self.getSolicitanteId(), self.getSolicitadoId())
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def delete(self, db):
        sql='delete from pedidoamistad where pedidoId=%s'
        val=(self.getPedidoId(),)
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def update(self,dic, db):
        sql="update pedidoamistad set solicitanteId=%s, solicitadoId=%s where pedidoId=%s"
        val=(dic['solicitanteId'], dic['solicitadoId'], self.getPedidoId())
        db.cursor.execute(sql,val)
        db.getConexion().commit()
        self.setSolicitanteId(dic['solicitanteId'])
        self.setSolicitadoId(dic['solicitadoId'])