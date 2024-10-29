class Locadora:
    def __init__ (Self, Nome):
        Self.Nome = Nome


class Funcionário:
    def __init__(self, Nome, ID_Func, Turno, Data_Nasc):
        self.Nome = Nome
        self.ID_Func = ID_Func
        self.Turno = Turno
        self.Data_Nasc = Data_Nasc

    
class Jogos:
    def __init__(self, Titulo, ID_Jogo, Estado_Fisico, Sistema, Classificacao, Genero, Desenvolvedora, Preco, Estado_aluguel):
        self.Titulo = Titulo
        self.ID_Jogo = ID_Jogo
        self.Estado_Fisico = Estado_Fisico
        self.Sistema = Sistema
        self.Classificacao = Classificacao
        self.Genero = Genero
        self.Desenvolvedora = Desenvolvedora
        self.Preco = Preco
        self.Estado_aluguel = Estado_aluguel

    
class Cliente:
    def __init__ (Self, Nome, Cpf, Data_Nascimento):
        Self.Nome = Nome
        Self.Cpf = Cpf
        Self.Data_Nascimento = Data_Nascimento

class Pedido:
    def __init__ (Self, ID_Pedido, Datas):
        Self.ID_Pedido = ID_Pedido
        Self.Datas = Datas

