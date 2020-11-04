import os
class Config(object):
    DEBUG=False
    

class Production(Config):
    DEBUG=True
    SECRET_KEY=os.urandom(24)