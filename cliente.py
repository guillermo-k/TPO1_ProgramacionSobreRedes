# Importación de librerias necesarias
import socket

# Inicialización del cliente y conexión al servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost",5000))

# Creación y envío de mensajes al servidor
while True:
    mensaje = input("escriba su mensaje: ")
    cliente.send(mensaje.encode())

    # Condición de salida
    if mensaje == "éxito":
        print(cliente.recv(1024).decode())
        break
    print(f"Respuesta del servidor: {cliente.recv(1024).decode()}")
print("Chat finalizado")

# Cierre de conexión
cliente.close()