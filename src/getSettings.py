from configparser import ConfigParser
config = ConfigParser()

config.read('settings.ini')
settings = {
    'theme': config.get("Settings", "theme"),
}