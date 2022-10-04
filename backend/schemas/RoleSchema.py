from schemas.shared_schema import ma
from models.RoleModel import Role


#Role Schema
class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk =True



#Role with Skills Schema
class RoleWithSkillsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk =True
    skills = ma.Nested('SkillSchema', many=True)