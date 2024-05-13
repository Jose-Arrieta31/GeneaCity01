from tkinter import *
from tkinter import messagebox
import guardar

def menu():
  vtnMenu=Tk()
  vtnMenu.title("Life Game")
  vtnMenu.geometry("800x600")
  vtnMenu.protocol("WM_DELETE_WINDOW",lambda:guardar.automatico(vtnMenu))
  vtnMenu.resizable(False,False)
  vtnMenu.mainloop()

def noCerrar():
  pass

menu()


