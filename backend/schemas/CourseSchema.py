from schemas.shared_schema import ma
from models.CourseModel import Course


#Course Schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk =True

#Course with Skills Schema
class CourseWithSkillsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk =True
    skills = ma.Nested('SkillSchema', many=True)