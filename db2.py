#Caso nao ter o alchemy na maquina, fazer a instalação primeiro pelo bash
#"pip install sqlalchemy"

from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///locadora.db")                                 # Criando o banco e alocando em uma variavel
Session = sessionmaker(bind=db)                                             # Funciona como um "Commit"
session = Session()                                                         # Faz as alterações no banco

Base = declarative_base()                                                   # Cria o banco
    
class Cliente(Base):                                                        # Tabelas do banco
    __tablename__ = 'clientes'

    cpf = Column("CPF", Integer, primary_key=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    # atendido = Column("Atendido_por", ForeignKey("funcionarios.id_func"))

    def __init__(self,cpf,nome,idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        # self.atendido = atendido


class Jogo(Base):
    __tablename__ = 'jogos'

    id_jogo = Column("Id_jogo", Integer, primary_key=True, autoincrement=True)
    titulo = Column("Titulo", String)
    modelo_fisico = Column("Modelo_fisico", String)
    sistema = Column("Sistema", String)
    classi = Column("Classificação", Integer)
    genero = Column("Genero", String)
    desenv = Column("Desenvolvedora", String)
    preco = Column("Preço", Float)
    estado_aluguel = Column("Estado_aluguel", Boolean)

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
    nome = Column("Nome", String)
    turno = Column("Turno", String)
    idade = Column("Idade", Integer)

    def __init__(self,nome,turno,data_nascimento):

        self.nome = nome
        self.turno = turno
        self.data_nascimento = data_nascimento

class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column("Id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("Locação", Date)
    devolucao = Column("Devolução", Date)

    def __init__(self,locacao,devolucao):
        
        self.locacao = locacao
        self.devolucao = devolucao


class Endereco(Base):
    __tablename__ = 'enderecos'

    cep = Column("Cep", Integer, primary_key=True)
    funcionario = Column("Funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self,cep,funcionario):
        self.cep = cep
        self.fucnionario = funcionario






Base.metadata.create_all(bind=db)                                           # Cria tudo dentro do banco criado

#CRUD

def add_jogo():
    titulo = input("Digite o título do jogo: ")
    modelo_fisico = input("Digite o modelo físico do jogo: ")
    sistema = input("Digite o sistema do jogo: ")
    classificacao = int(input("Digite a classificação do jogo (idade): "))
    genero = input("Digite o gênero do jogo: ")
    desenvolvedora = input("Digite a desenvolvedora do jogo: ")
    preco = float(input("Digite o preço do jogo: "))

    novo_jogo = Jogo(
        titulo=titulo,
        modelo_fisico=modelo_fisico,
        sistema=sistema,
        classificacao=classificacao,
        genero=genero,
        desenvolvedora=desenvolvedora,
        preco=preco
    )
    session.add(novo_jogo)
    session.commit()

    print(f"O jogo '{titulo}' foi adicionado a estante!")


def prateleira():
    jogos = session.query(Jogo).all()
    if len(jogos) == 0:
        print("Não a jogos na prateleira!!")
    else:
        print(f"Total de jogos na prateleira {len(jogos)}")
        for jogo in jogos:
            print(f"{jogo.titulo} - {jogo.sistema}")


def add_cliente():
    cpf = int(input("Digite o CPF do CLiente: "))
    nome = input("Digite o nome: ")
    idade = int(input("Digite ano de nascimento "))

    novo_cliente = Cliente(
        cpf=cpf,
        nome=nome,
        idade=idade
    )
    session.add(novo_cliente)
    session.commit()

    print(f"Cliente {nome} adicionado ao sistema!")




def main():
    while True:
        print(f"{10*'-='} L O C A D O R A {10*'=-'}")
        print(19*"-=-")
        print("[1] - Pratelheira de jogos")
        print("[2] - Adicionar Jogo")
        print("[3] - Adicionar Cliente")
        print("[5] - Encerrar Sistema")
        print(13*"-=-")

        opcao = input("DIGITE OPÇÃO: ")
        if opcao == "1":
            prateleira()
        elif opcao == "2":
            add_jogo()
        elif opcao == "3":
            add_cliente()
        elif opcao == "5":
            print("Finalizando operação..\nOBRIGADO")
            break
        else:
            print("Opção Invalida erro 202")

if __name__ == "__main__":
    main()