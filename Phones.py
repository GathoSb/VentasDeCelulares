from DB import DataBase


class Phones : 
    
    def __init__(self,model) :
        self.model = model 
    def save (self):
        sql =  f'Insertar Modelo (Model)("{self.model}")'
        db= DataBase()
        db.insert (sql)
    def list_all():
        db = DataBase ()
        sql = "SELECT * FROM PHONES"
        db.list(sql)
    def get_phones():
        db = DataBase()
        db.getById()   