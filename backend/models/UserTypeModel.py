from models.shared_model import db

#UserType Class/Model
class UserType(db.Model):
    __tablename__ = 'user_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), unique=True, nullable=False)
    Staffs = db.relationship('Staff', backref='user_type', lazy=True)

    def __init__(self, type):
        self.type = type