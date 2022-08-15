from configparser import ConfigParser

config = ConfigParser()

config.read("settings.ini")
language = config.get("LOCALE", "language")
section = language.upper()
config.read("locales/{}.ini".format(language))

lang = {
    'new_file': config.get(section, "new_file").encode('cp1251').decode('utf-8'),
    'open_file': config.get(section, "open_file").encode('cp1251').decode('utf-8'),
    'save_file': config.get(section, "save_file").encode('cp1251').decode('utf-8'),
    'close_file': config.get(section, "close_file").encode('cp1251').decode('utf-8'),
    
    'cut_text': config.get(section, "cut_text").encode('cp1251').decode('utf-8'),
    'copy_text': config.get(section, "copy_text").encode('cp1251').decode('utf-8'),
    'paste_text': config.get(section, "paste_text").encode('cp1251').decode('utf-8'),
    
    'dark_theme': config.get(section, "dark_theme").encode('cp1251').decode('utf-8'),
    'light_theme': config.get(section, "light_theme").encode('cp1251').decode('utf-8'),
    'theme': config.get(section, "theme").encode('cp1251').decode('utf-8'),
    
    'about': config.get(section, "about").encode('cp1251').decode('utf-8'),
    'langselect': config.get(section, "langselect").encode('cp1251').decode('utf-8'),
    
    'font': config.get(section, "font").encode('cp1251').decode('utf-8'),
    
    'file': config.get(section, "file").encode('cp1251').decode('utf-8'),
    'edit': config.get(section, "edit").encode('cp1251').decode('utf-8'),
    'view': config.get(section, "view").encode('cp1251').decode('utf-8'),
    'settings': config.get(section, "settings").encode('cp1251').decode('utf-8'),
    
    'untitled': config.get(section, "untitled").encode('cp1251').decode('utf-8'),
    
    'github_link': config.get(section, "github_link").encode('cp1251').decode('utf-8'),
}