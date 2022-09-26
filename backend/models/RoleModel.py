from models.shared_model import db, role_skill

#Role Class/Model
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True, nullable=False)
    description = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)
    learning_journeys = db.relationship('LearningJourney', backref='role', lazy=True)
    skills = db.relationship('Skill', secondary=role_skill, backref='roles', lazy=True)

    def __init__(self, name, description, active):
        self.name = name
        self.description = description
        self.active = active