from schemas.shared_schema import ma
from models.RegistrationModel import Registration

#Registration Schema
class RegistrationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Registration
        include_fk =True