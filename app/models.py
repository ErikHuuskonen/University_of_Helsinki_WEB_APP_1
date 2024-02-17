from src import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'userinfo'

    
