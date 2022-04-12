# Criando os dados que serão inseridos na tabela.
# Classe com o construtor.
# usuario = NomeDaTabela('Felipe', 35, 'Masculino')
# usuarios = [NomeDaTabela('Maria', 20, 'Feminino'), NomeDaTabela('Pedro', 50, 'Masculino')]

# Caso não seja utilizado o construtor na classe
# os dados são passados depois de se criar a instancia.
# usuario = NomeDaTabela()
# usuario.nome = 'Camila'
# usuario.idade = 50
# usuario.sexo = 'Feminino'

# Inserindo registro na tabela.
# session.add(usuario)

# Inserindo vários registros na tabela.
# session.add_all(usuarios)

# Persistindo os dados.
# session.commit()

# Consultar todos os registros.
# dados = session.query(NomeDaTabela).all()
# print(dados)
# for linha in dados:
#     print(f'Nome: {linha.nome} - Idade: {linha.idade} - Sexo: {linha.sexo}')

# Consulta registros com filtro.
# dados = session.query(NomeDaTabela).filter(NomeDaTabela.idade > 40).all()
# print(dados)
# for linha in dados:
#     print(f'Nome: {linha.nome} - Idade: {linha.idade} - Sexo: {linha.sexo}')

# Alterar um registro da tabela.
# print('Nome ANTES da alteração:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one().nome)
# session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).update({'nome': 'Roberto'})
# session.commit()
# print('Nome DEPOIS da alteração:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one().nome)

# Remover um registro da tabela.
# print('Registro ANTES da remoção:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one_or_none())
# session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).delete()
# session.commit()
# print('Registro DEPOIS da remoção:', session.query(NomeDaTabela).filter(NomeDaTabela.id == 1).one_or_none())
