from tkinter import *
from centraliza import center
from tkinter.ttk import *


Usuarios = []
Veiculos = []
Cidades = []

cities_list = []

def submit_usuario():
    nome=Usuarios[0].get()
    cpf=Usuarios[1].get()
    telefone=Usuarios[2].get()
    print(nome,cpf,telefone)

#primeira janela é tk, a segunda é toplevel
def usuario():

    #janelas secundarias são criadas a partir da toplevel
    usuario= Toplevel()

    #tamanho
    usuario.geometry("500x350")

    #centraliza
    center (usuario)

    #titulo
    usuario.title("Usuario")

    #inclui campus
    lblnome = Label(usuario, text="nome:").grid(row=0,column=0,padx=5,pady=5)
    lblcpf = Label(usuario, text="cpf:").grid(row=1,column=0,padx=5,pady=5)
    lbltelefone = Label(usuario, text="telefone:").grid(row=2,column=0,padx=5,pady=5)


    txtNome = Entry(usuario)
    txtNome.grid(row=0,column=1,padx=5,pady=5)
    txtcpf = Entry(usuario)
    txtcpf.grid(row=1,column=1,padx=5,pady=5)
    txtTelefone = Entry(usuario)
    txtTelefone.grid(row=2,column=1,padx=5,pady=5)

    Usuarios.append(txtNome)
    Usuarios.append(txtcpf)
    Usuarios.append(txtTelefone)
    btnSubmit= Button(usuario,text="submit",command=submit_usuario).grid(row=1,column=2,padx=5,pady=5)


    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    usuario.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    usuario.grab_set()


    #teste
    city_listbox = Listbox(usuario)
    
    # Populate the Listbox with city names
    for city in cities_list:
        city_listbox.insert(END, city)
    
    city_listbox.grid(row=3, column=0)
    
    #deixar janela aberta 
    usuario.mainloop()

##-----------------------------------------------------------------------------------------------------------------------------------------------------------

def submit_veiculo():
    id=Veiculos[0].get()
    placa=Veiculos[1].get()
    modelo=Veiculos[2].get()
    print(id, placa, modelo)

#primeira janela é tk, a segunda é toplevel
def veiculo():

    #janelas secundarias são criadas a partir da toplevel
    veiculo= Toplevel()

    #tamanho
    veiculo.geometry("300x150")

    #centraliza
    center (veiculo)

    #titulo
    veiculo.title("veiculo")

    #inclui campus
    lblid = Label(veiculo, text="id:").grid(row=0,column=0,padx=5,pady=5)
    lblplaca = Label(veiculo, text="placa:").grid(row=1,column=0,padx=5,pady=5)
    lblmodelo = Label(veiculo, text="modelo:").grid(row=2,column=0,padx=5,pady=5)


    txtid = Entry(veiculo)
    txtid.grid(row=0,column=1,padx=5,pady=5)
    txtplaca= Entry(veiculo)
    txtplaca.grid(row=1,column=1,padx=5,pady=5)
    txtmodelo = Entry(veiculo)
    txtmodelo.grid(row=2,column=1,padx=5,pady=5)

    Veiculos.append(txtid)
    Veiculos.append(txtplaca)
    Veiculos.append(txtmodelo)
    btnSubmit= Button(veiculo,text="submit",command=submit_veiculo).grid(row=3,column=0,padx=5,pady=5)


    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    veiculo.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    veiculo.grab_set()

    
    #deixar janela aberta 
    veiculo.mainloop()
    
    ##-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
def submit_cidade():
    cod=Cidades[0].get()
    nome=Cidades[1].get()
    uf=Cidades[2].get()
    cities_list.append(nome)

#primeira janela é tk, a segunda é toplevel
def cidade():

    #janelas secundarias são criadas a partir da toplevel
    cidade= Toplevel()

    #tamanho
    cidade.geometry("300x150")

    #centraliza
    center (cidade)

    #titulo
    cidade.title("cidade")

    #inclui campus
    lblcod = Label(cidade, text="cod:").grid(row=0,column=0,padx=5,pady=5)
    lblnome = Label(cidade, text="nome:").grid(row=1,column=0,padx=5,pady=5)
    lbluf = Label(cidade, text="UF:").grid(row=2,column=0,padx=5,pady=5)


    txtcod = Entry(cidade)
    txtcod.grid(row=0,column=1,padx=5,pady=5)
    txtnome = Entry(cidade)
    txtnome.grid(row=1,column=1,padx=5,pady=5)
    txtuf = Entry(cidade)
    txtuf.grid(row=2,column=1,padx=5,pady=5)

    Cidades.append(txtcod)
    Cidades.append(txtnome)
    Cidades.append(txtuf)
    btnSubmit= Button(cidade,text="submit",command=submit_cidade).grid(row=3,column=0,padx=5,pady=5)

    #criar botão na segunda janela
    #btn = Button(segunda_janela, text="outro botão?",command=segunda_janela)
    #coloca o botão na primeira linha e coluna
    #btn.grid(row=3, column=0, padx=10, pady=10)
    #coloca o foco na segunda janela
    cidade.focus_set()

    #desabilita a janela principal enquanto a outra estiver aberta
    cidade.grab_set()



        
    
    #deixar janela aberta 
    cidade.mainloop()
    
    ##-----------------------------------------------------------------------------------------------------------------------------------------------------------
    
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
    btn = Button(janela_principal, text="User",command=usuario)
    btn2= Button(janela_principal, text="Car",command=veiculo)
    btn3 = Button(janela_principal, text="City",command=cidade)
    

    #coloca o botão na primeira linha e coluna
    #coluna
    btn.grid(row=0, column=0, padx=10, pady=10)
    btn2.grid(row=0, column=1, padx=10, pady=10)
    btn3.grid(row=0, column=3, padx=10, pady=10)

    janela_principal.mainloop() #fica exibido até janela fechar


if __name__ =="__main__":
    main()