from abc import ABC

class Config(ABC):
    SECRET_KEY = 'secret'


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postegres://postegres:secret@localhost/statusok_cursos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    pass


config = {
    'development': Development,
    'testing': Testing
    
}