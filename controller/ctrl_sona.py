from app import db, ma
from models import Sona
from schemas import SonaSchema


class CtrlSona:

    def __init__(self):
        self.sona_schema = SonaSchema(strict=True)
        self.sonas_schama = SonaSchema(strict=True, many=True)

    def add_sona(self, sona):
        db.session.add(sona)
        db.session.commit()

        return self.dump_sona(sona)

    def get_sona(self, idx):
        p = Sona.query.get(idx)
        res = self.dump_sona(p)

        return res
    
    def dump_sona(self, sona):
        return self.sona_schema.dump(sona).data
    
    def dump_sonas(self, sonas):
        return self.sonas_schama.dump(sonas).data