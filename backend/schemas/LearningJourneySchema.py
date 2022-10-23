from schemas.shared_schema import ma
from models.LearningJourneyModel import LearningJourney

#LearningJourney Schema
class LearningJourneySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True


#Course with Skills Schema
class LearningJourneyWithCoursesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True
    courses = ma.Nested('CourseSchema', many=True)
