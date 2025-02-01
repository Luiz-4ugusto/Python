#Luiz Augusto Pereira

from tkinter import *
from centraliza import center
from tkinter.ttk import *
usuarios = []
veiculos= []
cidades= []
cities_list = ["PL","SC","SP"]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_usuario():
    nome=usuarios[0].get()
    cpf=usuarios[1].get()
    ende=usuarios[2].get()
    print(nome,cpf,ende)

def usuario():
    usuario= Toplevel()
    
    usuario.geometry("500x300")
   
    center (usuario)
   
    usuario.title("usuario")

    lblnome = Label(usuario, text="nome:").grid(row=0,column=0,padx=5,pady=5)
    lblcpf = Label(usuario, text="cpf:").grid(row=1,column=0,padx=5,pady=5)
    lblende = Label(usuario, text="ende:").grid(row=2,column=0,padx=5,pady=5)

    txtnome = Entry(usuario)
    txtnome.grid(row=0,column=1,padx=5,pady=5)

    txtcpf= Entry(usuario)
    txtcpf.grid(row=1,column=1,padx=5,pady=5)

    txtende = Entry(usuario)
    txtende.grid(row=2,column=1,padx=5,pady=5)

    usuarios.append(txtnome)
    usuarios.append(txtcpf)
    usuarios.append(txtende)
    btnSubmit= Button(usuario,text="submit",command=submit_usuario).grid(row=2,column=2,padx=5,pady=5)

    usuario.focus_set()
    usuario.grab_set()
    city_listbox = Listbox(usuario)
    
    # Populate the Listbox with city names
    for city in cities_list:
        city_listbox.insert(END, city)
    
    city_listbox.grid(row=3, column=0)

    usuario.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_veiculo():
    id=veiculos[0].get()
    placa=veiculos[1].get()
    modelo=veiculos[2].get()
    print(id,placa,modelo)

def veiculo():
    veiculo= Toplevel()
    
    veiculo.geometry("300x300")
   
    center (veiculo)
   
    veiculo.title("veiculo")

    lblid = Label(veiculo, text="id:").grid(row=0,column=0,padx=5,pady=5)
    lblplaca = Label(veiculo, text="placa:").grid(row=1,column=0,padx=5,pady=5)
    lblmodelo = Label(veiculo, text="modelo:").grid(row=2,column=0,padx=5,pady=5)

    txtid = Entry(veiculo)
    txtid.grid(row=0,column=1,padx=5,pady=5)

    txtplaca= Entry(veiculo)
    txtplaca.grid(row=1,column=1,padx=5,pady=5)

    txtmodelo = Entry(veiculo)
    txtmodelo.grid(row=2,column=1,padx=5,pady=5)

    veiculos.append(txtid)
    veiculos.append(txtplaca)
    veiculos.append(txtmodelo)
    btnSubmit= Button(veiculo,text="submit",command=submit_veiculo).grid(row=6,column=0,padx=5,pady=5)

    veiculo.focus_set()
    veiculo.grab_set()
    veiculo.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_cidade():
    uf=cidades[0].get()
    cod=cidades[1].get()
    nome=cidades[2].get()
    print(uf,cod,nome)

def cidade():
    cidade= Toplevel()
    
    cidade.geometry("300x300")
   
    center (cidade)
   
    cidade.title("cidade")

    lbluf = Label(cidade, text="uf:").grid(row=0,column=0,padx=5,pady=5)
    lblcod = Label(cidade, text="cod:").grid(row=1,column=0,padx=5,pady=5)
    lblnome = Label(cidade, text="nome:").grid(row=2,column=0,padx=5,pady=5)

    txtnome = Entry(cidade)
    txtnome.grid(row=0,column=1,padx=5,pady=5)

    txtuf= Entry(cidade)
    txtuf.grid(row=1,column=1,padx=5,pady=5)

    txtcod = Entry(cidade)
    txtcod.grid(row=2,column=1,padx=5,pady=5)

    cidades.append(txtnome)
    cidades.append(txtuf)
    cidades.append(txtcod)
    btnSubmit= Button(cidade,text="submit",command=submit_cidade).grid(row=6,column=0,padx=5,pady=5)

    cidade.focus_set()
    cidade.grab_set()
    cidade.mainloop()
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():

    janela_principal =Tk()


    janela_principal.geometry("605x780")


    center(janela_principal)

    city_listbox = Listbox(janela_principal)
    

    for city in cities_list:
        city_listbox.insert(END, city)
    

    def select_city():
        selected_index = city_listbox.curselection()
        if selected_index:
            selected_city = city_listbox.get(selected_index[0])
            print("Selected City:", selected_city)


    janela_principal.title("janela")

    btn = Button(janela_principal, text="usuario",command=usuario)
    btn1 = Button(janela_principal, text="veiculo",command=veiculo)
    btn2 = Button(janela_principal, text="cidade",command=cidade)

    
    btn.grid(row=0, column=0, padx=10, pady=10)
    btn1.grid(row=0, column=1, padx=10, pady=10)
    btn2.grid(row=0, column=2, padx=10, pady=10)
    janela_principal.mainloop() 


if __name__ =="__main__":
    main()

print(cities_list[0])