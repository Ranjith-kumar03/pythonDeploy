from flask import Flask , request , Blueprint
from src.database.database import db , User, Product

user = Blueprint("user",__name__, url_prefix="/api/v1/user/")

@user.get("/allusers")
def getallusers():
    users = User.query.all()
    if not users:
        return {"message":"no users added"}
    else:
        return {"message":{
            "users":[user.json()  for user in users]
        }}

@user.post("/adduser")
def adduser():
    user = request.get_json()
    print("see user",user)
    _user = User(
        name = user['name'],
        email = user['email'],
        address= user['address'],
        product= user['product']
    )
    db.session.add(_user)
    db.session.commit()
    db.session.flush()
    __user = User.query.filter_by(email = user['email']).first()

    if not __user:
        return {"message":"no user added"}
    else:
        return {"message":{"user":f'user with name {__user.name} added to database'}}
