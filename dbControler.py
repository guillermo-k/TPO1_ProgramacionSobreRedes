import sqlite3 as sql
import datetime

def guardarMensaje(contenido:str,fecha:datetime.date,ip_cliente:str):
    try:
        conn = sql.connect("TPO1.db")
    except:
        print("Error al intentar conectar con DB")
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO chat (contenido,fecha_envio,ip_cliente) VALUES('{contenido}','{fecha}','{ip_cliente}')"""
        )
        conn.commit()
        conn.close()
    except:
        print("Error al intentar insertar en DB")

def filtrarMensajePorIP(ip_cliente):
    try:
        conn = sql.connect("TPO1.db")
    except:
        print("Error al intentar conectar con DB")
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"""SELECT fecha_envio, contenido FROM chat WHERE ip_cliente LIKE '{ip_cliente}'"""
        )
        mensajes = cursor.fetchall()
        conn.close()
        return(mensajes)
    except ValueError as e:
        print("Error al consultar en DB", e)




if __name__=="__main__":
    conn = sql.connect("TPO1.db")
    cursor = conn.cursor()
    conn.commit()
    cursor.execute(
        """CREATE TABLE chat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contenido TEXT,
        fecha_envio TEXT,
        ip_cliente TEXT)
        """)
    conn.commit()
    conn.close()