import os
from pedidoamistad import PedidoAmistad
from amistad import Amistad
from generar_id import GenerarId
from posteo import Posteo

class MenuComando():
    def __init__(self, db, usuario):
        self.__db=db
        self.__usuario=usuario

    def getDb(self):
        return self.__db

    def getUsuario(self):
        return self.__usuario

    def menu(self):

        while True:

            def validarInput(ingreso, lista):
                if ingreso in lista:
                    return True
                else:
                    if ingreso not in lista:
                        return False

            listaUsuarios=self.getUsuario().getUsuariosDisponiblesValor()

            self.getUsuario().setListaAmigos(self.getDb())
            self.getUsuario().setListaPARecibida(self.getDb())
            self.getUsuario().setListaPAEnviada(self.getDb())

            Amigos=self.getUsuario().getListaAmigos()
            Recibidas=self.getUsuario().getListaPARecibida()
            Enviadas=self.getUsuario().getListaPAEnviada()

            AmigosP=self.printListas(Amigos, 'Lista de Amistades:', 'A')
            RecibidasP=self.printListas(Recibidas, 'Pedidos de Amistad Recibidos:', 'R')
            EnviadasP=self.printListas(Enviadas, 'Pedidos de Amistad Enviados:', 'E')

            if listaUsuarios==True:
                Disponible=self.getUsuario().ListarUsuarios(self.getDb())
                DisponibleP=self.printListas(Disponible, 'Usuarios Disponibles:', 'B')
                DisponiblePI=DisponibleP[0]
            else:
                DisponiblePI=''

            print('----------------------------------------------------------------------')
            print('| Usuario en Sesión: '+self.getUsuario().getNombre())
            print('----------------------------------------------------------------------')
            print('| '+AmigosP[0])
            print('| '+RecibidasP[0])
            print('| '+EnviadasP[0])
            print('| '+DisponiblePI)
            print('----------------------------------------------------------------------')
            print('| Aceptar o rechazar un pedido de amistad recibido= A                |')
            print('| Pedir amistar a un usuario= B                                      |')
            print('| Ver lista de usuarios disponibles: C-Activar/D-Desactivar)         |')
            print('| Borrar amistad= E                                                  |')
            print('| Crear posteo= F                                                    |')
            print('| Ver posteos de otros usuarios= G                                   |')
            print('| Ver posteos propios = H                                            |')
            print('| Finalizar sesión= I                                                |')
            print('----------------------------------------------------------------------')

            validarSeleccion=False
            while validarSeleccion==False:
                seleccion=input('Seleccione: ')
                seleccion=seleccion.lower()
                lista=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
                validarSeleccion=validarInput(seleccion, lista)

            if seleccion=='a':
                if len(Recibidas)!=0:
                    nombre=input('Escriba el nombre: ')
                    if nombre in RecibidasP[1].keys():
                        aceptarRechazar=False
                        while aceptarRechazar==False:
                            seleccionAR=input('¿Acepta el pedido o lo rechaza? A/R: ')
                            seleccionAR=seleccionAR.lower()
                            listaAR=['a', 'r']
                            aceptarRechazar=validarInput(seleccionAR, listaAR)
                        if seleccionAR=='a':
                            mensajeAR=self.getUsuario().AceptarRechazarAmistad(self.getDb(), RecibidasP[1][nombre], True)
                            print (mensajeAR)
                            print('----------------------------------------------------------------------')
                        else:
                            if seleccionAR=='r':
                                mensajeAR=self.getUsuario().AceptarRechazarAmistad(self.getDb(), RecibidasP[1][nombre], False)
                                print (mensajeAR)
                                print('----------------------------------------------------------------------')
                    else:
                        print('Ese nombre no se encuentra en la lista.')
                        print('----------------------------------------------------------------------')
                else:
                    print('No hay usuarios en la lista')
                    print('----------------------------------------------------------------------')

            if seleccion=='b':

                existeL=False
                existeD=False

                nombre=input('Ingresa el nombre del usuario: ')

                if len(Amigos)!=0 and nombre in AmigosP[1].keys():
                    print('Ya se encuentra en Amigos')
                    print('----------------------------------------------------------------------')
                    existeL=True

                elif len(Recibidas)!=0 and nombre in RecibidasP[1].keys():
                    print('Ya se encuentra en Pedidos Recibidos')
                    print('----------------------------------------------------------------------')
                    existeL=True

                elif len(Enviadas)!=0 and nombre in EnviadasP[1].keys():
                    print('Ya se encuentra en Pedidos Enviados')
                    print('----------------------------------------------------------------------')
                    existeL=True

                elif nombre==self.getUsuario().getNombre():
                    print('Eres tú.')
                    print('----------------------------------------------------------------------')
                    existeL=True

                else:
                    if listaUsuarios==True and len(Disponible)!=0:
                        if nombre in DisponibleP[1].keys():
                            existeL=True
                            existeD=True
                        else:
                            existeL=False
                    else:
                        if listaUsuarios==False:
                            Disponible=self.getUsuario().ListarUsuarios(self.getDb())
                            DisponibleP=self.printListas(Disponible, 'Usuarios Disponibles:', 'B')
                            if len(Disponible)!=0:
                                if nombre in DisponibleP[1].keys():
                                    existeL=True
                                    existeD=True
                                else:
                                    existeL=False

                #print(existeL)

                if existeL==False:
                    print('Noy existe un usuario con ese nombre')
                    print('----------------------------------------------------------------------')

                if existeD==True and existeL==True:
                    validarSN=False
                    while validarSN==False:
                        pedir=input('¿Deseas enviarle un pedido de amistad a '+nombre+'? S/N: ')
                        listaSN=['s', 'n']
                        pedir=pedir.lower()
                        validarSN=validarInput(pedir, listaSN)
                    if pedir=='s':
                        HacerPedido=self.getUsuario().PedirAmistad(self.getDb(), DisponibleP[1][nombre])
                        print(HacerPedido)
                        print('----------------------------------------------------------------------')
                    else:
                        if pedir=='n':
                                None

            if seleccion=='c':
                self.getUsuario().setUsuariosDisponiblesValor(True)

            if seleccion=='d':
                self.getUsuario().setUsuariosDisponiblesValor(False)

            if seleccion=='e':
                if len(Amigos)!=0:
                    nombre=input('Escriba el nombre: ')
                    if nombre in AmigosP[1].keys():
                        aceptarRechazar=False
                        while aceptarRechazar==False:
                            seleccionSN=input('¿Estás seguro que quieres cancelar la amistad? S/N: ')
                            seleccionSN=seleccionSN.lower()
                            listaSN=['s', 'n']
                            aceptarRechazar=validarInput(seleccionSN, listaSN)
                        if seleccionSN=='s':
                            mensajeSN=self.getUsuario().BorrarAmistad(self.getDb(), AmigosP[1][nombre])
                            print(mensajeSN)
                            print('----------------------------------------------------------------------')
                        else:
                            if seleccionSN=='n':
                                print('No se canceló la amistad.')
                                print('----------------------------------------------------------------------')
                    else:
                        print('Ese nombre no se encuentra en la lista.')
                        print('----------------------------------------------------------------------')

                else:
                    print('No hay usuarios en la lista')
                    print('----------------------------------------------------------------------')

            if seleccion=='f':
                mensajePosteo=self.getUsuario().CrearPost(self.getDb())
                print (mensajePosteo)
                print('----------------------------------------------------------------------')


            if seleccion=='g':
                nombre=input('Escriba el nombre: ')
                if nombre!=self.getUsuario().getNombre():
                    usuarioPost=self.getUsuario().BuscarPost(self.getDb(), nombre)
                    if usuarioPost[0]==True:
                        usuarioPost[1].setListaPosteos(self.getDb())
                        posteos=usuarioPost[1].getListaPosteos()
                        if len(posteos)!=0:
                            for i in posteos:
                                posteo=self.getUsuario().instanciarPosteo(self.getDb(), i)
                                print(posteo.getMensaje())
                                print(posteo.getFoto())
                                print('----------------------------------------------------------------------')
                        else:
                            print('No tiene posteos')
                            print('----------------------------------------------------------------------')
                    else:
                        if usuarioPost[0]==False:
                            print (usuarioPost[1])
                            print('----------------------------------------------------------------------')
                else:
                    print('Eres tú')
                    print('----------------------------------------------------------------------')

            if seleccion=='h':
                self.getUsuario().setListaPosteos(self.getDb())
                posteos=self.getUsuario().getListaPosteos()
                if len(posteos)!=0:
                    for i in posteos:
                        posteo=self.getUsuario().instanciarPosteo(self.getDb(), i)
                        print(posteo.getMensaje())
                        print(posteo.getFoto())
                    print('----------------------------------------------------------------------')
                else:
                    print('No hay posteos')
                    print('----------------------------------------------------------------------')

            if seleccion=='i':
                print('Adiós')
                print('----------------------------------------------------------------------')
                break

    def printListas(self, lista, titulo, identificador):
        string=''
        diccNombreObjeto={}
        diccItem={}
        if len(lista)!=0:
            if identificador=='A':
                for i in lista:
                    amistad=self.getUsuario().instanciarAmistad(self.getDb(), i)
                    if amistad.getUsuarioId1()!=self.getUsuario().getUsuarioId():
                        usuario=self.getUsuario().instanciarUsuario(self.getDb(), amistad.getUsuarioId1())
                        string=string+' * '+usuario.getNombre()
                        dicc={usuario.getNombre():amistad}
                        diccNombreObjeto.update(dicc)
                        dicc={}
                    elif amistad.getUsuarioId2()!=self.getUsuario().getUsuarioId():
                        usuario=self.getUsuario().instanciarUsuario(self.getDb(), amistad.getUsuarioId2())
                        string=string+' * '+usuario.getNombre()
                        dicc={usuario.getNombre():amistad}
                        diccNombreObjeto.update(dicc)
                        dicc={}
            elif identificador=='R':
                    for i in lista:
                        pedido=self.getUsuario().instanciarPedidoAmistad(self.getDb(), i)
                        usuario=self.getUsuario().instanciarUsuario(self.getDb(), pedido.getSolicitanteId())
                        string=string+' * '+usuario.getNombre()
                        dicc={usuario.getNombre():pedido}
                        diccNombreObjeto.update(dicc)
                        dicc={}
            elif identificador=='E':
                for i in lista:
                    pedido=self.getUsuario().instanciarPedidoAmistad(self.getDb(), i)
                    usuario=self.getUsuario().instanciarUsuario(self.getDb(), pedido.getSolicitadoId())
                    string=string+' * '+usuario.getNombre()
                    dicc={usuario.getNombre():pedido}
                    diccNombreObjeto.update(dicc)
                    dicc={}
            else:
                if identificador=='B':
                    for i in lista:
                        usuario=self.getUsuario().instanciarUsuario(self.getDb(), i)
                        string=string+' * '+usuario.getNombre()
                        dicc={usuario.getNombre():usuario}
                        diccNombreObjeto.update(dicc)
                        dicc={}
            return titulo+string, diccNombreObjeto 
        else:
            return titulo + ' * Sin items', 'Nada'