from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import src.fontslib as fontslib
import src.themeslib as themeslib
import os

def change_theme(theme):
    text_fild['bg'] = themeslib.themes[theme]['text_bg']
    text_fild['fg'] = themeslib.themes[theme]['text_fg']
    text_fild['insertbackground'] = themeslib.themes[theme]['cursor']
    text_fild['selectbackground'] = themeslib.themes[theme]['select_bg']

def change_fonts(fontss):
    text_fild['font'] = fontslib.fonts[fontss]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

def new_file():
    root.title("Безымянный — R4Notepad")
    text_fild.delete('1.0', END)

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
    if file_path:
        root.title(os.path.basename(file_path) + " — R4Notepad")
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()
    root.title(os.path.basename(file_path) + " — R4Notepad")

def about_menu():
    about_window = Toplevel(root)
    about_window.iconbitmap('img/r4notepad.ico')
    about_window.title("О программе")
    about_window.geometry("300x300")
    about_name = Label(about_window, text="R4Notepad", font=("Roboto Bold", 20))
    about_github = Button(about_window, text="Страница проекта на Github", command=about_callback)
    about_name.pack()
    about_github.pack()

def about_callback():
    webbrowser.open_new("https://github.com/Rarmash/R4Notepad")
    
def cut_text():
    text_fild.event_generate("<<Cut>>")

def copy_text():
    text_fild.event_generate("<<Copy>>")

def paste_text():
    text_fild.event_generate("<<Paste>>")

root = Tk()
root.title('Безымянный — R4Notepad')
root.geometry('600x400')
root.iconbitmap('img/r4notepad.ico')

main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Новый файл', command=new_file)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Вырезать', command=cut_text)
edit_menu.add_command(label='Копировать', command=copy_text)
edit_menu.add_command(label='Вставить', command=paste_text)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

# Настройки
settings_menu = Menu(main_menu, tearoff=0)
settings_menu.add_command(label='О программе', command=about_menu)

font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
font_menu_sub.add_command(label='System', command=lambda: change_fonts('System'))
font_menu_sub.add_command(label='Script', command=lambda: change_fonts('Script'))
font_menu_sub.add_command(label='Segoe UI', command=lambda: change_fonts('Segoe UI'))
font_menu_sub.add_command(label='Segoe Script', command=lambda: change_fonts('Segoe Script'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Редактировать', menu=edit_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
main_menu.add_cascade(label='Настройки', menu=settings_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text,
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
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()