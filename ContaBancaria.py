class ContaBancaria:
    #Função (def) 
    #Objeto (titular, saldo_inicial)
    def __init__(self, titular: str,  saldo_inicial: float = 0.0):
        #Instância da classe (self)
        self.titular = titular
        #Acesso privado (__saldo)
        self.__saldo = saldo_inicial
    #Método consultar saldo
    def get_saldo(self) -> float:
        return self.__saldo
    #Método depositar dinheiro
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.__saldo += valor
            print(f'Valor de R${valor: .2f} depositado')
        else:  
            print("Não é permitido efetuar deposito negativo")
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Erro: Não é possivel sacar valores negativos")
            return False
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque efetuado com sucesso de R${valor: .2f}.')
            return True
        else:
            print("Saldo insuficiente!")
#Herança
class Poupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial = 0, taxa_juros: float = 0.005):
        super().__init__(titular, saldo_inicial)
        self.taxa_juros = taxa_juros
    def reder_juros(self) -> None:
        saldo_atual = self.get_saldo()
        juros = saldo_atual * self.taxa_juros
        self.depositar(juros)
        print(f'O seu rendimento foi de R${juros: .2f}')

# --- Testar o código --> próximo passo alunos!
