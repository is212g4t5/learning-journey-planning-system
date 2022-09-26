from schemas.shared_schema import ma
from models.RoleModel import Role


#Role Schema
class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk =True