from dbservice import DBService
from config import dboptions

class Controller:
    def connect_db(self):
        db = DBService(**dboptions)
        db.set()
        
