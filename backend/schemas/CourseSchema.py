from schemas.shared_schema import ma
from models.CourseModel import Course


#Course Schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        include_fk =True