class Config(object):
    DEBUG = False
    TESTING = False
    HOST = "0.0.0.0"
    PORT = 8080
    LOGFILE = 'stacktrace.log'
    JSONfile = True
    AUTHPASS = "httppassword"
    ZONEFILE = "example.org"
    DBFILE = "zones.db"
    ZONES_START_POINT = ";zones start"
    ZONES_END_POINT = ";zones end"
    BIND_RELOAD_CMD = "/etc/rc.d/named reload"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    JSONfile = False

class TestingConfig(Config):
    TESTING = True
    DBFILE = "zonestest.db"
    ZONEFILE = "testexample.org"

