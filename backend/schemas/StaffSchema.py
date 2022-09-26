from schemas.shared_schema import ma
from models.StaffModel import Staff

#Staff Schema
class StaffSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Staff
        include_fk =True