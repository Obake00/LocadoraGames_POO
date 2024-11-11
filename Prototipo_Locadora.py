# Instalando o Alchemy na máquina
# "pip install sqlalchemy"

from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from time import sleep
from datetime import datetime, timedelta

# Configuração do banco de dados
db = create_engine("sqlite:///locadora.db")  
Session = sessionmaker(bind=db)                
session = Session()                            

Base = declarative_base()                      

# Tabela referente aos Clientes
class Cliente(Base):                           
    __tablename__ = 'clientes'

    cpf = Column("CPF", Integer, primary_key=True)
    nome = Column("Nome", String)
    sexo = Column("Sexo", String)
    idade = Column("Idade", Integer)

    def __init__(self, cpf, nome, sexo, idade):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

# Tabela referente ao cadastro dos jogos
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
    status = Column("Status", Boolean)

    def __init__(self, titulo, modelo_fisico, sistema, classificacao, genero, desenvolvedora, preco, status=True):
        self.titulo = titulo
        self.modelo_fisico = modelo_fisico
        self.sistema = sistema
        self.classi = classificacao
        self.genero = genero
        self.desenv = desenvolvedora
        self.preco = preco
        self.status = status

# Tabela referente aos Funcionarios
class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id_func = Column("id_func", Integer, primary_key=True)
    nome = Column("Nome", String)
    turno = Column("Turno", Boolean)

    def __init__(self, id_func, nome, turno=False):
        self.id_func = id_func
        self.nome = nome
        self.turno = turno

# Tabela referente aos Pedidos realizados pelos clientes para com os funcionarios
class Pedido(Base):
    __tablename__ = 'pedidos'

    id_pedido = Column("Id_pedido", Integer, primary_key=True, autoincrement=True)
    locacao = Column("Locação", Date)
    devolucao = Column("Devolução", Date)
    cpf_cliente = Column("CPF_Cliente", ForeignKey("clientes.CPF"))
    id_jogo = Column("Id_Jogo", ForeignKey("jogos.Id_jogo"))
    id_func = Column("Id_Funcionario", ForeignKey("funcionarios.id_func"))

    def __init__(self, locacao, devolucao, cpf_cliente, id_jogo, id_func):
        self.locacao = locacao
        self.devolucao = devolucao
        self.cpf_cliente = cpf_cliente
        self.id_jogo = id_jogo
        self.id_func = id_func


# Parte de Funções de manipulação das informações

# Função que adiciona funcionarios à locadora assim que inicia o sistema
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
    print("Iniciando. . . ")
    sleep(2)

# Função retorna os funcionarios no sistema( funcionarios ja definidos)
def listar_funcionarios():
    funcionarios = session.query(Funcionario).all()
    print("Lista de Funcionários:")
    print(f"{'- -'*40}")
    for funcionario in funcionarios:
        print(f"ID: {funcionario.id_func}      Funcionario: {funcionario.nome}")
    os.system('pause')

# Função que adiciona jogos a prateleira, jogos com o mesmo nome, nao entram
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

# Jogos ja pre definidos no sistema, quando iniciado o banco a lista ja é instanciado
def prateleira_base():
    jogos_base = [
        Jogo(titulo="Alladin", modelo_fisico="Cartucho", sistema="Snes", classificacao=10, genero="Aventura", desenvolvedora="Capcom", preco=10),
        Jogo(titulo="Banjo-Tooie", modelo_fisico="Cartucho", sistema="N64", classificacao=7, genero="Aventura", desenvolvedora="Rare", preco=20),
        Jogo(titulo="Black", modelo_fisico="Cd", sistema="Ps2", classificacao=18, genero="Fps", desenvolvedora="Criterion Games", preco=15),
        Jogo(titulo="Bully", modelo_fisico="Cd", sistema="Ps2", classificacao=14, genero="Aventura", desenvolvedora="Rockstar Games", preco=15),
        Jogo(titulo="Crash Bandicoot", modelo_fisico="Cd", sistema="Ps1", classificacao=10, genero="Aventura", desenvolvedora="Naughty Dog", preco=15),
        Jogo(titulo="Dino Crisis 2", modelo_fisico="Cd", sistema="Ps1", classificacao=12, genero="Ação/Aventura", desenvolvedora="Capcom", preco=18),
        Jogo(titulo="FIFA 13", modelo_fisico="Cd", sistema="Ps3", classificacao=3, genero="Esporte", desenvolvedora="EA Sports", preco=25),
        Jogo(titulo="God of War II", modelo_fisico="Cd", sistema="Ps2", classificacao=18, genero="Ação/Aventura", desenvolvedora="Santa Monica Studio", preco=25),
        Jogo(titulo="Grand Theft Auto - San Andreas", modelo_fisico="Cd", sistema="Ps2", classificacao=18, genero="Ação/Aventura", desenvolvedora="Rockstar North", preco=20),
        Jogo(titulo="Legend of Zelda - The Ocarina of Time", modelo_fisico="Cartucho", sistema="N64", classificacao=10, genero="Aventura", desenvolvedora="Nintendo", preco=30),
        Jogo(titulo="Mickey Mouse - Castle of Illusion", modelo_fisico="Cartucho", sistema="Sega Genesis", classificacao=7, genero="Plataforma", desenvolvedora="Sega", preco=15),
        Jogo(titulo="Mortal Kombat 3", modelo_fisico="Cartucho", sistema="Snes", classificacao=18, genero="Luta", desenvolvedora="Midway Games", preco=10),
        Jogo(titulo="NBA 2K16", modelo_fisico="Cd", sistema="Ps3", classificacao=3, genero="Esporte", desenvolvedora="Visual Concepts", preco=30),
        Jogo(titulo="NBA Jam", modelo_fisico="Cartucho", sistema="Snes", classificacao=10, genero="Esporte", desenvolvedora="Midway Games", preco=15),
        Jogo(titulo="Perfect Dark", modelo_fisico="Cartucho", sistema="N64", classificacao=12, genero="Fps", desenvolvedora="Rare", preco=25),
        Jogo(titulo="Pro Evolution Soccer 2011", modelo_fisico="Cd", sistema="Ps3", classificacao=3, genero="Esporte", desenvolvedora="Konami", preco=20),
        Jogo(titulo="Resident Evil 3 - Nemesis", modelo_fisico="Cd", sistema="Ps1", classificacao=18, genero="Survival Horror", desenvolvedora="Capcom", preco=18),
        Jogo(titulo="Resident Evil 4", modelo_fisico="Cd", sistema="Ps2", classificacao=18, genero="Survival Horror", desenvolvedora="Capcom", preco=20),
        Jogo(titulo="Shinobi", modelo_fisico="Cartucho", sistema="Sega Genesis", classificacao=10, genero="Ação", desenvolvedora="Sega", preco=12),
        Jogo(titulo="Sonic the Hedgehog", modelo_fisico="Cartucho", sistema="Sega Genesis", classificacao=7, genero="Plataforma", desenvolvedora="Sega", preco=12),
        Jogo(titulo="Sonic the Hedgehog 2", modelo_fisico="Cartucho", sistema="Sega Genesis", classificacao=7, genero="Plataforma", desenvolvedora="Sega", preco=12),
        Jogo(titulo="Star Fox 64", modelo_fisico="Cartucho", sistema="N64", classificacao=10, genero="Aventura", desenvolvedora="Nintendo", preco=30),
        Jogo(titulo="Super Mario 64", modelo_fisico="Cartucho", sistema="N64", classificacao=10, genero="Plataforma", desenvolvedora="Nintendo", preco=30),
        Jogo(titulo="Super Mario World", modelo_fisico="Cartucho", sistema="Snes", classificacao=10, genero="Plataforma", desenvolvedora="Nintendo", preco=20),
        Jogo(titulo="Super Monaco GP", modelo_fisico="Cartucho", sistema="Sega Genesis", classificacao=7, genero="Corrida", desenvolvedora="Codemasters", preco=15),
        Jogo(titulo="Tekken 3", modelo_fisico="Cd", sistema="Ps1", classificacao=12, genero="Luta", desenvolvedora="Bandai Namco", preco=20),
        Jogo(titulo="The Last of Us", modelo_fisico="Cd", sistema="Ps3", classificacao=18, genero="Ação/Aventura", desenvolvedora="Naughty Dog", preco=30),
        Jogo(titulo="Top Gear", modelo_fisico="Cartucho", sistema="Snes", classificacao=7, genero="Corrida", desenvolvedora="Gremlin Interactive", preco=15),
        Jogo(titulo="Winning Eleven 2001", modelo_fisico="Cd", sistema="Ps2", classificacao=3, genero="Esporte", desenvolvedora="Konami", preco=20)
    ]
    for jogo in jogos_base:
        existente = session.query(Jogo).filter_by(titulo=jogo.titulo).first()
        if not existente:
            session.add(jogo)

    session.commit()


def clientes_base():
    clientes_base = [
        Cliente(cpf="12345678910", nome="Joaquim", sexo="M", idade=21),
        Cliente(cpf="23456789011", nome="Maria", sexo="F", idade=24),
        Cliente(cpf="34567890122", nome="Carlos", sexo="F", idade=18),
        Cliente(cpf="45678901233", nome="Bernadete", sexo="M", idade=20)
    ]
    for cliente in clientes_base:
        existente = session.query(Cliente).filter_by(cpf=cliente.cpf).first()
        if not existente:
            session.add(cliente)

    session.commit()

# Função de login dos funcionarios, muda o estado do funcionario para "ativo", e quando encerra muda o estado para "inativo", so e acessado por funcionarios ja no sistema.
def acesso():
    listar_funcionarios()

    while True:
        id_func = input("Use ID para login: ")
        
        if id_func.isdigit():
            id_func = int(id_func)
            funcionario = session.query(Funcionario).filter_by(id_func=id_func).first()
            if funcionario:
                if not funcionario.turno:
                    funcionario.turno = True
                    session.commit()
                    print("Acessando. . .")
                    sleep(2)
                    print(f"Acesso concedido! Bem-vindo: {funcionario.nome}  -> TURNO ATIVO")
                    sleep(2)
                    return funcionario
                else:
                    print("Finalizando seu turno....")
                    sleep(2)
                    print(f"Tenha um ótimo descanso {funcionario.nome}!")
                    funcionario.turno = False
                    session.commit()
            else:
                print("ID inválido!")
        else:
            print("Por favor, insira um ID válido.")

# Função mostrar todos os jogos no banco, com opção por filtro de Cd e Cartucho
def prateleira():
    while True:
        print("Escolha uma opção:")
        print("[1] - Mostrar todos os jogos")
        print("[2] - Mostrar jogos de Cartucho")
        print("[3] - Mostrar jogos de Cd")
        print("[0] - Voltar ao menu principal")

        opcao = input("DIGITE OPÇÃO: ")
        
        if opcao == "1":
            jogos = session.query(Jogo).all()
            if len(jogos) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'- -'*40}")
                print("Não há jogos na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos na prateleira: {len(jogos)}")
                print(f"{'- -'*40}")
                for jogo in jogos:
                    print(f" - {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "2":
            jogos_cartucho = session.query(Jogo).filter_by(modelo_fisico="Cartucho").all()
            if len(jogos_cartucho) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'- -'*40}")
                print("Não há jogos de cartucho na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos de cartucho: {len(jogos_cartucho)}")
                print("-"*56)
                for jogo in jogos_cartucho:
                    print(f" - {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "3":
            jogos_cd = session.query(Jogo).filter_by(modelo_fisico="Cd").all()
            if len(jogos_cd) == 0:
                print("Processando. . .")
                sleep(2)
                print(f"{'- -'*40}")
                print("Não há jogos de CD na prateleira!!")
                os.system('pause')
            else:
                print("Processando. . .")
                sleep(2)
                print(f"Total de jogos de CD: {len(jogos_cd)}")
                print(f"{'- -'*40}")
                for jogo in jogos_cd:
                    print(f" - {jogo.titulo} -> {jogo.sistema}")

                os.system('pause')

        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

# Adiciona Clientes ao Sistema, um jogo so pode ser alugado por clientes ja cadastrados
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
            print(f"|{nome}|   adicionado ao sistema!")
            break
        else:
            print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")
    os.system('pause')

# Lista os clientes no sistema para pesquisa
def listar_clientes():
    clientes = session.query(Cliente).all()
    if len(clientes) == 0:
        print("Processando. . .")
        sleep(2)
        print("Não há clientes no Sistema!!")
        os.system('pause') #os.system('pause') é uma funcao do python para pausar o codigo até o usuario pressionar uma tecla
    else:
        print(f"Total de Clientes no Sistema: {len(clientes)}")
        print("-"*56)
        for cliente in clientes:
            print(f"- {cliente.nome} (CPF: {cliente.cpf})")
        os.system('pause')


def atualizar_cliente():
    listar_clientes()
    cpf = input("Digite o CPF do Cliente a ser atualizado: ")
    
    if cpf.isdigit() and len(cpf) == 11:
        cliente = session.query(Cliente).filter_by(cpf=int(cpf)).first()
        
        if cliente:
            print(f"Dados atuais de {cliente.nome}:")
            print(f"Nome: {cliente.nome}")
            print(f"Sexo: {cliente.sexo}")
            print(f"Idade: {cliente.idade}")
            
            
            novo_nome = input("Digite novo Nome (ENTER para manter atual): ").capitalize()
            if novo_nome:
                cliente.nome = novo_nome
            
            novo_sexo = input("Digite novo sexo (ENTER para manter atual): ").capitalize()
            if novo_sexo:
                cliente.sexo = novo_sexo
            
            nova_idade = input("Digite nova idade (ENTER para manter atual): ")
            if nova_idade.isdigit():
                cliente.idade = int(nova_idade)

            session.commit()
            print("Dados atualizados com sucesso!")
            print(f" Nome: {cliente.nome} Idade: {cliente.idade} Sexo: {cliente.sexo}")
        else:
            print("Cliente não encontrado!")
    else:
        print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")

    os.system('pause')
# Deleta o Cliente no sistema atraves do CPF
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
# Atualiza o Funcionario no sistema atraves do ID 
def atualizar_funcionario():
    listar_funcionarios()
    sleep(2)
    id_func = input("Use ID do funcionario a ser atualizado: ")
    if id_func.isdigit():
        id_func = int(id_func)
        funcionario = session.query(Funcionario).filter_by(id_func=id_func).first()
        
        if funcionario:
            print(f"Nome: {funcionario.nome}")
            print(f"ID: {funcionario.id_func}")

            novo_nome = input("Digite o novo nome do funcionario (ENTER para manter o nome atual): ").capitalize()
            if novo_nome:
                funcionario.nome = novo_nome
            novo_id = input("Digite o novo ID do funcionario (ENTER para manter o ID atual): ")
            if novo_id.isdigit():
                funcionario.id_func = int(novo_id)
            session.commit()

            print("Dados atualizados com sucesso!")
            print(f" Nome: {funcionario.nome} ID: {funcionario.id_func}")  
        else:
            print("Usuario não encontrado!")
    else:
        print("ID inválido! O ID deve ser um número.")

# Adiciona um jogo a tabela aluguel
def alugar_jogo(funcionario_ativo):
    listar_clientes()
    sleep(1)
    cpf_cliente = input("Digite o CPF do Cliente (11 dígitos): ")
    
    if cpf_cliente.isdigit() and len(cpf_cliente) == 11:
        cliente = session.query(Cliente).filter_by(cpf=int(cpf_cliente)).first()
        if cliente:
            jogos_alugados = []
            total_valor = 0.0
            sleep(1)
            while True:
                jogos = session.query(Jogo).all()
                for jogo in jogos:
                    statusPrint = "Disponível" if jogo.status else "Indisponível"
                    print(f"ID|{jogo.id_jogo}|   Titulo: {jogo.titulo}   Sistema de uso: {jogo.sistema}   Status: {statusPrint}")
                print(f"{'- -' * 40}")

                id_jogo = input("Digite o ID do jogo para aluguel ou '0' para finalizar: ")
                if id_jogo == '0':
                    break

                print("Processando . . .")
                sleep(2)

                if id_jogo.isdigit():
                    jogo = session.query(Jogo).filter_by(id_jogo=int(id_jogo)).first()
                    if jogo and jogo.status:
                        locacao = datetime.now().date()
                        devolucao = locacao + timedelta(weeks=1)

                        novo_pedido = Pedido(locacao=locacao, devolucao=devolucao, cpf_cliente=cliente.cpf, id_jogo=jogo.id_jogo, id_func=funcionario_ativo.id_func)
                        session.add(novo_pedido)

                        jogo.status = False
                        session.commit()

                        jogos_alugados.append(jogo)
                        total_valor += jogo.preco

                        print(f"Jogo {jogo.titulo} Sistema: {jogo.sistema} alugado para {cliente.nome} até {devolucao}. Valor: R${jogo.preco}")
                    else:
                        print(f"Jogo {id_jogo} não disponível para aluguel.")
                else:
                    print("ID de jogo inválido!")
            
            if jogos_alugados:
                print("Processando . . .")
                sleep(3)
                print("\nAlugados:")
                print(f"{'- -' * 40}")
                for jogo in jogos_alugados:
                    print(f"- {jogo.titulo} -> {jogo.sistema} -> {jogo.modelo_fisico} -> R${jogo.preco}")
                print(f"Total jogos reservados: {len(jogos_alugados)} Valor total R$: {total_valor:.2f}")
            else:
                print("Nenhum jogo no pedido.")
        else:
            print("Cliente não encontrado!")
    else:
        print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")
    os.system('pause')

# Exclui um funcionario da tabela *Funcionario* a partir do ID do digitado
def excluir_funcionario():
    listar_funcionarios()
    sleep(2)
    id_func = input("Use ID do funcionario a ser excluido: ")
    if id_func.isdigit():
        id_func = int(id_func)
        funcionario = session.query(Funcionario).filter_by(id_func=id_func).first()
        if funcionario:
            print(f" Nome: {funcionario.nome} ID: {funcionario.id_func}")  
            session.delete(funcionario)
            print(f"Funcionario excluído com sucesso!")
            session.commit()
        else:
            print("Funcionario nao encontrado!")
    else:
        print("ID inválido! O ID deve ser um número.")

def adicionar_funcionario():
    listar_funcionarios()
    sleep(2)
    id_nome = input("Digite o nome do funcionario: ").capitalize()
    senha = input("Digite o ID do funcionario: ")

    novo_funcionario = Funcionario(
                nome=id_nome,
                id_func=senha
            )
    session.add(novo_funcionario)
    session.commit()


def listar_pedidos():
    pedidos = session.query(Pedido).all()
    if len(pedidos) == 0:
        print("Processando . . .")
        sleep(2)
        print("Não há pedidos")
    else:
        print("Processando. . .")
        sleep(2)
        print("Lista de Pedidos:")
        print(f"{'- -'*40}")
        for pedido in pedidos:
            cliente = session.query(Cliente).filter_by(cpf=pedido.cpf_cliente).first()
            jogo = session.query(Jogo).filter_by(id_jogo=pedido.id_jogo).first()
            if cliente and jogo:
                print(f"ID Pedido: {pedido.id_pedido}    Cliente: {cliente.nome}    Jogo: {jogo.titulo}    Devolução: {pedido.devolucao}    Funcionario responsavel: {pedido.id_func}")
    os.system('pause')

# deleta o pedido da tabela
def devolver_jogo():
    listar_clientes()
    cpf_cliente = input("Digite o CPF do Cliente (11 dígitos): ")
    
    if cpf_cliente.isdigit() and len(cpf_cliente) == 11:
        cliente = session.query(Cliente).filter_by(cpf=int(cpf_cliente)).first()
        if cliente:
            pedidos = session.query(Pedido).filter_by(cpf_cliente=cliente.cpf).all()
            if pedidos:
                print("Pedidos Ativos:")
                print(f"{'- -'*40}")
                for pedido in pedidos:
                    jogo = session.query(Jogo).filter_by(id_jogo=pedido.id_jogo).first()
                    if jogo:
                        print(f"ID Pedido: {pedido.id_pedido}    Jogo: {jogo.titulo}    Devolução: {pedido.devolucao}")
                
                id_pedido = input("Digite o ID do pedido que deseja devolver: ")
                print("Processando. . .")
                sleep(2)
                if id_pedido.isdigit():
                    pedido = session.query(Pedido).filter_by(id_pedido=int(id_pedido)).first()
                    if pedido:
                        jogo = session.query(Jogo).filter_by(id_jogo=pedido.id_jogo).first()
                        if jogo:
                            jogo.status = True
                            session.delete(pedido)
                            session.commit()
                            print("Aguarde. . .")
                            sleep(2)
                            print(f"Jogo: {jogo.titulo} Sistema: {jogo.sistema}    devolvido com sucesso!")
                        else:
                            print("Jogo não encontrado!")
                    else:
                        print("Pedido não encontrado!")
                else:
                    print("ID de pedido inválido!")
            else:
                print("Não há pedidos ativos para esse cliente.")
        else:
            print("Cliente não encontrado!")
    else:
        print("CPF inválido! O CPF deve conter 11 dígitos, somente números.")
    os.system('pause')


#Menu Principal de inicialização de sistema!
def main(funcionario_ativo):
    while True:
        print(f"{10*'-='} L O C A D O R A {10*'=-'}")
        print(f"{'- -'*40}")
        print("[1] - Prateleira de jogos")
        print("[2] - Adicionar Jogo")
        print("[3] - Alugar Jogos")
        print("[4] - Devolver Jogo")
        print("[5] - Lista de Pedidos")
        print("[6] - Adicionar cliente")
        print("[7] - Excluir cliente")
        print("[8] - Cliente no sistema")
        print("[9] - Atualizar Cliente")
        print("[10]- Lista de Funcionários")
        print("[11]- Atualizar Funcionário")
        print("[12]- Adicionar Funcionario")
        print("[13]- Demitir Funcionario")
        print("[0] - Encerrar Sistema")
        print(f"{'- -'*40}")

        opcao = input("DIGITE OPÇÃO: ")
        if opcao == "1":
            prateleira()
        elif opcao == "2":
            add_jogo()
        elif opcao == "3":
            alugar_jogo(funcionario_ativo)
        elif opcao == "4":
            devolver_jogo()
        elif opcao == "5":
            listar_pedidos()  
        elif opcao == "6":
            add_cliente
        elif opcao == "7":
            del_cliente()
        elif opcao == "8":
            listar_clientes()
        elif opcao == "9":
            atualizar_cliente()
        elif opcao == "10":
            listar_funcionarios()
        elif opcao == "11":
            atualizar_funcionario()
        elif opcao == "12":
            adicionar_funcionario()
        elif opcao == "13":
            excluir_funcionario()

        elif opcao == "0":  
            funcionario_ativo.turno = False
            session.commit()
            print("Encerrando acesso. . .")
            sleep(2)
            print("Finalizando Operação. . .")
            sleep(3)
            print(f"{20*'-='}  OBRIGADO  {20*'=-'}")
            break
        else:
            print(f"Opção Inválida, erro 202")


#Função principal que inicia o banco e todo o sistema
if __name__ == "__main__":
    Base.metadata.create_all(bind=db) # Cria as tabelas declaradas no banco, sem esse comando, nenhuma tabela seria criada
    funcionarios_base()
    prateleira_base()
    clientes_base()
    
    funcionario_ativo = acesso()
    if funcionario_ativo:
        main(funcionario_ativo)
