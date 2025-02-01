from tkinter import *
from centraliza import center
from tkinter.ttk import *
cds = []
livros=[]

def submit_CD():
    isbn=cds[0].get()
    cod=cds[1].get()
    desc=cds[2].get()
    autor=cds[3].get()
    preco=cds[4].get()
    estoque=cds[5].get()
    print(isbn,cod,desc,autor,preco,estoque)
#primeira janela é tk, a segunda é toplevel
def dvd():

    #janelas secundarias são criadas a partir da toplevel
    dvd= Toplevel()

    #tamanho
    dvd.geometry("300x300")

    #centraliza
    center (dvd)

    #titulo
    dvd.title("cd")

    #inclui campus
    lblisbn = Label(dvd, text="isbn:").grid(row=0,column=0,padx=5,pady=5)
    lblcod = Label(dvd, text="cod:").grid(row=1,column=0,padx=5,pady=5)
    lbldesc = Label(dvd, text="desc:").grid(row=2,column=0,padx=5,pady=5)
    lblautor = Label(dvd, text="autor:").grid(row=3,column=0,padx=5,pady=5)
    lblpreco = Label(dvd, text="preco:").grid(row=4,column=0,padx=5,pady=5)
    lblestoque = Label(dvd, text="estoque:").grid(row=5,column=0,padx=5,pady=5)

    txtisbn = Entry(dvd)
    txtisbn.grid(row=0,column=1,padx=5,pady=5)

    txtcod= Entry(dvd)
    txtcod.grid(row=1,column=1,padx=5,pady=5)

    txtdesc = Entry(dvd)
    txtdesc.grid(row=2,column=1,padx=5,pady=5)

    txtautor = Entry(dvd)
    txtautor.grid(row=3,column=1,padx=5,pady=5)

    txtpreco= Entry(dvd)
    txtpreco.grid(row=4,column=1,padx=5,pady=5)

    txtestoque = Entry(dvd)
    txtestoque.grid(row=5,column=1,padx=5,pady=5)

    cds.append(txtisbn)
    cds.append(txtcod)
    cds.append(txtdesc)
    cds.append(txtautor)
    cds.append(txtpreco)
    cds.append(txtestoque)
    btnSubmit= Button(dvd,text="submit",command=submit_CD).grid(row=6,column=0,padx=5,pady=5)


    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    dvd.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    dvd.grab_set()

    
    #deixar janela aberta 
    dvd.mainloop()
def submit_livro():
    isbn=livros[0].get()
    cod=livros[1].get()
    desc=livros[2].get()
    autor=livros[3].get()
    preco=livros[4].get()
    estoque=livros[5].get()
    print(isbn,cod,desc,autor,preco,estoque)
#primeira janela é tk, a segunda é toplevel
def livro():

    #janelas secundarias são criadas a partir da toplevel
    livro= Toplevel()

    #tamanho
    livro.geometry("300x300")

    #centraliza
    center (livro)

    #titulo
    livro.title("livro")

    #inclui campus
    lblisbn = Label(livro, text="isbn:").grid(row=0,column=0,padx=5,pady=5)
    lblcod = Label(livro, text="cod:").grid(row=1,column=0,padx=5,pady=5)
    lbldesc = Label(livro, text="desc:").grid(row=2,column=0,padx=5,pady=5)
    lblautor = Label(livro, text="autor:").grid(row=3,column=0,padx=5,pady=5)
    lblpreco = Label(livro, text="preco:").grid(row=4,column=0,padx=5,pady=5)
    lblestoque = Label(livro, text="estoque:").grid(row=5,column=0,padx=5,pady=5)

    txtisbn = Entry(livro)
    txtisbn.grid(row=0,column=1,padx=5,pady=5)

    txtcod= Entry(livro)
    txtcod.grid(row=1,column=1,padx=5,pady=5)

    txtdesc = Entry(livro)
    txtdesc.grid(row=2,column=1,padx=5,pady=5)

    txtautor = Entry(livro)
    txtautor.grid(row=3,column=1,padx=5,pady=5)

    txtpreco= Entry(livro)
    txtpreco.grid(row=4,column=1,padx=5,pady=5)

    txtestoque = Entry(livro)
    txtestoque.grid(row=5,column=1,padx=5,pady=5)

    livros.append(txtisbn)
    livros.append(txtcod)
    livros.append(txtdesc)
    livros.append(txtautor)
    livros.append(txtpreco)
    livros.append(txtestoque)
    btnSubmit1= Button(livro,text="submit",command=submit_livro).grid(row=6,column=0,padx=5,pady=5)


    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    livro.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    livro.grab_set()

    
    #deixar janela aberta 
    livro.mainloop()
def main():
    #cria a janela principal
    janela_principal =Tk()

    #DEFINE O TAMANHO DA JANELA
    janela_principal.geometry("500x250")

    #CENTRALIZA A JANELA NA TELA
    center(janela_principal)

    #DEFINE O TITULO DA JANELA
    janela_principal.title("janela")

    #criar botão usando a class button
    btn = Button(janela_principal, text="dvd",command=dvd)
    btn1 = Button(janela_principal, text="livro",command=livro)
    #coloca o botão na primeira linha e coluna
    #coluna
    btn.grid(row=0, column=0, padx=10, pady=10)
    btn1.grid(row=0, column=1, padx=10, pady=10)
    janela_principal.mainloop() #fica exibido até janela fechar


if __name__ =="__main__":
    main()