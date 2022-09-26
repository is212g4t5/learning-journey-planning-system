from models.shared_model import db

#Registration Class/Model
class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(20), db.ForeignKey('course.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    reg_status = db.Column(db.String(20), default = 'Waitlist', nullable=False)
    completion_status = db.Column(db.String(20), default = 'Not Started', nullable=False)

    def __init__(self, course_id, staff_id, reg_status, completion_status):
        self.course_id = course_id
        self.staff_id = staff_id
        self.reg_status = reg_status
        self.completion_status = completion_status