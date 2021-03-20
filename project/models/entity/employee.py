from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class InfoModel(db.Model):
    __tablename__ = 'employees'
 
    id = db.Column(db.Integer, primary_key = True)
    create_by = db.Column(db.String)
    create_date = db.Column(db.String)
    user_name = db.Column(db.String)
    position = db.Column(db.String)
 
    def __init__(self,id,create_by,create_date,user_name,position):
        self.id = id
        self.create_by = create_by
        self.create_date = create_date
        self.user_name = user_name
        self.position = position
 
    def __repr__(self):
        return f"{self.id}:{self.create_by}:{self.create_date}:{self.user_name}:{self.position}"