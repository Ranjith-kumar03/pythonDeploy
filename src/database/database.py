from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    def __init__(self,name, age , address , product):
        self.name = name
        self.age = age
        self.address= address
        self.product = product

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(54), required= True , unique= True)
    age = db.Column(db.Integer, default = 0)
    address = db.Column(db.String(154), required= True , unique= False)
    product = db.Column(db.String(54), required= True , unique= True)


    def json(self):
        return {"id":self.id,"name":self.name,"age":self.age,"address":self.address,"product":self.product}


class Product(db.Model):
    def __init__(self,name, sno , lifetime):
        self.name = name
        self.sno = sno
        self.ifetime= lifetime
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(54), required= True , unique= True)
    age = db.Column(db.Integer, default = 0)
    sno = db.Column(db.String(154), required= True , unique= False)
    lifetime = db.Column(db.String(54), required= True , unique= True)


    def json(self):
        return {"id":self.id,"name":self.name,"age":self.age,"address":self.address,"product":self.product}

        