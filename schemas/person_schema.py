from models import Person
from app import ma


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person