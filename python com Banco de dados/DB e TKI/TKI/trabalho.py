from tkinter import *
from centraliza import center
from tkinter.ttk import *
import tkinter as tk 
from tkinter import ttk 
usuarios = []
veiculos= []
cidades= []
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_usuario():

    nome_usuario=usuarios[0].get()
    cpf=usuarios[1].get()
    ende=usuarios[2].get()
    cidade=usuarios[3].get()
    habilitacao=usuarios[4].get()
    cel=usuarios[5].get()    
    email=usuarios[6].get()
    
    print(nome_usuario,cpf,ende,cidade,habilitacao,cel,email)

def usuario():
    
    usuario= Toplevel()
    
    usuario.geometry("700x400")
   
    center (usuario)
   
    usuario.title("usuario")

    #cidade,habilitacao,cel,email

    lblnome = Label(usuario, text="nome:").grid(row=0,column=0,padx=5,pady=5)
    lblcpf = Label(usuario, text="cpf:").grid(row=1,column=0,padx=5,pady=5)
    lblende = Label(usuario, text="endereço:").grid(row=2,column=0,padx=5,pady=5)
    lblcidade = Label(usuario, text="cidade:").grid(row=3,column=0,padx=5,pady=5)
    lblhabilitacao = Label(usuario, text="habilitacao:").grid(row=4,column=0,padx=5,pady=5)
    lblcel = Label(usuario, text="cel:").grid(row=5,column=0,padx=5,pady=5)
    lblemail = Label(usuario, text="email:").grid(row=6,column=0,padx=5,pady=5)
 

    txtnome = Entry(usuario)
    txtnome.grid(row=0,column=1,padx=5,pady=5)

    txtcpf= Entry(usuario)
    txtcpf.grid(row=1,column=1,padx=5,pady=5)

    txtende = Entry(usuario)
    txtende.grid(row=2,column=1,padx=5,pady=5)

    txtcidade= Entry(usuario)
    txtcidade.grid(row=3,column=1,padx=5,pady=5)

    txthabilitacao= Entry(usuario)
    txthabilitacao.grid(row=4,column=1,padx=5,pady=5)

    txtcel = Entry(usuario)
    txtcel.grid(row=5,column=1,padx=5,pady=5)

    txtemail = Entry(usuario)
    txtemail.grid(row=6,column=1,padx=5,pady=5)

 
    usuarios.append(txtnome)
    usuarios.append(txtcpf)
    usuarios.append(txtende)
    usuarios.append(txthabilitacao)
    usuarios.append(txtcel)
    usuarios.append(txtemail)
    usuarios.append(txtcidade)


    btnSubmit= Button(usuario,text="submit",command=submit_usuario).grid(column=1,row=10,padx=5,pady=5)
    usuario.focus_set()
    usuario.grab_set()
    usuario.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_veiculo():
    ano=veiculos[0].get()
    placa=veiculos[1].get()
    modelo=veiculos[2].get()
    marca=veiculos[3].get()
    capacidade=veiculos[4].get()
    proprietario=veiculos[5].get()
    print(ano,placa,modelo,marca,capacidade,proprietario)

def veiculo():
    veiculo= Toplevel()
    
    veiculo.geometry("300x300")
   
    center (veiculo)
   
    veiculo.title("veiculo")

    lblano = Label(veiculo, text="ano:").grid(row=0,column=0,padx=5,pady=5)
    lblplaca = Label(veiculo, text="placa:").grid(row=1,column=0,padx=5,pady=5)
    lblmodelo = Label(veiculo, text="modelo:").grid(row=2,column=0,padx=5,pady=5)
    lblmarca = Label(veiculo, text="marca:").grid(row=3,column=0,padx=5,pady=5)
    lblcapacidade = Label(veiculo, text="capacidade:").grid(row=4,column=0,padx=5,pady=5)
    lblproprietario = Label(veiculo, text="proprietario:").grid(row=5,column=0,padx=5,pady=5)


    txtano = Entry(veiculo)
    txtano.grid(row=0,column=1,padx=5,pady=5)

    txtplaca= Entry(veiculo)
    txtplaca.grid(row=1,column=1,padx=5,pady=5)

    txtmodelo = Entry(veiculo)
    txtmodelo.grid(row=2,column=1,padx=5,pady=5)

    txtmarca = Entry(veiculo)
    txtmarca.grid(row=3,column=1,padx=5,pady=5)

    txtcapacidade = Entry(veiculo)
    txtcapacidade.grid(row=4,column=1,padx=5,pady=5)

    txtproprietario = Entry(veiculo)
    txtproprietario.grid(row=5,column=1,padx=5,pady=5)


    veiculos.append(txtano)
    veiculos.append(txtplaca)
    veiculos.append(txtmodelo)
    veiculos.append(txtmarca)
    veiculos.append(txtcapacidade)
    veiculos.append(txtproprietario)
    btnSubmit= Button(veiculo,text="submit",command=submit_veiculo).grid(row=6,column=0,padx=5,pady=5)

    veiculo.focus_set()
    veiculo.grab_set()
    veiculo.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit_cidade():
    uf=cidades[0].get()
    nome=cidades[1].get()
    print(uf,nome)

def cidade():
    cidade= Toplevel()
    cidade.geometry("300x200")
   
    center (cidade)
   
    cidade.title("cidade")

    lbluf = Label(cidade, text="uf:").grid(row=1,column=0,padx=5,pady=5)
    lblnome = Label(cidade, text="nome:").grid(row=2,column=0,padx=5,pady=5)

    txtuf= Entry(cidade)
    txtuf.grid(row=1,column=1,padx=5,pady=5)

    txtnome= Entry(cidade)
    txtnome.grid(row=2,column=1,padx=5,pady=5)

    cidades.append(txtuf)
    cidades.append(txtnome)

    btnSubmit= Button(cidade,text="submit", command=submit_cidade).grid(row=6,column=0,padx=5,pady=5)
    cidade.focus_set()
    cidade.grab_set()
    cidade.mainloop()
##------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():

    janela_principal =Tk()
    janela_principal.geometry("350x250")
    center(janela_principal)

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
