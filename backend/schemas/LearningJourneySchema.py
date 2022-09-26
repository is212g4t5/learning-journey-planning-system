from schemas.shared_schema import ma
from models.LearningJourneyModel import LearningJourney

#LearningJourney Schema
class LearningJourneySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningJourney
        include_fk =True