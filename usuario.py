import base64
from pedidoamistad import PedidoAmistad
from amistad import Amistad
from generar_id import GenerarId
from posteo import Posteo
from usuario_menu_grafico import MenuGrafico
from usuario_menu_comando import MenuComando

class Usuario():
    def __init__(self, usuarioId, nombre, avatar, email, password):
        self.__usuarioId=usuarioId
        self.__nombre=nombre
        self.__avatar=avatar
        self.__email=email
        self.setPassword(password)
        self.__listaPAEnviada=[]
        self.__listaPARecibida=[]
        self.__listaAmigos=[]
        self.__listaPosteos=[]
        self.__usuariosDisponibles=False

    def getUsuarioId(self):
        return self.__usuarioId

    def getNombre(self):
        return self.__nombre

    def getAvatar(self):
        return self.__avatar

    def getMail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def getListaPAEnviada(self):
        return self.__listaPAEnviada

    def getListaPARecibida(self):
        return self.__listaPARecibida

    def getListaAmigos(self):
        return self.__listaAmigos

    def getUsuariosDisponiblesValor(self):
        return self.__usuariosDisponibles

    def getListaPosteos(self):
        return self.__listaPosteos

    def setUsuarioId(self, usuarioId):
        self.__usuarioId=usuarioId

    def setNombre(self, nombre):
        self.__nombre=nombre

    def setAvatar(self, avatar):
        self.__avatar=avatar

    def setMail(self, email):
        self.__email=email

    def setPassword(self, password):
        self.__password=self.encriptarPass(password)

    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')

    def desencriptarPass(self, password):
        return base64.decodebytes(password.encode("utf-8")).decode('utf-8')

    def save(self, db):
        sql='insert into usuario(usuarioId, nombre, avatar, email, password) values (%s, %s, %s, %s, %s)'
        val=(self.getUsuarioId(), self.getNombre(), self.getAvatar(), self.getMail(), self.getPassword())
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def delete(self, db):
        sql='delete from usuario where usuarioId=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        db.getConexion().commit()

    def update(self,dic, db):
        sql="update usuario set nombre=%s, avatar=%s, email=%s, password=%s where usuarioId=%s"
        self.setPassword(dic['password'])
        val=(dic['nombre'], dic['avatar'], dic['email'], self.getPassword(), self.getUsuarioId())
        db.cursor.execute(sql,val)
        db.getConexion().commit()
        #self.setNombre(dic['nombre'])
        #self.setAvatar(dic['avatar'])
        #self.setMail(dic['email'])
        #self.setPassword(dic['password'])

    def setListaPAEnviada(self, db):
        self.__listaPAEnviada=[]
        sql='SELECT pedidoId FROM pedidoamistad WHERE solicitanteId=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        if len(Reg)!=0:
            for i in Reg:
                self.__listaPAEnviada.append(i[0])
        else:
            self.__listaPAEnviada

    def setListaPARecibida(self,db):
        self.__listaPARecibida=[]
        sql='SELECT pedidoId FROM pedidoamistad WHERE solicitadoId=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        if len(Reg)!=0:
            for i in Reg:
                self.__listaPARecibida.append(i[0])
        else:
            self.__listaPARecibida

    def setListaAmigos(self, db):
        self.__listaAmigos=[]

        sql='SELECT amistadId FROM amistad WHERE usuarioId1=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        if len(Reg)!=0:
            for i in Reg:
                self.__listaAmigos.append(i[0])
        else:
            self.__listaAmigos

        sql='SELECT amistadId FROM amistad WHERE usuarioId2=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        if len(Reg)!=0:
            for i in Reg:
                self.__listaAmigos.append(i[0])
        else:
            self.__listaAmigos

    def setListaPosteos(self, db):
        self.__listaPosteos=[]
        sql='SELECT posteoId FROM posteo WHERE usuarioId=%s'
        val=(self.getUsuarioId(),)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        if len(Reg)!=0:
            for i in Reg:
                self.__listaPosteos.append(i[0])
        else:
            self.__listaPosteos

    def setUsuariosDisponiblesValor(self, valor):
        self.__usuariosDisponibles=valor

    def instanciarUsuario(self, db, idd):
        sql='SELECT * FROM usuario WHERE usuarioId=%s'
        val=(idd,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        for i in Reg:
            usuario=Usuario(i[0],i[1],i[2],i[3],i[4])
            return usuario

    def instanciarPedidoAmistad(self, db, idd):
        sql='SELECT * FROM pedidoamistad WHERE pedidoId=%s'
        val=(idd,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        for i in Reg:
            pedido=PedidoAmistad(i[0],i[1],i[2])
            return pedido

    def instanciarAmistad(self, db, idd):
        sql='SELECT * FROM amistad WHERE amistadId=%s'
        val=(idd,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        for i in Reg:
            amistad=Amistad(i[0],i[1],i[2])
            return amistad

    def instanciarPosteo(self, db, idd):
        sql='SELECT * FROM posteo WHERE posteoId=%s'
        val=(idd,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchall()
        for i in Reg:
            posteo=Posteo(i[0],i[1],i[2],i[3])
            return posteo

    def ListarUsuarios(self, db):

        self.setListaPAEnviada(db)
        self.setListaPARecibida(db)
        self.setListaAmigos(db)

        usuariosEnListas=[]

        for i in self.getListaPAEnviada():
            pedido=self.instanciarPedidoAmistad(db, i)
            UsuarioId=pedido.getSolicitadoId()
            usuariosEnListas.append(UsuarioId)

        for i in self.getListaPARecibida():
            recibido=self.instanciarPedidoAmistad(db, i)
            UsuarioId=recibido.getSolicitanteId()
            usuariosEnListas.append(UsuarioId)

        for i in self.getListaAmigos():
            amistad=self.instanciarAmistad(db, i)
            UsuarioId1=amistad.getUsuarioId1()
            if self.getUsuarioId()!=UsuarioId1:
                usuariosEnListas.append(UsuarioId1)

        for i in self.getListaAmigos():
            amistad=self.instanciarAmistad(db, i)
            UsuarioId2=amistad.getUsuarioId2()
            if self.getUsuarioId()!=UsuarioId2:
                usuariosEnListas.append(UsuarioId2)

        usuariosEnListas.append(self.getUsuarioId())
        usuariosDisponibles=[]
        usuariosDisponiblesVacio=[]

        sql='SELECT usuarioId FROM usuario'
        db.cursor.execute(sql)
        Reg=db.cursor.fetchall()
        if Reg!=None:
            for i in Reg:
                if i[0] not in usuariosEnListas:
                    usuariosDisponibles.append(i[0])
            return usuariosDisponibles
        else:
            if Reg==None:
                return usuariosDisponiblesVacio

    def BuscarPost(self, db, nombre):
        sql='SELECT usuarioId FROM usuario WHERE nombre=%s'
        val=(nombre,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchone()
        if Reg!=None:
            usuario=self.instanciarUsuario(db, Reg[0])
            return True, usuario
        else:
            if Reg==None:
                False, 'Usuario inexistente.'

    def AceptarRechazarAmistad(self, db, pedido, valor):
        if valor==True:
            usuarioId=pedido.getSolicitanteId()
            pedido.delete(db)
            ide=GenerarId(db, 'A')
            idd=ide.generar()
            amistad=Amistad(idd, self.getUsuarioId(), usuarioId)
            amistad.save(db)
            return 'Amistad Aceptada'
        else:
            if valor==False:
                pedido.delete(db)
                return 'Amistad Rechazada'

    def PedirAmistad(self, db, usuario):
        ide=GenerarId(db, 'P')
        idd=ide.generar()
        pedido=PedidoAmistad(idd, self.getUsuarioId(), usuario.getUsuarioId())
        pedido.save(db)
        return 'Amistad Solicitada'

    def BorrarAmistad(self, db, amistad):
        amistad.delete(db)
        return 'Amistad Cancelada'

    def CrearPost(self, db):
        sql='SELECT * FROM imagenPosteo'
        db.cursor.execute(sql)
        Reg=db.cursor.fetchall()
        for i in Reg:
            print(i[0])
        fotoExiste=False
        while fotoExiste==False:
            foto=input('Ingrese el nombre de la foto: ')
            foto=foto.lower()
            for i in Reg:
                if i[0]==foto:
                    url=i[1]
                    fotoExiste=True
                    break
                else:
                    continue
        mensaje=input('Ingrese su mensaje: ')
        ide=GenerarId(db, 'R')
        idd=ide.generar()
        posteo=Posteo(idd, self.getUsuarioId(), mensaje, url)
        posteo.save(db)
        return 'Posteo creado.'

    def CrearPostMenuG(self, db):
        sql='SELECT * FROM imagenPosteo'
        db.cursor.execute(sql)
        Reg=db.cursor.fetchall()
        string=''
        for i in Reg:
            string=string +' * '+i[0]
        return string

    def SavePostMenuG(self, db, mensaje, nombreFoto):
        sql='SELECT direccion FROM imagenPosteo where nombre=%s'
        val=(nombreFoto,)
        db.cursor.execute(sql, val)
        Reg=db.cursor.fetchone()
        ide=GenerarId(db, 'R')
        idd=ide.generar()
        posteo=Posteo(idd, self.getUsuarioId(), mensaje, Reg[0])
        posteo.save(db)
        return 'Posteo creado.'

    def menu_interfaz(self, db):
        usuario=self.instanciarUsuario(db, self.getUsuarioId())
        #ruta=input('Ingrese la ruta de las imagenes: ')
        sesionGrafica=MenuGrafico(db, usuario, 0,0,0,0,0)
        sesionGrafica.menu()

    def menu_comando(self, db):
        #clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        #clearConsole()
        #cls = lambda: print('\n'*100)
        #cls()
        usuario=self.instanciarUsuario(db, self.getUsuarioId())
        sesionComando=MenuComando(db, usuario)
        sesionComando.menu()

    def test(self):
        print('Sí')