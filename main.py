from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import src.fontslib as fontslib
import src.themeslib as themeslib
import os
from locales.strings import lang
from locales.changeLang import *

def change_theme(theme):
    text_field['bg'] = themeslib.themes[theme]['text_bg']
    text_field['fg'] = themeslib.themes[theme]['text_fg']
    text_field['insertbackground'] = themeslib.themes[theme]['cursor']
    text_field['selectbackground'] = themeslib.themes[theme]['select_bg']

def change_fonts(fontss):
    text_field['font'] = fontslib.fonts[fontss]['font']

def notepad_exit():
    #answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    #if answer:
        root.destroy()

def new_file():
    root.title(f"{lang['untitled']} — R4Notepad")
    text_field.delete('1.0', END)

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(title='Выбор файла', defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
    if file_path:
        root.title(os.path.basename(file_path) + " — R4Notepad")
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())
    text_field.bind("<<Modified>>", onModification)

def save(Event=False):
    contents = text_field.get('1.0', "end-1c")
    try:
        with open(file_path, 'w') as outputFile:
            outputFile.write(contents)
        text_field.bind("<<Modified>>", onModification)
    except:
        save_as()

def save_as(Event=False):
    global file_path
    file_path = filedialog.asksaveasfilename(initialfile=f'{lang["untitled"]}.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()
    root.title(os.path.basename(file_path) + " — R4Notepad")
    text_field.bind("<<Modified>>", onModification)

def about_menu():
    about_window = Toplevel(root)
    about_window.iconbitmap('img/r4notepad.ico')
    about_window.title(lang['about'])
    img = PhotoImage(file='img/r4notepad_100x100.png')
    about_window.geometry("300x350")
    about_window.resizable(width=False, height=False)
    about_name = Label(about_window, text="R4Notepad", font=("Roboto Bold", 20))
    about_pic = Label(about_window, image=img)
    about_pic.image = img
    imggh = PhotoImage(file='img/github.png')
    about_github = Button(about_window, image=imggh, command=about_callback, borderwidth = 0)
    about_github.image = imggh
    about_pic.pack()
    about_name.pack()
    about_github.pack()

def langselect():
    lang_window = Toplevel(root)
    lang_window.iconbitmap('img/r4notepad.ico')
    lang_window.title(lang['langselect'])
    lang_window.geometry("264x150")
    lang_window.resizable(width=False, height=False)
    lang_header = Label(lang_window, text=lang['langselect'], font=("Roboto Bold", 20))
    lang_header.pack()
    rus_flag = PhotoImage(file='img/rus_flag.png')
    en_flag = PhotoImage(file='img/en_flag.png')
    russian = Button(lang_window, image=rus_flag, command=changerussian, height=66, width=100, borderwidth = 0)
    russian.image = rus_flag
    english = Button(lang_window, image=en_flag, command=changeenglish, height=66, width=100, borderwidth = 0)
    english.image = en_flag
    russian.pack()
    russian.place(x=10, y=50)
    english.pack()
    english.place(x=150, y=50)
    
def about_callback():
    webbrowser.open_new("https://github.com/Rarmash/R4Notepad")
    
def cut_text():
    text_field.event_generate("<<Cut>>")

def copy_text():
    text_field.event_generate("<<Copy>>")

def paste_text():
    text_field.event_generate("<<Paste>>")
    
def onModification(Event=False):
    pass
    #try:
        #root.title(os.path.basename(file_path) + "* — R4Notepad")
    #except:
        #root.title(f"{lang['untitled']}* — R4Notepad")


root = Tk()
root.title(f'{lang["untitled"]} — R4Notepad')
root.geometry('600x400')
root.iconbitmap('img/r4notepad.ico')

root.bind("<Control-s>", save)

main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label=lang['new_file'], command=new_file)
file_menu.add_command(label=lang['open_file'], command=open_file)
file_menu.add_command(label=lang['save_file'], command=save)
file_menu.add_separator()
file_menu.add_command(label=lang['close_file'], command=notepad_exit)
root.config(menu=file_menu)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label=lang['cut_text'], command=cut_text)
edit_menu.add_command(label=lang['copy_text'], command=copy_text)
edit_menu.add_command(label=lang['paste_text'], command=paste_text)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label=lang['dark_theme'], command=lambda: change_theme('dark'))
view_menu_sub.add_command(label=lang['light_theme'], command=lambda: change_theme('light'))
view_menu.add_cascade(label=lang['theme'], menu=view_menu_sub)

# Настройки
settings_menu = Menu(main_menu, tearoff=0)
settings_menu.add_command(label=lang['about'], command=about_menu)
settings_menu.add_command(label=lang['langselect'], command=langselect)

font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
font_menu_sub.add_command(label='System', command=lambda: change_fonts('System'))
font_menu_sub.add_command(label='Script', command=lambda: change_fonts('Script'))
font_menu_sub.add_command(label='Segoe UI', command=lambda: change_fonts('Segoe UI'))
font_menu_sub.add_command(label='Segoe Script', command=lambda: change_fonts('Segoe Script'))
view_menu.add_cascade(label=lang['font'] + '...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label=lang['file'], menu=file_menu)
main_menu.add_cascade(label=lang['edit'], menu=edit_menu)
main_menu.add_cascade(label=lang['view'], menu=view_menu)
main_menu.add_cascade(label=lang['settings'], menu=settings_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_field = Text(f_text,
                 bg='white',
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Arial 14 bold'
                 )
text_field.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

text_field.bind("<<Modified>>", onModification)

root.mainloop()