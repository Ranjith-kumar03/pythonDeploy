from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    def __init__(self,name, email , address , product):
        self.name = name
        self.email = email
        self.address= address
        self.product = product

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(54),  unique= True)
    email = db.Column(db.String(54), default = 0)
    address = db.Column(db.String(154),  unique= False)
    product = db.Column(db.String(54),  unique= True)


    def json(self):
        return {"id":self.id,"name":self.name,"email":self.email,"address":self.address,"product":self.product}


class Product(db.Model):
    def __init__(self,name, sno , lifetime):
        self.name = name
        self.sno = sno
        self.ifetime= lifetime
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(54),  unique= True)
    sno = db.Column(db.String(154),  unique= True)
    lifetime = db.Column(db.String(54),  unique= True)


    def json(self):
        return {"id":self.id,"name":self.name,"sno":self.sno,"lifetime":self.lifetime}

        