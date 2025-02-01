import sqlite3 as sql
from tkinter import *
from centraliza import center
from tkinter import ttk

c = {
    'nome': None,
    'uf': None
}

u = {
    'nome': None,
    'cidade': None,
    'endereço': None,
    'cpf': None,
    'habilitação': None,
    'celular': None
}

v = {
    'marca' : None,
    'modelo': None,
    'placa': None,
    'ano' : None,
    'capacidade' : None,
    'proprietario' : None
}

def create_database():
    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cidades(nome text, uf text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS usuario(id INTEGER PRIMARY KEY, nome text, cidade text, endereco text, cpf text, habilitacao text, celular text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS veiculos(marca, modelo, placa, ano, capacidade, proprietario)')
    banco.commit()
    banco.close()

def Subimit_cidade():
    nome = c['nome'].get()
    uf = c['uf'].get()

    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO cidades VALUES (?, ?)', (nome, uf))
    banco.commit()
    banco.close()

def Subimit_usuario():
    nome = u['nome'].get()
    cidade = u['cidade'].get()
    endereco = u['endereço'].get()
    cpf = u['cpf'].get()
    habilitacao = u['habilitação'].get()
    celular = u['celular'].get()

    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO usuario(nome, cidade, endereco, cpf, habilitacao, celular) VALUES (?, ?, ?, ?, ?, ?)', (nome, cidade, endereco, cpf, habilitacao, celular))
    banco.commit()
    banco.close()

def Subimit_veiculo():
    marca = v['marca'].get()
    modelo = v['modelo'].get()
    placa = v['placa'].get()
    ano = v['ano'].get()
    capacidade = v['capacidade'].get()
    proprietario = v['proprietario'].get()

    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO veiculos VALUES (?, ?, ?, ?, ?, ?)', (marca,modelo,placa,ano,capacidade,proprietario))
    banco.commit()
    banco.close()

def Cadastrar_cidade():
    cadastrar_cidade = Toplevel()
    cadastrar_cidade.geometry('300x150')
    center(cadastrar_cidade)
    cadastrar_cidade.title('Cadastrar Cidade')
    cadastrar_cidade.focus_set()
    cadastrar_cidade.grab_set()

    lblNome = Label(cadastrar_cidade, text='Nome: ')
    lblNome.grid(row=0, column=0, padx=5, pady=5)
    lblUF = Label(cadastrar_cidade, text='UF: ')
    lblUF.grid(row=1, column=0, padx=5, pady=5)

    c['nome'] = StringVar()
    c['uf'] = StringVar()

    txtNome = Entry(cadastrar_cidade, textvariable=c['nome'])
    txtNome.grid(row=0, column=1, padx=5, pady=5)
    txtUF = Entry(cadastrar_cidade, textvariable=c['uf'])
    txtUF.grid(row=1, column=1, padx=5, pady=5)

    btnSubmit = Button(cadastrar_cidade, text='Submit', command=Subimit_cidade)
    btnSubmit.grid(row=3, column=1, padx=5, pady=5)

    cadastrar_cidade.mainloop()

def Cidade_db():
    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute('SELECT nome FROM cidades')
    rows = cursor.fetchall()
    options = [row[0] for row in rows]
    banco.close()
    return options

def Cadastrar_usuario():
    cadastrar_usuario = Toplevel()
    cadastrar_usuario.geometry("300x350")
    center(cadastrar_usuario)
    cadastrar_usuario.title('Cadastrar Usuário')
    cadastrar_usuario.focus_set()
    cadastrar_usuario.grab_set()

    opc = Cidade_db()

    lblNome = Label(cadastrar_usuario, text='Nome: ')
    lblNome.grid(row=0, column=0, padx=5, pady=5)
    lblCidade = Label(cadastrar_usuario, text='Cidade: ')
    lblCidade.grid(row=1, column=0, padx=5, pady=5)
    lblEndereco = Label(cadastrar_usuario, text='Endereço: ')
    lblEndereco.grid(row=2, column=0, padx=5, pady=5)
    lblCPF = Label(cadastrar_usuario, text='CPF: ')
    lblCPF.grid(row=3, column=0, padx=5, pady=5)
    lblHabilitacao = Label(cadastrar_usuario, text='Habilitação: ')
    lblHabilitacao.grid(row=4, column=0, padx=5, pady=5)
    lblCelular = Label(cadastrar_usuario, text='Celular: ')
    lblCelular.grid(row=5, column=0, padx=5, pady=5)

    u['nome'] = StringVar()
    u['cidade'] = StringVar()
    u['endereço'] = StringVar()
    u['cpf'] = StringVar()
    u['habilitação'] = StringVar()
    u['celular'] = StringVar()

    txtNome = Entry(cadastrar_usuario, textvariable=u['nome'])
    txtNome.grid(row=0, column=1, padx=5, pady=5)
    txtCidade = ttk.Combobox(cadastrar_usuario, values=opc, textvariable=u['cidade'])
    txtCidade.grid(row=1, column=1, padx=5, pady=5)
    txtEndereco = Entry(cadastrar_usuario, textvariable=u['endereço'])
    txtEndereco.grid(row=2, column=1, padx=5, pady=5)
    txtCPF = Entry(cadastrar_usuario, textvariable=u['cpf'])
    txtCPF.grid(row=3, column=1, padx=5, pady=5)
    txtHabilitacao = Entry(cadastrar_usuario, textvariable=u['habilitação'])
    txtHabilitacao.grid(row=4, column=1, padx=5, pady=5)
    txtCelular = Entry(cadastrar_usuario, textvariable=u['celular'])
    txtCelular.grid(row=5, column=1, padx=5, pady=5)

    btnSubmit = Button(cadastrar_usuario, text='Submit', command=Subimit_usuario)
    btnSubmit.grid(row=7, column=1, padx=5, pady=5)

    cadastrar_usuario.mainloop()

def Usuario_db():
    banco = sql.connect('viagens.db')
    cursor = banco.cursor()
    cursor.execute('SELECT nome FROM usuario')
    rows = cursor.fetchall()
    options = [row[0] for row in rows]
    banco.close()
    return options

def Cadastrar_veiculo():
    cadastrar_veiculo = Toplevel()
    cadastrar_veiculo.geometry("600x350")
    center(cadastrar_veiculo)
    cadastrar_veiculo.title('Cadastrar Veículo')
    cadastrar_veiculo.focus_set()
    cadastrar_veiculo.grab_set()

    opc = Usuario_db()

    lblMarca = Label(cadastrar_veiculo,text='Marca: ')
    lblMarca.grid(row=0, column=0, padx=5, pady=5)
    lblModelo = Label(cadastrar_veiculo,text='Modelo: ')
    lblModelo.grid(row=1, column=0, padx=5, pady=5)
    lblPlaca = Label(cadastrar_veiculo,text='Placa: ')
    lblPlaca.grid(row=2, column=0, padx=5, pady=5)
    lblAno = Label(cadastrar_veiculo,text='Ano: ')
    lblAno.grid(row=3, column=0, padx=5, pady=5)
    lblCapacidade = Label(cadastrar_veiculo, text='Capacidade: ')
    lblCapacidade.grid(row=4, column=0, padx=5, pady=5)
    lblProprietario = Label(cadastrar_veiculo,text='Proprietário: ')
    lblProprietario.grid(row=5, column=0, padx=5, pady=5)

    v['marca'] = StringVar()
    v['modelo'] = StringVar()
    v['placa'] = StringVar()
    v['ano'] = StringVar()
    v['capacidade'] = StringVar()
    v['proprietario'] = StringVar()

    txtMarca = Entry(cadastrar_veiculo, textvariable = v['marca'])
    txtMarca.grid(row=0,column=1,padx=5,pady=5)
    txtModelo = Entry(cadastrar_veiculo, textvariable=v['modelo'])
    txtModelo.grid(row=1, column=1, padx=5, pady=5)
    txtPlaca = Entry(cadastrar_veiculo, textvariable=v['placa'])
    txtPlaca.grid(row=2, column=1, padx=5, pady=5)
    txtAno = Entry(cadastrar_veiculo, textvariable=v['ano'])
    txtAno.grid(row=3, column=1, padx=5, pady=5)
    txtCapacidade = Entry(cadastrar_veiculo, textvariable=v['capacidade'])
    txtCapacidade.grid(row=4, column=1, padx=5, pady=5)
    txtProprietario = ttk.Combobox(cadastrar_veiculo, values=(opc), textvariable=v['proprietario'])
    txtProprietario.grid(row=5, column=1, padx=5, pady=5)

    btnSubimit = Button(cadastrar_veiculo, text='Submit', command=Subimit_veiculo)
    btnSubimit.grid(row=6,column=1,padx=5,pady=5) 

def main():
    janela_principal = Tk()
    janela_principal.geometry("400x200")
    center(janela_principal)
    janela_principal.title("Janela Principal")

    create_database()

    btnCadastrar_Cidade = Button(janela_principal, text='Cadastrar Cidade', command=Cadastrar_cidade)
    btnCadastrar_Cidade.grid(row=0, column=0, padx=10, pady=10)
    btnCadastrar_Usuario = Button(janela_principal, text='Cadastrar Usuário', command=Cadastrar_usuario)
    btnCadastrar_Usuario.grid(row=0, column=1, padx=10, pady=10)
    btnCadastrar_Veiculo = Button(janela_principal, text='Cadastrar Veículo', command=Cadastrar_veiculo)
    btnCadastrar_Veiculo.grid(row=0, column=2, padx=10, pady=10)

    janela_principal.mainloop()

if __name__ == '__main__':
    main()