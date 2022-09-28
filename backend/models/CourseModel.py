from models.shared_model import db, course_skill

#Course Class/Model
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.String(15), default = 'Active')
    type = db.Column(db.String(10))
    category = db.Column(db.String(50))

    # active = db.Column(db.Boolean, default=True)
    skills = db.relationship('Skill', secondary=course_skill, backref='courses', lazy=True)

    def __init__(self, id, name, description, status, type, category, active = True):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.type = type
        self.category = category
        # self.active = active

