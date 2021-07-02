class Imagenes():
    def __init__ (self, nombre, direccion):
        self.__nombre=nombre
        self.__direccion=direccion

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def save(self, db):
        sql='insert into imagenPosteo(nombre, direccion) values (%s, %s)'
        val=(self.getNombre(), self.getDireccion())
        db.cursor.execute(sql, val)
        db.getConexion().commit()