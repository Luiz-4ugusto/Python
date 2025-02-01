##Alunos: Lucas, Luiz, Igor, Henrique d Souza


class CPessoa: 
    def __init__(self, id, nome, endereco, tel, email):
        self.id=id
        self.nome=nome
        self.endereco=endereco
        self.tel=tel
        self.email=email

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Pessoa==
        |id:{self.id}
        |Nome:{self.Nome}
        |Endereco:{self.Endereco}
        |Tel:{self.Tel}
        |email:{self.email}
         {50*"-"}
        """

class CPaciente (CPessoa): 
    def __init__(self, id, nome, endereco, tel, email, data_cadastro, ultima_consulta):
        super().__init__(id, nome, endereco, tel, email)
        self.data_cadastro=data_cadastro
        self.ultima_consulta=ultima_consulta

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Paciente==
        |data_cadastro:{self.data_cadastro}
        |ultima_consulta:{self.ultima_consulta}
        |id:{self.id}
        |nome:{self.nome}
        |endereco:{self.endereco}
        |tel:{self.tel}
        |email:{self.email}
         {50*"-"}
        """

class CSecretaria (CPessoa):
    def __init__(self, id, nome, endereco, tel, email, contratacao, turma):
        super().__init__(id, nome, endereco, tel, email)
        self.contratacao = contratacao
        self.turma = turma

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Secretaria==
        |contratacao:{self.contratacao}
        |turma:{self.turma}
        |id:{self.id}
        |nome:{self.nome}
        |endereco:{self.endereco}
        |tel:{self.tel}
        |email:{self.email}
         {50*"-"}
        """

class CMedico (CPessoa):
    def __init__(self,id, nome, endereco, tel, email, crm, especialidade):
        super().__init__(id, nome, endereco, tel, email)
        self.crm=crm
        self.especialidade=especialidade

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Medico==
        |crm:{self.crm}
        |especialidade:{self.especialidade}
        |id:{self.id}
        |nome:{self.nome}
        |endereco:{self.endereco}
        |tel:{self.tel}
        |email:{self.email}
         {50*"-"}
        """

class CHAorariotendimento:
    def __init__ (self, id, dia, turno):
        self.id=id
        self.dia=dia
        self.turno=turno

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Horario Atendimento==
        |id:{self.id}
        |dia:{self.dia}
        |turno:{self.turno}
         {50*"-"}
        """
    
class CLab: 
    def __init__(self, id, nome, endereco, tel, email):
        self.id=id
        self.nome=nome
        self.endereco=endereco
        self.tel=tel
        self.email=email
    
    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Laboratorio==
        |id:{self.id}
        |nome:{self.nome}
        |endereco:{self.endereco}
        |tel:{self.tel}
        |email:{self.email}
         {50*"-"}
        """
    
class CMedicamento: 
    def __init__(self, id, nome, efeito, descricao):
        self.id=id
        self.nome=nome
        self.efeito=efeito
        self.descricao=descricao

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Medicamento==
        |id:{self.id}
        |nome:{self.nome}
        |efeito:{self.efeito}
        |descricao:{self.descricao}
         {50*"-"}
        """
    
        
class CPrescricao: 
    def __init__(self, id, modoUSO, medicamento):
        self.id=id
        self.modoUSO=modoUSO
        self.medicamento = medicamento

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Prescricao==
        |id:{self.id}
        |modoUSO:{self.modoUSO}
        |Nome do remedio:{self.medicamento.nome}
         {50*"-"}
        """
    
class CConsulta: 
    def __init__(self, id, data, horario, sintoma, diagnostico, convenio, tipo):
        self.id = id
        self.data = data
        self.horario = horario
        self.sintoma = sintoma
        self.diagnostico = diagnostico
        self.prescricoes = []  # Lista de prescrições
        self.convenio = convenio
        self.tipo = tipo

    def adicionar_prescricao(self, prescricao):
        self.prescricoes.append(prescricao)

    def __str__(self) -> str:
        consulta_str = f"""
        {50*"-"}
        |==Consulta==
        |id:{self.id}
        |data:{self.data}
        |horario:{self.horario}
        |sintoma:{self.sintoma}
        |diagnostico:{self.diagnostico}
        |convênio: {self.convenio.nome}
        |tipo: {self.tipo.consulta}
        |Prescrições:
        """

        for prescricao in self.prescricoes:
            consulta_str += f"\n|  - Nome do remédio: {prescricao.medicamento.nome}"

        consulta_str += f"\n{50*'-'}"

        return consulta_str

    
class CTipo: 
    def __init__(self, consulta,retorno):
        self.consulta=consulta
        self.retorno=retorno

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Tipo==
        |consulta:{self.consulta}
        |retorno:{self.retorno}
         {50*"-"}
        """
    
class CConvenio: 
    def __init__(self, id,nome):
        self.id=id
        self.nome=nome

    def __str__(self) -> str:
        return f"""
        {50*"-"}
        |==Convenio==
        |id:{self.id}
        |nome:{self.nome}
         {50*"-"}
        """

paciente1 = CPaciente( '01', 'Jorgin', 'Rua','99224432', 'Jorgindelas@gmail.com', '28-10-2013', '21-09-2015')

secretaria1 = CSecretaria('02', 'Joana',  'Casa', '323232', 'Joaninha@gmail.com', '20-03-2012', 'Noite') 

medico1 = CMedico('03', 'Mario',  'Hospital', '99995533', 'doctorwho@gmail.com', 'CRM/SP 123456', 'Cirurgião')

horarioatendimento = CHAorariotendimento('04','22-02-2015', 'Tarde, Noite')

lab1 = CLab('05','Tiradentes', 'Hospital', '489932332', 'nopainnogain@hotmail.com')

medicamento1 = CMedicamento('1', 'Aspirina', 'Analgésico', 'Reduz a dor e a inflamação')
medicamento2 = CMedicamento('10', 'Dipirona', 'Passa fome', 'Efeito rápido, e cura fácil')
tipo1 = CTipo('Otorrino', 'Nunca')

prescicao1 = CPrescricao('076', 'Ingerir a cada 8h em 8h', medicamento1)
prescicao2 = CPrescricao('22', 'ingerir 2 vezes ao dia', medicamento2)
convenio1 = CConvenio('022', 'Unimed')

consulta1 = CConsulta('9', '20-02-2000', 'Ao entardecer', 'fortes dores', 'ferido', convenio1, tipo1)

consulta1.adicionar_prescricao(prescicao1)
consulta1.adicionar_prescricao(prescicao2)
print(paciente1)
print(secretaria1)
print(medico1)
print(horarioatendimento)
print(lab1)
print(medicamento1)
print(prescicao1)
print(consulta1)
print(convenio1)
print(tipo1)

