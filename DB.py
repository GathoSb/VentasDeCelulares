from getpass import getpass , Error , connect
class DataBase:
    
    def __init__(self) :
        try:
            aux = connect (
                host ="LocalHost",
                user = "Usuario",
                password = getpass("contraseña"),
                database = "nueva tableta"
            )
            self.conection=aux 
        except Error as x : 
            print ("Error" + x)

def insert(self ,sql):
    try:
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()
    except Error as x : 
        print ("Erorr " + x)

def list (self , sql):
    cursor = self.connection.cursor()
    cursor.execute(sql)
    resultado= cursor.fetchall()
    for registro in resultado:
        print (registro)
    self.close()


def getById (self,pk):
    cursor = self.connection.cursor()
    cursor.execute

def close(self):
    self.connection.close()
    print ("la conexion fue cerrada")    

        