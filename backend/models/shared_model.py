from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#association table between Role and Skill
role_skill = db.Table('role_skill',db.Model.metadata,
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

#association table between Course and Skill
course_skill = db.Table('course_skill',db.Model.metadata,
    db.Column('course_id', db.String(20), db.ForeignKey('course.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'), primary_key=True)
)

#association table between LearningJourney and Courses
lj_course = db.Table('lj_course',db.Model.metadata,
    db.Column('lj_id', db.Integer, db.ForeignKey('learning_journey.id'), primary_key=True),
    db.Column('course_id', db.String(20), db.ForeignKey('course.id'), primary_key=True)
)