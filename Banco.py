from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///locadora.db")                                 # Criando o banco e alocando em uma variavel
Session = sessionmaker(bind=db)                                             # Funciona como um "Commit"
session = Session()                                                         # Faz as alterações no banco

Base = declarative_base()                                                   # Cria o banco

class Cliente(Base):                                                        # Tabelas do banco

    cpf = Column("cpf", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    data_nascimento = Column("data_nascimento", Date)
    atendido = Column("atendido_por", ForeignKey("funcionarios.id_func"))

    def __init__(self,nome,data_nascimento,atendido):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.atendido = atendido


class Jogo(Base):

    id_jogo = Column("Id_jogo", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    estado_fisico = Column("estado_fisico", String)
    sistema = Column("sistema", String)
    classificacao = Column("classificação", String)
    genero = Column("genero", String)
    desenvolvedora = Column("desenvolvedora", String)
    preco = Column("estado_fisico", Float)
    estado_aluguel = Column("estado_aluguel", Boolean)

    def __init__(self,id_jogo,titulo,estado_fisico,sistema,classificacao,genero,desenvolvedora,preco,estado_aluguel=True):
        self.id_jogo = id_jogo
        self.titulo = titulo
        self.estado_fisico = estado_fisico
        self.sistema = sistema
        self.classificacao = classificacao
        self.genero = genero
        self.desenvolvedora = desenvolvedora
        self.preco = preco
        self.estado_aluguel = estado_aluguel


class Funcionario(Base):

    id_func = Column("id_func", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    turno = Column("turno", String)
    data_nascimento = Column("data_nascimento", Date)

    def __init__(self,id_func,nome,turno,data_nascimento):
        
        self.id_func = id_func
        self.nome = nome
        self.turno = turno
        self.data_nascimento = data_nascimento

class Pedido(Base):

    id_pedido = Column("id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("locação", Date)
    devolucao = Column("devolução", Date)

    def __init__(self,id_pedido,locacao,devolucao):
        self.id_pedido = id_pedido
        self.locacao = locacao
        self.devolucao = devolucao


class Endereco(Base):

    cep = Column("cep", Integer, primary_key=True, autoincrement=True)
    fucnionario = Column("funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self,cep,funcionario):
        self.cep = cep
        self.fucnionario = funcionario

class Reserva(Base):

    id_reserva = Column("id_reserva", Integer, primary_key=True, autoincrement=True)
    valor = Column("valor", float)
    cfpr = Column("cpf", ForeignKey("clientes.cpf"))
    id_pedidor = Column("id_pedido", ForeignKey("pedidos.id_pedido"))
    id_jogor = Column("id_jogo", ForeignKey("jogos.id_jogos"))

    def __init__(self,id_reserva,valor,cpfr,id_pedidor,id_jogor):
        self.id_reserva = id_reserva
        self.valor = valor
        self.cpfr = cpfr
        self.id_pedidor = id_pedidor
        self.id_jogor = id_jogor



Base.metadata.create_all(bind=db)                                           # Cria tudo dentro do banco criado