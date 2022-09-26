from models.shared_model import db

#Staff Class/Model
class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'), nullable=False)
    learning_journeys = db.relationship('LearningJourney', backref='staff', lazy=True)
 
    def __init__(self, first_name, last_name, department, email, user_type_id):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        self.user_type_id = user_type_id