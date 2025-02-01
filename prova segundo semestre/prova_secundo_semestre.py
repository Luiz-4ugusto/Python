class paciente:
    def __init__(self,cpf,nome,endereco,tel):
        self.cpf=cpf
        self.nome=nome
        self.endereco=endereco
        self.tel=tel
class secretaria (paciente):
    def __init__(self, cpf, nome, endereco, tel, email,senha):
        super().__init__(cpf, nome, endereco, tel)
        self.email=email
        self.senha=senha
    def __str__(self) -> str:
        return F" =secretaria=\n nome:{self.nome}\n CPF:{self.cpf}\n ende:{self.endereco}\n tel:{self.tel}\n Email:{self.email}\n Senha:{self.senha}"
class medico (secretaria):
    def __init__(self, cpf, nome, endereco, tel, email, senha,especialidade):
        super().__init__(cpf, nome, endereco, tel, email, senha)
        self.especialidade=especialidade
    def __str__(self):
        return F" =medico=\n nome:{self.nome}\n CPF:{self.cpf}\n ende:{self.endereco}\n tel:{self.tel}\n Email:{self.email}\n Senha:{self.senha}\n especialidade:{self.especialidade}"
class consulta:
    def __init__ (self,codigo,data,paciente,secretaria,medico,sintomas,medicamentos,valor):
        self.codigo=codigo
        self.data=data
        self.paciente=paciente
        self.secretaria=secretaria
        self.medico=medico
        self.sintomas=sintomas
        self.medicamentos=medicamentos
        self.valor=valor
    def __str__(self):
        return F"=consulta=\n codigo:{self.codigo}\n data:{self.data}\n paciente:{self.paciente}\n secretaria:{self.secretaria}\n medico:{self.medico}\n sintomas:{self.sintomas}\n medicamentos:{self.medicamentos}\n valor:{self.valor}"
nome1=paciente ("jacinto",123, "rua", 423)
nome2=paciente ("swf",133, "rua", 4223)
secretari1=secretaria ("cleyde", 321, "Ruasa",4334, "email", 2123)
medico1=medico("mario",3423,"ruaaaa", 564554, "mario email", 12121, "cirugia")

consulta1=consulta( 10, 10, nome1, secretari1,medico1, "dor", "remedio", "verde", )
consulta2=consulta( 102, 120, nome2, secretari1,medico1, "dor", "remedio", "verde")
if consulta1.valor>consulta2.valor:
    print(consulta1)
else:
    print(consulta2)
