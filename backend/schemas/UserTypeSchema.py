from schemas.shared_schema import ma
from models.UserTypeModel import UserType

#UserType Schema
class UserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserType
        include_fk= True