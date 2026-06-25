class Carro:
    def __init__(self, cor, modelo, ano, velocidade_atual=0):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = velocidade_atual

# Objetos criados:
meu_carro = Carro(cor="Preto", modelo="Sedan", ano=2024)
carro_da_mae = Carro(cor="Vermelho", modelo="Hatch", ano=2025)

print('Dados do meu_carro:')
print(f'Cor: {meu_carro.cor}')
print(f'Modelo: {meu_carro.modelo}')
print(f'Ano: {meu_carro.ano}')
print(f'Velocidade Atual: {meu_carro.velocidade_atual}')

print('\nDados do carro_da_mae:')
print(f'Cor: {carro_da_mae.cor}')
print(f'Modelo: {carro_da_mae.modelo}')
print(f'Ano: {carro_da_mae.ano}')
print(f'Velocidade Atual: {carro_da_mae.velocidade_atual}')

