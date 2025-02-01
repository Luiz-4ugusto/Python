from tkinter import *

def imprimirlist():
    print("cidade: " + str(lista_cid.get(ACTIVE)) )
app= Tk()
app.title("cidades")
app.geometry("500x300")

lista=["sc", "Sp", "pL"]
lista_cid=Listbox(app)
for list in lista:
    lista_cid.insert(END, list)
lista_cid.pack()
app,mainloop()

btn_lista=Button(app,text="imprimir",command=)