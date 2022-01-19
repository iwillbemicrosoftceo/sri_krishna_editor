from concurrent.futures import process
from tkinter import *
from tkinter.filedialog import asksaveasfilename as filesaves
from tkinter.filedialog import askopenfilename as openfilesystem

compiler = Tk()
compiler.title("Sri krishna editor")
editor = Text()
def run():
    exec(editor.get("1.0", END))
    
    


def save():
        path = filesaves(filetypes=[("Python Files", "*.py")])
        with open(path, "w") as file:
            code = editor.get("1.0", END)
        file.write(code)

        

menu_bar= Menu(compiler)

exit_editor = Menu(menu_bar, tearoff=0)
exit_editor.add_command(label='Exit Editor', command=exit)
menu_bar.add_cascade(label="Exit", menu=exit_editor)

file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label='Run', command=run)
file_bar.add_command(label='Save', command=save)
menu_bar.add_cascade(label="File", menu=file_bar)

compiler.config(menu=menu_bar)


editor.pack()
compiler.mainloop()
