from models.shared_model import db

#Skill Class/Model
class Skill(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, name, description,active):
        self.name = name
        self.description = description
        self.active = active