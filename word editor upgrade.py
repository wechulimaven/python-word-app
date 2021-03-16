from tkinter import*
from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox
import os

root=Tk()
root.iconbitmap(r'word_0.ico')
root.title('WORD EDITOR')
textArea = scrolledtext.ScrolledText(root, width=100,height=80)
textArea.pack()

def newfile():
    if len(textArea.get('1.0',END+'-1'))>0:
        if messagebox.askyesno('Save?','Do you wish to save file'):
            savefile()
        else:
            textArea.delete('1.0',END)

def openfile():
    file=filedialog.askopenfile(parent=root,mode='rb',title='Select Text File to Edit',filetypes=(("Text file", '*.txt'), ("All files", '*.*')))
    root.title(os.path.basename(file.name) + '-TEXT EDITOR')

    if file != None:
        contents=file.read()
        textArea.insert('1.0',contents)
        file.close()

def savefile():
    file = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("Text file", '*.txt'), ("HTML file", '*.html'), ("All files", '*.*')))
    if file != None:
        data=textArea.get('1.0',END+'-1')
        file.write(data)
        file.close()


def iexit():
    msg=messagebox.askyesno('Quit','Are you sure you want to quit')
    if msg:
        root.destroy()

def about():
    label=messagebox.showinfo('About','This a Word Editor build with python for educatioal purposes')

menu=Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New',command=newfile)
fileMenu.add_command(label='Open',command=openfile)
fileMenu.add_command(label='Save',command=savefile)
fileMenu.add_command(label='Print')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=iexit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help')
menu.add_cascade(label='About',command=about)


root.mainloop()
