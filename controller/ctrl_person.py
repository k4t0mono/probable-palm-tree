from app import db, ma
from models import Person
from schemas import PersonSchema


class CtrlPerson:

    def __init__(self):
        self.person_schema = PersonSchema(strict=True)
        self.people_schama = PersonSchema(strict=True, many=True)

    def add_person(self, person):
        db.session.add(person)
        db.session.commit()

        return self.dump_person(person)

    def get_person(self, idx):
        p = Person.query.get(idx)
        res = self.dump_person(p)

        return res
    
    def dump_person(self, person):
        return self.person_schema.dump(person).data
    
    def dump_people(self, people):
        return self.people_schama.dump(people).data