from tkinter import *
from centraliza import center
from tkinter.ttk import *

campos = []

def submit_segunda_janela():
    nome=campos[0].get()
    email=campos[1].get()
    telefone=campos[2].get()
    print(nome,email,telefone)

#primeira janela é tk, a segunda é toplevel
def segunda_janela():

    #janelas secundarias são criadas a partir da toplevel
    segunda_janela= Toplevel()

    #tamanho
    segunda_janela.geometry("300x150")

    #centraliza
    center (segunda_janela)

    #titulo
    segunda_janela.title("campus")

    #inclui campus
    lblnome = Label(segunda_janela, text="nome:").grid(row=0,column=0,padx=5,pady=5)
    lblemail = Label(segunda_janela, text="email:").grid(row=1,column=0,padx=5,pady=5)
    lbltelefone = Label(segunda_janela, text="telefone:").grid(row=2,column=0,padx=5,pady=5)


    txtNome = Entry(segunda_janela)
    txtNome.grid(row=0,column=1,padx=5,pady=5)
    txtEmail = Entry(segunda_janela)
    txtEmail.grid(row=1,column=1,padx=5,pady=5)
    txtTelefone = Entry(segunda_janela)
    txtTelefone.grid(row=2,column=1,padx=5,pady=5)

    campos.append(txtNome)
    campos.append(txtEmail)
    campos.append(txtTelefone)
    btnSubmit= Button(segunda_janela,text="submit",command=submit_segunda_janela).grid(row=3,column=0,padx=5,pady=5)


    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    segunda_janela.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    segunda_janela.grab_set()

    
    #deixar janela aberta 
    segunda_janela.mainloop()



def main():
    #cria a janela principal
    janela_principal =Tk()

    #DEFINE O TAMANHO DA JANELA
    janela_principal.geometry("800x600")

    #CENTRALIZA A JANELA NA TELA
    center(janela_principal)

    #DEFINE O TITULO DA JANELA
    janela_principal.title("janela")

    #criar botão usando a class button
    btn = Button(janela_principal, text="cadastro",command=segunda_janela)

    #coloca o botão na primeira linha e coluna
    #coluna
    btn.grid(row=0, column=0, padx=10, pady=10)

    janela_principal.mainloop() #fica exibido até janela fechar


if __name__ =="__main__":
    main()