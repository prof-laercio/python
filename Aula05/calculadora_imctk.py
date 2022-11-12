from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Informe o peso:").grid(column=0, row=0)
ttk.Entry(frm).grid(column=1, row=0)
ttk.Label(frm, text="Informe a altura:").grid(column=0, row=1)
ttk.Entry(frm).grid(column=1, row=1)
ttk.Button(frm, text="Calcular", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=3)
root.mainloop()