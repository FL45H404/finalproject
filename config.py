import os
class Config(object):
    DEBUG=False
    

class Production(Config):
    DEBUG=False
    SECRET_KEY=os.urandom(24)
