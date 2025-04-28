# Importación de librerias necesarias
import socket
import datetime as dt
import dbControler as db


PUERTO = 5000
def inicializarSocket(puerto):
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        servidor.bind(("localhost",puerto))
        servidor.listen(1)
        print(f"Servidor escuchando en puerto: {puerto}")
        return servidor
    except socket.error as e:
        print(f"Error al enlazar socket al puerto {puerto}: {e}")
        return None



def recibirMensajes(servidor:socket.socket):
    while True:
        conexion, ip = servidor.accept()
        ip = f"{ip[0]}:{ip[1]}"
        print(f"Conexión establecida desde: {ip}") 
        while True:
            mensaje = conexion.recv(1024).decode()
            if mensaje == "éxito":
                mensajes = db.filtrarMensajePorIP(ip)
                cadena = "Mensajes de la sesion:\n" + "\n".join([": ".join(map(str, mensaje)) for mensaje in mensajes])
                conexion.send(cadena.encode())
                break
            print(f"Nuevo mensaje: {mensaje}")
            fecha = dt.datetime.today()
            db.guardarMensaje(mensaje, fecha, ip)
            conexion.send(f"Mensaje recibido: {fecha}".encode())
        print("Conexión cerrada desde el cliente")
        break


servidor = inicializarSocket(PUERTO)
if servidor != None:
    recibirMensajes(servidor)