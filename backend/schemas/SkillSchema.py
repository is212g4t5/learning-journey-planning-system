from schemas.shared_schema import ma
from models.SkillModel import Skill

#Skill Schema
class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        include_fk =True