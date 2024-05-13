from tkinter import messagebox

def automatico(vtnMenu):
        
    with open("saves/guardadoAutomatico.txt", "w"):
        pass
    messagebox.showinfo("a","Se guardo Automaticamente")
    vtnMenu.destroy()