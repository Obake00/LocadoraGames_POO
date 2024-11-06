# Caso nao ter o alchemy na maquina, fazer a instalação primeiro pelo bash
# "pip install sqlalchemy"

from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from time import sleep

# Configuração do banco de dados
db = create_engine("sqlite:///locadora.db")  # Criando o banco de dados
Session = sessionmaker(bind=db)                # Funciona como um "Commit"
session = Session()                            # Faz as alterações no banco

Base = declarative_base()                      # Cria a base do banco
    
class Cliente(Base):                           # Tabelas do banco
    __tablename__ = 'clientes'

    cpf = Column("CPF", Integer, primary_key=True)
    nome = Column("Nome", String)
    sexo = Column("Sexo", String)
    idade = Column("Idade", Integer)

    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade


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

    def __init__(self, titulo, modelo_fisico, sistema, classificacao, genero, desenvolvedora, preco, estado_aluguel=True):
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

    id_func = Column("id_func", Integer, primary_key=True)
    nome = Column("Nome", String)
    turno = Column("Turno", Boolean)

    def __init__(self, id_func, nome, turno=False):
        self.id_func = id_func
        self.nome = nome
        self.turno = turno


class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column("Id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("Locação", Date)
    devolucao = Column("Devolução", Date)

    def __init__(self, locacao, devolucao):
        self.locacao = locacao
        self.devolucao = devolucao


class Endereco(Base):
    __tablename__ = 'enderecos'

    cep = Column("Cep", Integer, primary_key=True)
    funcionario = Column("Funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self, cep, funcionario):
        self.cep = cep
        self.funcionario = funcionario


# Função para adicionar funcionários base
def funcionarios_base():
    funcionarios_base = [
        Funcionario(id_func=1010, nome="Caique Diniz"),
        Funcionario(id_func=2020, nome="Jhonata Almeida"),
        Funcionario(id_func=3030, nome="Maiki Ferreira")
    ]

    for funcionario in funcionarios_base:
        existente = session.query(Funcionario).filter_by(id_func=funcionario.id_func).first()
        if not existente:
            session.add(funcionario)

    session.commit()
    print("Funcionários base adicionados ao sistema.")


def listar_funcionarios():
    funcionarios = session.query(Funcionario).all()
    print("Lista de Funcionários:")
    print(f"{'- -'*19}")
    for funcionario in funcionarios:
        print(f"ID: {funcionario.id_func}      Funcionario: {funcionario.nome}")


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
    print(f"O jogo '{titulo}' foi adicionado à estante!")
    os.system('pause')


def prateleira():
    while True:
        print("Escolha uma opção:")
        print("[1] - Mostrar todos os jogos")
        print("[2] - Mostrar jogos de cartucho")
        print("[3] - Mostrar jogos de CD")
        print("[0] - Voltar ao menu principal")

        opcao = input("DIGITE OPÇÃO: ")
        
        if opcao == "1":
            jogos = session.query(Jogo).all()
            if len(jogos) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'-'*56}")
                print("Não há jogos na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos na prateleira: {len(jogos)}")
                print(f"{'- -'*19}")
                for jogo in jogos:
                    print(f"- {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "2":
            jogos_cartucho = session.query(Jogo).filter_by(modelo_fisico="Cartucho").all()
            if len(jogos_cartucho) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'- -'*19}")
                print("Não há jogos de cartucho na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos de cartucho: {len(jogos_cartucho)}")
                print("-"*56)
                for jogo in jogos_cartucho:
                    print(f"- {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "3":
            jogos_cd = session.query(Jogo).filter_by(modelo_fisico="CD").all()
            if len(jogos_cd) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'- -'*19}")
                print("Não há jogos de CD na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos de CD: {len(jogos_cd)}")
                print(f"{'- -'*19}")
                for jogo in jogos_cd:
                    print(f"- {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "0":
            break  # Sai do loop e retorna ao menu principal

        else:
            print("Opção inválida! Tente novamente.")


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
                    print("Erro: Idade inválida! Por favor, insira somente números.")
            
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

            # Listar clientes após a adição para verificação
            listar_clientes()
            break
        else:
            print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")
    os.system('pause')


def listar_clientes():
    clientes = session.query(Cliente).all()
    if len(clientes) == 0:
        print("Processando. . .")
        sleep(2)
        print("Não há clientes no Sistema!!")
        os.system('pause')
    else:
        print(f"Total de Clientes no Sistema: {len(clientes)}")
        print("-"*56)
        for cliente in clientes:
            print(f"- {cliente.nome} (CPF: {cliente.cpf})")  # Incluindo CPF para melhor identificação
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


def acesso():
    listar_funcionarios()  # Mostra a lista de funcionários

    # Solicita o ID do funcionário
    while True:
        id_func = input("Use ID para login: ")
        
        if id_func.isdigit():
            id_func = int(id_func)
            funcionario = session.query(Funcionario).filter_by(id_func=id_func).first()
            if funcionario:
                if not funcionario.turno:  # Se o turno for inativo
                    funcionario.turno = True  # Ativa o turno
                    session.commit()
                    print(f"Acesso concedido! Bem-vindo {funcionario.nome}. Turno ativado.")
                    return funcionario  # Retorna o funcionário para desativar depois
                else:
                    print("Esse funcionário já está ativo.")
                    return None
            else:
                print("ID inválido!")
        else:
            print("Por favor, insira um ID válido.")


def main(funcionario_ativo):
    while True:
        print(f"{10*'-='} L O C A D O R A {10*'=-'}")
        print(19*"-=-")
        print("[1] - Prateleira de jogos")
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
            # Desativa o turno do funcionário ao encerrar
            funcionario_ativo.turno = False
            session.commit()
            print("Encerrando acesso. . .")
            sleep(2)
            print("Finalizando Operação. . .")
            sleep(3)
            print(f"{10*'-='}  OBRIGADO  {10*'=-'}")
            break
        else:
            print(f"Opção Inválida, erro 202")


# Função principal que inicia o banco e todo o sistema
if __name__ == "__main__":
    Base.metadata.create_all(bind=db)
    funcionarios_base()
    
    # Verifica acesso antes de iniciar o sistema
    funcionario_ativo = acesso()
    if funcionario_ativo:
        main(funcionario_ativo)