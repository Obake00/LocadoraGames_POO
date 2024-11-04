from sqlalchemy import create_engine, Column, Integer, Float, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///locadora.db")                                 # Criando o banco e alocando em uma variavel
Session = sessionmaker(bind=db)                                             # Funciona como um "Commit"
session = Session()                                                         # Faz as alterações no banco

Base = declarative_base()                                                   # Cria o banco

class Cliente(Base):                                                        # Tabelas do banco
    __tablename__ = 'clientes'

    cpf = Column("cpf", Integer, primary_key=True)
    nome = Column("nome", String)
    data_nascimento = Column("data_nascimento", Date)
    atendido = Column("atendido_por", ForeignKey("funcionarios.id_func"))

    def __init__(self,cpf,nome,data_nascimento,atendido):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.atendido = atendido


class Jogo(Base):
    __tablename__ = 'jogos'

    id_jogo = Column("Id_jogo", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    modelo_fisico = Column("modelo_fisico", String)
    sistema = Column("sistema", String)
    classi = Column("classificação", Integer)
    genero = Column("genero", String)
    desenv = Column("desenvolvedora", String)
    preco = Column("preço", Float)
    estado_aluguel = Column("estado_aluguel", Boolean)

    def __init__(self,titulo,modelo_fisico,sistema,classificacao,genero,desenvolvedora,preco,estado_aluguel=True):
        
        self.titulo = titulo
        self.modelo_fisico = modelo_fisico
        self.sistema = sistema
        self.classi = classificacao
        self.genero = genero
        self.desenv = desenvolvedora
        self.preco = preco
        self.estado_aluguel = estado_aluguel


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id_func = Column("id_func", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    turno = Column("turno", String)
    data_nascimento = Column("data_nascimento", Date)

    def __init__(self,nome,turno,data_nascimento):

        self.nome = nome
        self.turno = turno
        self.data_nascimento = data_nascimento

class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column("id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("locação", Date)
    devolucao = Column("devolução", Date)

    def __init__(self,locacao,devolucao):
        
        self.locacao = locacao
        self.devolucao = devolucao


class Endereco(Base):
    __tablename__ = 'enderecos'

    cep = Column("cep", Integer, primary_key=True)
    funcionario = Column("funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self,cep,funcionario):
        self.cep = cep
        self.fucnionario = funcionario






Base.metadata.create_all(bind=db)                                           # Cria tudo dentro do banco criado

# funçoes

def add_jogo(titulo,modelo_fisico,sistema,classi,genero,desenv,preco):
    jogo = session.query(Jogo)




# def main():

#     while True:
#         print("LOCADORA")
#         print(20*"=")
#         print("Listar Jogos tecle [1]")

#         opcao = input("Opção: ")
#         if opcao == '1':