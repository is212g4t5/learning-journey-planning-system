from models.shared_model import db, lj_course

#LearningJourney Class/Model
class LearningJourney(db.Model):
    __tablename__ = 'learning_journey'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    courses = db.relationship('Course', secondary=lj_course, backref='learning_journeys', lazy=True)

    def __init__(self, name, staff_id, role_id):
        self.name = name
        self.staff_id = staff_id
        self.role_id = role_id