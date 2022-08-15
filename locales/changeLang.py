from configparser import ConfigParser
from tkinter.messagebox import *

config = ConfigParser()

path = "settings.ini"

def changerussian():
    config.read(path)
    config.set("LOCALE", "language", "RU")
    with open(path, "w") as config_file:
        config.write(config_file)
    config_file.close()
    showinfo('Смена языка', 'Язык был изменён. Перезапустите программу для применения.')
    
def changeenglish():
    config.read(path)
    config.set("LOCALE", "language", "EN")
    with open(path, "w") as config_file:
        config.write(config_file)
    config_file.close()
    showinfo('Language change', 'The language has been changed. Restart the program to apply.')
    