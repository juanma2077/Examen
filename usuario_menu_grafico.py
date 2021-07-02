from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import base64
import io

from pedidoamistad import PedidoAmistad
from amistad import Amistad
from generar_id import GenerarId
from posteo import Posteo

class MenuGrafico():

    def __init__(self, db, usuario, posicionAmigos, posicionRecibidos, posicionEnviados, posicionDisponibles, posicionPost):
        self.__db=db
        self.__usuario=usuario
        self.__posicionAmigos=posicionAmigos
        self.__posicionRecibidos=posicionRecibidos
        self.__posicionEnviados=posicionEnviados
        self.__posicionDisponibles=posicionDisponibles
        self.__posicionPost=posicionPost
        self.__listaImagenes=[]
        self.__PosteadorInicial=usuario


    def getUsuario(self):
        return self.__usuario

    def getDb(self):
        return self.__db

    def getPosicionAmigos(self):
        return self.__posicionAmigos

    def getPosicionRecibidos(self):
        return self.__posicionRecibidos

    def getPosicionEnviados(self):
        return self.__posicionEnviados

    def getPosicionDisponibles(self):
        return self.__posicionDisponibles

    def getPosicionPost(self):
        return self.__posicionPost

    def getListaImagenes(self):
        return self.__listaImagenes

    def getPosteadorInicial(self):
        return self.__PosteadorInicial

    def getRuta(self):
        return self.__ruta

    def setPosicionAmigos(self, valor):
        self.__posicionAmigos=valor

    def setPosicionRecibidos(self, valor):
        self.__posicionRecibidos=valor

    def setPosicionEnviados(self, valor):
        self.__posicionEnviados=valor

    def setPosicionDisponibles(self, valor):
        self.__posicionDisponibles=valor

    def setPosicionPost(self, valor):
        self.__posicionPost=valor

    def setListaImagenes(self, imagen):
        self.__listaImagenes.append(imagen)

    def setPosteadorInicial(self, usuario):
        self.__PosteadorInicial=usuario

    def pedirListas (self):

        self.getUsuario().setListaAmigos(self.getDb())
        self.getUsuario().setListaPAEnviada(self.getDb())
        self.getUsuario().setListaPARecibida(self.getDb())

        listaAmigos1=self.getUsuario().getListaAmigos()
        listaRecibidos1=self.getUsuario().getListaPARecibida()
        listaEnviados1=self.getUsuario().getListaPAEnviada()
        listaDisponibles1=self.getUsuario().ListarUsuarios(self.getDb())

        listaAmigos3=self.Listas3(listaAmigos1)
        listaRecibidos3=self.Listas3(listaRecibidos1)
        listaEnviados3=self.Listas3(listaEnviados1)
        listaDisponibles3=self.Listas3(listaDisponibles1)

        return listaAmigos3, listaRecibidos3, listaEnviados3, listaDisponibles3

    def Listas3(self, lista):
        listaVacia=[['n', 'n', 'n']]
        grupo3=[]
        agregar=[]
        todo=[]
        listaTotal=[]
        idUsuario={}
        if len(lista)!=0 and len(lista)<=3:
            if len(lista)==3:
                todo=[[lista[0], lista[1], lista[2]]]
            elif len(lista)==2:
                todo=[[lista[0], lista[1], 'n']]
            elif len(lista)==1:
                todo=[[lista[0],'n','n']]
            return todo
        elif len(lista)>3:
            for i in lista:
                grupo3.append(i)
                if len(grupo3)==3:
                    listaTotal.append(grupo3)
                    grupo3=[]
                else:
                    continue
            modulo=len(listaTotal)%3
            if modulo==2:
                agregar=[[lista[len(lista)-2],lista[len(lista)-1],'n']]
                todo=listaTotal+agregar
            elif modulo==1:
                agregar=[[lista[len(lista)-1],'n','n']]
                todo=listaTotal+agregar
            else:
                if modulo==0:
                    todo=listaTotal
            return todo
        else:
            if len(lista)==0:
                return listaVacia

    def menu(self):

        global root
        global titulo
        global boton
        global tipo
        global tipoS
        global tipo2
        global tipoR
        global color
        global ruta

        coloresGrisNaranja=['black', 'white', 'DarkOrange1','gray90', 'gray60', 'gray50', 'gray40', 'red']
        colores2=['coral','coral1', 'coral2', 'coral3', 'coral4']
        color=coloresGrisNaranja
        titulo=['POSTEOS','AMIGOS', 'RECIBIDOS', 'ENVIADOS', 'DISPONIBLES']
        boton=[' has iniciado tu sesión.', 'FINALIZAR SESION', 'VER POSTEOS','CANCELAR', 'ACEPTAR', 'RECHAZAR', 'INVITAR', 'CREAR POSTEO']
        tipoS = ("Arial", 12, "bold")
        tipo = ("Arial", 10, "bold")
        tipo2 = ("Arial", 7)
        tipoR = ("Arial", 24)
        ruta='/home/juanma/Documents/GitHub/TP_Objetos/images/'

        root = Tk()
        #root.geometry('800x600')
        root.config(bg=color[6])

        self.Superior()
        self.Inferior()

        root.mainloop()

    def Superior(self):

        superior=Frame(root)
        superior.config(bg=color[2])
        superior.grid(row=0, column=0)

        datosSesion=Frame(superior)
        datosSesion.config(bg=color[2])
        datosSesion.grid(row=0, column=0, stick=N)

        RedLabel=Label(datosSesion, text='RedSocial', font=tipoR)
        RedLabel.config(fg=color[6], bg=color[2])
        RedLabel.grid(row=0, column=0, stick=NW)

        InicioSesionLabel=Label(datosSesion, text=self.getUsuario().getNombre()+boton[0], font=tipoS)
        InicioSesionLabel.config(fg=color[1], bg=color[2])
        InicioSesionLabel.grid(row=1, column=0, stick=SE)

        avatar=self.getUsuario().getAvatar()
        if avatar!='' and avatar!='#':
            imagen=Image.open(ruta+avatar)
            imagen=ImageTk.PhotoImage(imagen)
            ImagenUsuario=Label(datosSesion, image=imagen)
            ImagenUsuario.image=imagen
            ImagenUsuario.config(bg=color[7], height=100)
            ImagenUsuario.grid(row=0, rowspan=3, column=1, stick=NE)
            #columnaCLI.grid(row=1, column=0)
        elif avatar=='#':
            imagen=Image.open(ruta+'avatar_vacio.jpg')
            imagen=ImageTk.PhotoImage(imagen)
            ImagenUsuario=Label(datosSesion, image=imagen)
            ImagenUsuario.image=imagen
            ImagenUsuario.config(bg=color[7], height=100)
            ImagenUsuario.grid(row=0, rowspan=3, column=1, stick=NE)
            #columnaCLI.grid(row=1, column=0)
        else:
            None

        VerPostBot=Button(datosSesion)
        VerPostBot.config(text=boton[2], font=tipo2, command=lambda: self.posteoUsuarioSesion())
        VerPostBot.grid(row=0, column=3, stick=SW)

        CrearPostBot=Button(datosSesion)
        CrearPostBot.config(text=boton[7], font=tipo2, command=lambda: self.CrearPostMenuPop())
        CrearPostBot.grid(row=1, column=3, stick=SW)

        CerrarSesionBot=Button(datosSesion)
        CerrarSesionBot.config(text=boton[1], font=tipo2, command=root.destroy)
        CerrarSesionBot.grid(row=2, column=3, stick=SW)

        #imagenPosteo=Entry (datosSesion) 
        #canvas1.create_window(200, 140, window=entry1)

        BandaLabel=Frame(datosSesion)
        BandaLabel.config(bg=color[0], height=10, width=750)
        BandaLabel.grid(row=3, column=0, columnspan=4)

    def posteoUsuarioSesion(self):
        self.setPosteadorInicial(self.getUsuario())
        self.refreshPost()


    def CrearPostMenuPop(self):

        global postPopUp

        postPopUp=Tk()
        postPopUp.geometry('400x200')
        postPopUp.config(bg=color[2])

        self.CrearPostPopContenido()

        postPopUp.mainloop()

    def CrearPostPopContenido(self):

        def input(ops):
            if opcionesInput.get() in ops and opcionesInput.get()!='':
                
                def input2():
                    if opcionesInput2.get()!='':
                        ElMensaje=opcionesInput2.get()
                        mensajefinal=self.getUsuario().SavePostMenuG(self.getDb(), ElMensaje, fotoNombre)
                        MensajeFinal=Label(marco, text=mensajefinal, fg=color[1], font=tipoS)
                        MensajeFinal.config(bg=color[2])
                        MensajeFinal.pack()

                fotoNombre=opcionesInput.get()

                opcionesLabelMensaje=Label(MarcoElegir, text='ESCRIBA UN MENSAJE')
                opcionesLabelMensaje.pack()
           
                opcionesInput2=Entry(MarcoElegir)
                opcionesInput2.pack()

                opcionesInputBot=Button(MarcoElegir)
                opcionesInputBot.config(text='ENTER', command=lambda: input2())
                opcionesInputBot.pack()
                
            else:
                NoFoto=Label(MarcoElegir, text='Incorrecto')
                NoFoto.pack()

        marco=Frame(postPopUp)
        marco.config()
        marco.grid(row=0, column=0, stick=N)

        opciones=self.getUsuario().CrearPostMenuG(self.getDb())
        
        MarcoElegir=Frame(marco)
        MarcoElegir.pack()

        opcionesLabelelija=Label(MarcoElegir, text='ELIJA UNA FOTO')
        opcionesLabelelija.pack()

        opcionesLabel=Label(MarcoElegir, text=opciones)
        opcionesLabel.pack()

        opcionesInput=Entry(MarcoElegir)
        opcionesInput.pack()

        opcionesInputBot=Button(MarcoElegir)
        opcionesInputBot.config(text='ENTER', command=lambda: input(opciones))
        opcionesInputBot.pack()


    def Inferior(self):

        global inferior

        inferior=Frame(root)
        inferior.config(bg=color[3])
        inferior.grid(row=1, column=0, stick=S)

        self.frameContenido()
    
    def frameContenido(self):

        global FrameContenido

        FrameContenido=Frame(inferior)
        FrameContenido.config(bg=color[3])
        FrameContenido.grid(row=0, column=0, sticky=NW)

        self.framePost()
        self.frameColumnas()

    def framePost(self):

        global FramePost

        FramePost=Frame(FrameContenido)
        FramePost.config(bg=color[3])
        #FrameContenido.columnconfigure(0, weight=2)
        FramePost.grid(row=0, column=0, sticky=NW)

        self.ColumnaPost()

    def frameColumnas(self):

        global FrameColumnas

        FrameColumnas=Frame(FrameContenido)
        FrameColumnas.config(bg=color[3])
        #FrameColumnas.columnconfigure(1, weight=1)
        FrameColumnas.grid(row=0, column=1, sticky=NE)

        self.titulosColumnas()
        self.columnaAmigos()
        self.columnaRecibidos()
        self.columnaEnviados()
        self.columnaDisponibles()

    def ColumnaPost(self):

        global ColumnaPost

        usuarioP=self.getPosteadorInicial()
        usuarioP.setListaPosteos(self.getDb())
        posteos=usuarioP.getListaPosteos()

        ColumnaPost=Frame(FramePost)
        ColumnaPost.config()
        ColumnaPost.grid(row=0, column=0, rowspan=4, columnspan=4, stick=NS)

        longitudLista=len(posteos)

        if longitudLista!=0:
            self.EspacioPost(usuarioP, posteos[self.getPosicionPost()])
            self.BotoneraPost(self.getPosicionPost(),longitudLista)
        else:
            if longitudLista==0:
                self.EspacioPost(usuarioP, 'nada')
                #self.BotoneraPost(self.getPosicionPost(),longitudLista)

    def EspacioPost(self, usuario, idd):

        if idd!='nada':

            posteo=usuario.instanciarPosteo(self.getDb(), idd)
            mensaje=posteo.getMensaje()
            espacio=' posteó: '
            nombre=usuario.getNombre()
            foto=posteo.getFoto()

            if foto!='#':
                imagen=Image.open(ruta+foto)
                imagen=ImageTk.PhotoImage(imagen)
                ColumnaPostI=Label(ColumnaPost, image=imagen)
                ColumnaPostI.image=imagen
                ColumnaPostI.pack()
            else:
                if foto=='#':
                    imagen=Image.open(ruta+'post_vacio.jpg')
                    imagen=ImageTk.PhotoImage(imagen)
                    ColumnaPostI=Label(ColumnaPost, image=imagen)
                    ColumnaPostI.image=imagen
                    ColumnaPostI.pack()

            ColumnaPostL=Label(ColumnaPost, text=nombre+espacio+mensaje, font=tipo)
            ColumnaPostL.config()
            ColumnaPostL.pack()

        else:
            if idd=='nada':
                nombre=usuario.getNombre()

                imagen=Image.open(ruta+'post_vacio.jpg')
                imagen=ImageTk.PhotoImage(imagen)
                ColumnaPostI=Label(ColumnaPost, image=imagen)
                ColumnaPostI.image=imagen
                ColumnaPostI.pack()

                ColumnaPostL=Label(ColumnaPost, text=nombre+' no tiene posteos.', font=tipo)
                ColumnaPostL.config()
                ColumnaPostL.pack()

    def BotoneraPost(self, valor, longitud):

        texto1P='<<'
        texto2P='>>'
        estadoB='normal'
        estadoF='normal'
        accion1P=lambda: self.accionesBotoneraPost(valor-1)
        accion2P=lambda: self.accionesBotoneraPost(valor+1)

        long=longitud-1
        if valor==0:
            estadoB='disabled'
        if valor==long:
            estadoF='disabled'

        columnaCBP=Frame(ColumnaPost)
        columnaCBP.config()
        columnaCBP.pack()

        columnaCB1=Button(columnaCBP, text=texto1P, command=accion1P, state=estadoB)
        columnaCB1.config()
        columnaCB1.pack(side=LEFT)
        columnaCB2=Button(columnaCBP, text=texto2P, command=accion2P, state=estadoF)
        columnaCB2.config()
        columnaCB2.pack(side=LEFT)

    def titulosColumnas(self):

        columnaT1=Frame(FrameColumnas)
        columnaT1.config(bg=color[3])
        columnaT1.grid(row=0, column=0)
       
        columnaT2=Frame(FrameColumnas)
        columnaT2.config(bg=color[3])
        columnaT2.grid(row=0, column=1)

        columnaT3=Frame(FrameColumnas)
        columnaT3.config(bg=color[3])
        columnaT3.grid(row=0, column=2)

        columnaT4=Frame(FrameColumnas)
        columnaT4.config(bg=color[3])
        columnaT4.grid(row=0, column=3)

        columnaTL1=Label(columnaT1, text=titulo[1], font=tipo, fg=color[0])
        columnaTL1.config(bg=color[3])
        columnaTL1.pack()

        columnaTL2=Label(columnaT2, text=titulo[2], font=tipo, fg=color[0])
        columnaTL2.config(bg=color[3])
        columnaTL2.pack()

        columnaTL3=Label(columnaT3, text=titulo[3], font=tipo, fg=color[0])
        columnaTL3.config(bg=color[3])
        columnaTL3.pack()

        columnaTL4=Label(columnaT4, text=titulo[4], font=tipo, fg=color[0])
        columnaTL4.config(bg=color[3])
        columnaTL4.pack()

    def columnaAmigos(self):

        global ColumnaAmigos

        lista=self.pedirListas()[0]

        print('Columna Amigos:')
        print(lista)

        longitud=len(lista)

        bloque3=lista[self.getPosicionAmigos()]

        print(bloque3)
        print(self.getPosicionAmigos())

        info1=self.infoAmistad(bloque3[0])
        info2=self.infoAmistad(bloque3[1])
        info3=self.infoAmistad(bloque3[2])

        ColumnaAmigos=Frame(FrameColumnas)
        ColumnaAmigos.config()
        ColumnaAmigos.grid(row=1, column=0, sticky=N)

        self.GrupoUsuario(ColumnaAmigos, 0, info1)
        self.GrupoUsuario(ColumnaAmigos, 1, info2)
        self.GrupoUsuario(ColumnaAmigos, 2, info3)
        self.botoneraDibujar(ColumnaAmigos, 3, 0, self.getPosicionAmigos(),longitud)

    def columnaRecibidos(self):

        global ColumnaRecibidos

        lista=self.pedirListas()[1]

        print('Columna Recibidos:')
        print(lista)

        longitud=len(lista)

        bloque3=lista[self.getPosicionRecibidos()]

        print(bloque3)
        print(self.getPosicionRecibidos())

        info1=self.infoRecibidos(bloque3[0])
        info2=self.infoRecibidos(bloque3[1])
        info3=self.infoRecibidos(bloque3[2])

        ColumnaRecibidos=Frame(FrameColumnas)
        ColumnaRecibidos.config()
        ColumnaRecibidos.grid(row=1, column=1, sticky=N)

        self.GrupoUsuario(ColumnaRecibidos, 0, info1)
        self.GrupoUsuario(ColumnaRecibidos, 1, info2)
        self.GrupoUsuario(ColumnaRecibidos, 2, info3)
        self.botoneraDibujar(ColumnaRecibidos, 3, 1, self.getPosicionRecibidos(),longitud)

    def columnaEnviados(self):

        global ColumnaEnviados

        lista=self.pedirListas()[2]
        print('Columna Enviados:')
        print(lista)

        longitud=len(lista)

        bloque3=lista[self.getPosicionEnviados()]
        print(bloque3)
        print(self.getPosicionEnviados())

        info1=self.infoEnviados(bloque3[0])
        info2=self.infoEnviados(bloque3[1])
        info3=self.infoEnviados(bloque3[2])

        ColumnaEnviados=Frame(FrameColumnas)
        ColumnaEnviados.config()
        ColumnaEnviados.grid(row=1, column=2, sticky=N)

        self.GrupoUsuario(ColumnaEnviados, 0, info1)
        self.GrupoUsuario(ColumnaEnviados, 1, info2)
        self.GrupoUsuario(ColumnaEnviados, 2, info3)
        self.botoneraDibujar(ColumnaEnviados, 3, 2, self.getPosicionEnviados(),longitud)

    def columnaDisponibles(self):

        global ColumnaDisponibles

        lista=self.pedirListas()[3]
        print('Columna Disponibles:')
        print(lista)

        longitud=len(lista)

        bloque3=lista[self.getPosicionDisponibles()]
        print(bloque3)
        print(self.getPosicionDisponibles())

        info1=self.infoDisponibles(bloque3[0])
        info2=self.infoDisponibles(bloque3[1])
        info3=self.infoDisponibles(bloque3[2])

        ColumnaDisponibles=Frame(FrameColumnas)
        ColumnaDisponibles.config()
        ColumnaDisponibles.grid(row=1, column=3, sticky=N)

        self.GrupoUsuario(ColumnaDisponibles, 0, info1)
        self.GrupoUsuario(ColumnaDisponibles, 1, info2)
        self.GrupoUsuario(ColumnaDisponibles, 2, info3)
        self.botoneraDibujar(ColumnaDisponibles, 3, 3, self.getPosicionDisponibles(),longitud)

    def GrupoUsuario(self, frame, ro, datos):

        col=color[3]
        '''
        if frame==ColumnaAmigos:
            col=color[6]
        elif frame==ColumnaRecibidos:
            col=color[6]
        elif frame==ColumnaEnviados:
            col=color[6]
        else:
            if frame==ColumnaDisponibles:
                col=color[6]
        '''

        # amistad, usuario, nombre, path, estado, texto1, texto2, accion1, accion2, accion3, texto3)

        if datos!='Vacio':

            nombre=datos[2]
            texto1=datos[5]
            texto2=datos[6]
            texto3=datos[10]
            accion1=datos[7]
            accion2=datos[8]
            accion3=datos[9]
            avatar=datos[3]
            estado=datos[4]

            #with open(avatar, 'rb') as file:
            #    img = base64.b64encode(file.read())
            #    img = Image.open(io.BytesIO(img))

            columnaG=Frame(frame)
            columnaG.config(bg=col, width=130)
            columnaG.grid(row=ro, column=0)

            columnaCL=Label(columnaG, text=nombre, font=tipo)
            columnaCL.config(bg=col)
            columnaCL.pack()
            #columnaCL.grid(row=3, column=0)

            if avatar!='' and avatar!='#':
                imagen=Image.open(ruta+avatar)
                imagen=ImageTk.PhotoImage(imagen)
                columnaCLI=Label(columnaG, image=imagen)
                columnaCLI.image=imagen
                columnaCLI.config(bg=col)
                columnaCLI.pack()
            elif avatar=='#':
                imagen=Image.open(ruta+'avatar_vacio.jpg')
                imagen=ImageTk.PhotoImage(imagen)
                columnaCLI=Label(columnaG, image=imagen)
                columnaCLI.image=imagen
                columnaCLI.config(bg=col)
                columnaCLI.pack()
            else:
                None

            columnaCB=Frame(columnaG)
            columnaCB.config(bg=col)
            columnaCB.pack()
            #columnaCB.grid(row=2, column=0)

            columnaCB1=Button(columnaCB, text=texto1, font=tipo2, command=accion1, state=estado)
            columnaCB1.config(bg=col)
            columnaCB1.pack()
            columnaCB2=Button(columnaCB, text=texto2, font=tipo2, command=accion2, state=estado)
            columnaCB2.config(bg=col)
            columnaCB2.pack(side=LEFT)
            columnaCB3=Button(columnaCB, text=texto3, font=tipo2, command=accion3, state=estado)
            columnaCB3.config(bg=col)
            columnaCB3.pack(side=LEFT)
        else:
            if datos=='Vacio':
                columnaG=Frame(frame)
                columnaG.grid(row=ro, column=0)
                columnaGF=Frame(columnaG)
                columnaGF.config(bg=col, height=130)
                columnaGF.pack()
                

    def botoneraDibujar(self, frame, ro, co, valor, longitud):
        texto1='<<'
        texto2='>>'
        estadoB='normal'
        estadoF='normal'
        accion1=lambda: self.accionesBotonera(valor-1, co)
        accion2=lambda: self.accionesBotonera(valor+1, co)

        long=longitud-1
        if valor==0:
            estadoB='disabled'
        if valor==long:
            estadoF='disabled'

        columnaCB=Frame(FrameColumnas)
        columnaCB.config()
        columnaCB.grid(row=ro, column=co, sticky=S)

        columnaCB1=Button(columnaCB, text=texto1, command=accion1, state=estadoB)
        columnaCB1.config()
        columnaCB1.pack(side=LEFT)
        columnaCB2=Button(columnaCB, text=texto2, command=accion2, state=estadoF)
        columnaCB2.config()
        columnaCB2.pack(side=LEFT)

    def infoAmistad(self, i):
        listaVacio=[]
        if i=='n':
            return 'Vacio'
        else:
            if i!='n':
                amistad=self.getUsuario().instanciarAmistad(self.getDb(), i)
                usuarioSesionId=self.getUsuario().getUsuarioId()
                usuarioId1=amistad.getUsuarioId1()
                usuarioId2=amistad.getUsuarioId2()
                if usuarioId1!=usuarioSesionId:
                    usuarioId=usuarioId1
                else:
                    if usuarioId2!=usuarioSesionId:
                        usuarioId=usuarioId2
                usuario=self.getUsuario().instanciarUsuario(self.getDb(), usuarioId)
                nombre=usuario.getNombre()
                path=usuario.getAvatar()
                estado='normal'
                texto1=boton[2]
                texto2=boton[3]
                texto3=''
                accion1=lambda: self.acciones(usuario, 'Post')
                accion2=lambda: self.acciones(amistad, 'Cancel')
                accion3=''

                return(amistad, usuario, nombre, path, estado, texto1, texto2, accion1, accion2, accion3, texto3)

    def infoRecibidos(self, i):
        listaVacio=[]
        if i=='n':
            return 'Vacio'
        else:
            pedido=self.getUsuario().instanciarPedidoAmistad(self.getDb(), i)
            usuarioId=pedido.getSolicitanteId()
            usuario=self.getUsuario().instanciarUsuario(self.getDb(), usuarioId)
            nombre=usuario.getNombre()
            path=usuario.getAvatar()
            estado='normal'
            texto1=boton[2]
            texto2=boton[4]
            texto3=boton[5]
            accion1=lambda: self.acciones(usuario, 'Post')
            accion2=lambda: self.acciones(pedido, 'Acep')
            accion3=lambda: self.acciones(pedido, 'Rech')

            return(pedido, usuario, nombre, path, estado, texto1, texto2, accion1, accion2, accion3, texto3)

    def infoEnviados(self, i):
        listaVacio=[]
        if i=='n':
            return 'Vacio'
        else:
            pedido=self.getUsuario().instanciarPedidoAmistad(self.getDb(), i)
            usuarioId=pedido.getSolicitadoId()
            usuario=self.getUsuario().instanciarUsuario(self.getDb(), usuarioId)
            nombre=usuario.getNombre()
            path=usuario.getAvatar()
            estado='normal'
            texto1=boton[2]
            texto2=''
            texto3=''
            accion1=lambda: self.acciones(usuario, 'Post')
            accion2=''
            accion3=''

            return(pedido, usuario, nombre, path, estado, texto1, texto2, accion1, accion2, accion3, texto3)

    def infoDisponibles(self, i):
        listaVacio=[]
        if i=='n':
            return 'Vacio'
        else:
            usuario=self.getUsuario().instanciarUsuario(self.getDb(), i)
            nombre=usuario.getNombre()
            path=usuario.getAvatar()
            estado='normal'
            texto1=boton[2]
            texto2=boton[6]
            texto3=''
            accion1=lambda: self.acciones(usuario, 'Post')
            accion2=lambda: self.acciones(usuario, 'Inv')
            accion3=''

            return(usuario, usuario, nombre, path, estado, texto1, texto2, accion1, accion2, accion3, texto3)

    def accionesBotoneraPost(self, valor):
        self.setPosicionPost(valor)
        #self.refreshDebajo()
        self.refreshPost()

    def accionesBotonera(self, valor, columna):
        if columna==0:
            self.setPosicionAmigos(valor)
            self.refreshColumnaAmigos()
        elif columna==1:
            self.setPosicionRecibidos(valor)
            self.refreshColumnaRecibidos()
        elif columna==2:
            self.setPosicionEnviados(valor)
            self.refreshColumnaEnviados()
        else:
            if columna==3:
                self.setPosicionDisponibles(valor)
                self.refreshColumnaDisponibles()

    def acciones(self, objeto, valor):
        print(objeto)
        if valor=='Post':
            self.setPosteadorInicial(objeto)
            self.setPosicionPost(0)
            self.refreshPost()
        else:
            if valor!='Post':
                if valor=='Cancel':
                    self.getUsuario().BorrarAmistad(self.getDb(), objeto)
                    self.setPosicionAmigos(0)
                    self.setPosicionDisponibles(0)
                    self.refreshColumnaAmigos()
                    self.refreshColumnaDisponibles()

                elif valor=='Acep':
                    self.getUsuario().AceptarRechazarAmistad(self.getDb(), objeto, True)
                    self.setPosicionRecibidos(0)
                    self.setPosicionAmigos(0)
                    self.refreshColumnaRecibidos()
                    self.refreshColumnaAmigos()
                elif valor=='Rech':
                    self.getUsuario().AceptarRechazarAmistad(self.getDb(), objeto, False)
                    self.setPosicionRecibidos(0)
                    self.setPosicionDisponibles(0)
                    self.refreshColumnaRecibidos()
                    self.refreshColumnaDisponibles()
                else:
                    if valor=='Inv':
                        self.getUsuario().PedirAmistad(self.getDb(), objeto)
                        self.setPosicionEnviados(0)
                        self.setPosicionDisponibles(0)
                        self.refreshColumnaEnviados()
                        self.refreshColumnaDisponibles()
            #self.reset()
            #self.refreshColumnas()

    def reset(self):
        self.setPosicionAmigos(0)
        self.setPosicionRecibidos(0)
        self.setPosicionEnviados(0)
        self.setPosicionDisponibles(0)

    def refreshPost(self):
        FramePost.destroy()
        self.framePost()

    def refreshColumnas(self):
        FrameColumnas.destroy()
        self.frameColumnas()
        #self.columnaAmigos()
        #self.columnaRecibidos()
        #self.columnaEnviados()
        #self.columnaDisponibles()

    def refreshColumnaAmigos(self):
        ColumnaAmigos.destroy()
        self.columnaAmigos()

    def refreshColumnaRecibidos(self):
        ColumnaRecibidos.destroy()
        self.columnaRecibidos()

    def refreshColumnaEnviados(self):
        ColumnaEnviados.destroy()
        self.columnaEnviados()

    def refreshColumnaDisponibles(self):
        ColumnaDisponibles.destroy()
        self.columnaDisponibles()