from configparser import ConfigParser
import os.path

config = ConfigParser()

def cfgCreate():
    if not os.path.exists('settings.ini'):
        config.add_section("LOCALE")
        config.set("LOCALE", "language", "EN")
        config.add_section("Settings")
        config.set("Settings", "theme", "light")
        with open('settings.ini', "w+") as config_file:
            config.write(config_file)
            
def changeclr(theme):
    config.read("settings.ini")
    config.set("Settings", "theme", theme)
    with open('settings.ini', "w+") as config_file:
            config.write(config_file)
    config_file.close()

config.read('settings.ini')
settings = {
    'theme': config.get("Settings", "theme"),
}