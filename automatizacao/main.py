import tkinter as tk    # Importando a biblioteca responsável por lidar com a interface.
import auto
from tkinter.filedialog import askdirectory

window = tk.Tk()            # Cria um objeto que irá cuidar da janela.

def window_interface():

    def button_pressed_folder():
        folderpath = askdirectory(title = "Selecione uma pasta")
        if len(folderpath) >= 1:
            var_folderpath.set(folderpath)
            auto.main(folderpath)

# Muda o nome da janela.
    window.title("Estoquelegal")
    window['bg'] = 'white'
    var_folderpath = tk.StringVar()  

    # Expande para além da coluna/linha.
    text = tk.Label(text= "Interface que o usuário irá visualizar", borderwidth=2, relief='solid')
    text.grid(row=0, column=0, columnspan = 4, sticky="NSEW")   

    # Texto.
    text1 = tk.Label(text= "Automatiza Sped:", anchor = 'e')
    text1.grid(row=1, column=0)

    # Botão para procurar xml.    
    bt_file2 = tk.Button(text = "Selecione uma pasta", command = button_pressed_folder)
    bt_file2.grid(row = 1, column = 1, padx = 10, pady = 10)

    # Função main da janela.
    window.mainloop()

# Função main.
window_interface()    # Cria a interface.