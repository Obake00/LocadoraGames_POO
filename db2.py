#Caso nao ter o alchemy na maquina, fazer a instalação primeiro pelo bash
#"pip install sqlalchemy"

from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from time import sleep

db = create_engine("sqlite:///locadora.db")                                 # Criando o banco e alocando em uma variavel
Session = sessionmaker(bind=db)                                             # Funciona como um "Commit"
session = Session()                                                         # Faz as alterações no banco

Base = declarative_base()                                                   # Cria o banco
    
class Cliente(Base):                                                        # Tabelas do banco
    __tablename__ = 'clientes'

    cpf = Column("CPF", Integer, primary_key=True)
    nome = Column("Nome", String)
    sexo = Column("Sexo", String)
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
    titulo = input("Digite o título do jogo: ").capitalize()
    modelo_fisico = input("Digite o modelo físico do jogo: ").capitalize()
    sistema = input("Digite o sistema do jogo: ").capitalize()
    classificacao = int(input("Digite a classificação do jogo (idade): "))
    genero = input("Digite o gênero do jogo: ").capitalize()
    desenvolvedora = input("Digite a desenvolvedora do jogo: ").capitalize()
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

    print("Processando. . .")
    sleep(2)
    print(f"O jogo '{titulo}' foi adicionado a estante!")
    os.system('pause')


def prateleira():
    jogos = session.query(Jogo).all()
    if len(jogos) == 0:
        print("Processando. . .")
        sleep(2)
        print(f"{'-'*56}")
        print("Não a jogos na prateleira!!")
        os.system('pause')
    else:
        print("Processando. . .")
        sleep(2)
        print(f"Total de jogos na prateleira:   {len(jogos)}")
        print("Processando. . .")
        sleep(2)
        print("-"*56)
    
        for jogo in jogos:
            print(f"- {jogo.titulo} -> {jogo.sistema}")

    os.system('pause')    


def add_cliente():
    while True:
        cpf = input("Digite o CPF do Cliente (11 dígitos): ")
        
        if cpf.isdigit() and len(cpf) == 11:
            cpf = int(cpf)
            nome = input("Digite o nome: ").capitalize()
            sexo = input("Digite o sexo: ").capitalize()
            
            while True:
                idade = input("Digite a idade: ")
                if idade.isdigit():
                    idade = int(idade)
                    break
                else:
                    print(f"Erro Idade inválida! Por favor, insira um número inteiro.")
            
            novo_cliente = Cliente(
                cpf=cpf,
                nome=nome,
                sexo=sexo,
                idade=idade
            )
            session.add(novo_cliente)
            session.commit()

            print("Processando. . .")
            sleep(2)
            print(f"Cliente {nome} adicionado ao sistema!")
            break
        else:
            print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")
    os.system('pause')


def listar_clientes():
    clientes = session.query(Cliente).all()
    if len(clientes) == 0:
        print("Não a clientes no Sistema!!")
    else:
        print(f"Total de Clientes no Sistema {len(clientes)}")
        print("-"*56)
        for cliente in clientes:
            print(f"- {cliente.nome}")
        os.system('pause')


def del_cliente():
    cpf = input("CPF do Cliente a ser deletado (11 dígitos): ")
    
    if cpf.isdigit() and len(cpf) == 11:
        cliente = session.query(Cliente).filter_by(cpf=int(cpf)).first()
        
        if cliente:
            session.delete(cliente)
            session.commit()
            print(f"Cliente {cliente.nome} deletado com sucesso!")
        else:
            print("Cliente não encontrado!")
    else:
        print("CPF inválido! O CPF deve ter exatamente 11 dígitos e ser um número.")


def main():
    while True:
        print(f"{10*'-='} L O C A D O R A {10*'=-'}")
        print(19*"-=-")
        print("[1] - Pratelheira de jogos")
        print("[2] - Adicionar Jogo")
        print("[3] - Adicionar Cliente")
        print("[4] - Clientes no Sistema")
        print("[5] - Excluir Cliente")
        print("[0] - Encerrar Sistema")
        print(13*"-=-")

        opcao = input("DIGITE OPÇÃO: ")
        if opcao == "1":
            prateleira()
        elif opcao == "2":
            add_jogo()
        elif opcao == "3":
            add_cliente()
        elif opcao == "4":
            listar_clientes()
        elif opcao == "5":
            del_cliente()    
        elif opcao == "0":
            print("Finalizando operação. . .")
            sleep(3)
            print(f"{10*'-='}  OBRIGADO  {10*'=-'}")
            break
        else:
            print(f"Opção Invalida erro 202")

if __name__ == "__main__":
    main()