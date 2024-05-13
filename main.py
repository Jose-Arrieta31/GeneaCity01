from tkinter import *
from tkinter import messagebox

def menu():
  vtnMenu=Tk()
  vtnMenu.title("Life Game")
  vtnMenu.geometry("800x600")
  vtnMenu.protocol("WM_DELETE_WINDOW",noCerrar())
  vtnMenu.resizable(False,False)
  vtnMenu.mainloop()

def noCerrar():
  messagebox.showwarning("No","")

menu()


