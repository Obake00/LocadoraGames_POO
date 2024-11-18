# ProjetoLocadora_POO

O sistema de locadora de jogos é configurado com um banco de dados SQLite utilizando SQLAlchemy. Ele é composto por cinco modelos de dados:

Cliente: Armazena CPF, nome, sexo e idade dos clientes.
Jogo: Contém informações sobre jogos, incluindo título, modelo físico, sistema, classificação, gênero, desenvolvedora, preço e status.
Funcionário: Registra dados dos funcionários, como ID, nome e estado de turno (ativo/inativo).
Pedido: Representa locações, associando clientes, jogos e funcionários.
Endereço: Armazena informações de endereço dos funcionários.
As principais funções do sistema incluem adicionar e listar funcionários e jogos, registrar e gerenciar clientes, processar locações e devoluções de jogos. Menus interativos facilitam a navegação entre essas funcionalidades.

A função principal inicia o sistema e apresenta um menu ao funcionário autenticado, permitindo que ele gerencie as operações do dia a dia da locadora. As funcionalidades abrangem autenticação de funcionários, gerenciamento de clientes e jogos, além do processo de locação e devolução de jogos.
