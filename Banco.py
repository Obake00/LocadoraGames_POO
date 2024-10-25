from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///locadora.db')                                 # Criando o banco e alocando em uma variavel
Session = sessionmaker(bind=db)                                             # Funciona como um "Commit"
session = Session()                                                         # Faz as alterações no banco

Base = declarative_base()                                                   # Cria o banco

class Cliente(Base):                                                        # Tabelas do banco
    __tabblename__ = 'clientes'

    cpf = Column("cpf", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    data_nascimento = Column("data_nascimento", Date)
    atendido = Column("atendido_por", ForeignKey("funcionarios.id_func"))

    def __init__(self,nome,data_nascimento,atendido):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.atendido = atendido


class Jogo(Base):
    __tabblename__ = 'jogos'

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
    __tabblename__ = 'funcionarios'

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
    __tabblename__ = 'pedidos'

    id_pedido = Column("id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("locação", Date)
    devolucao = Column("devolução", Date)

    def __init__(self,id_pedido,locacao,devolucao):
        self.id_pedido = id_pedido
        self.locacao = locacao
        self.devolucao = devolucao


class Endereco(Base):
    __tabblename__ = 'enderecos'

    cep = Column("cep", Integer, primary_key=True, autoincrement=True)
    fucnionario = Column("funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self,cep,funcionario):
        self.cep = cep
        self.fucnionario = funcionario

class Reserva(Base):
    __tabblename__ = 'reservas'

    id_reserva = Column("id_reserva", Integer, primary_key=True, autoincrement=True)
    valor = Column("valor", float)
    cfp_id = Column("cpf_id", ForeignKey("clientes.cpf"))
    pedido_id = Column("pedido_id", ForeignKey("pedidos.id_pedido"))
    jogo_id = Column("jogo_id", ForeignKey("jogos.id_jogo"))

    def __init__(self,id_reserva,valor,cpf_id,pedido_id,jogo_id):
        self.id_reserva = id_reserva
        self.valor = valor
        self.cpf_id = cpf_id
        self.pedido_id = pedido_id
        self.jogo_id = jogo_id



Base.metadata.create_all(bind=db)                                           # Cria tudo dentro do banco criado