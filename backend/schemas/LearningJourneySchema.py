from schemas.shared_schema import ma
from models.LearningJourneyModel import LearningJourney

#LearningJourney Schema
class LearningJourneySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True

#LearningJourney with Course Schema
class LearningJourneyWithCoursesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True
    courses = ma.Nested('CourseSchema',many=True)