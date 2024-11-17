class ContaBancaria:
    def __init__(self, titular):
        self._saldo = 0.0
        self._titular = titular

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido!")


    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria("João Silva")
conta.exibir_saldo()  
conta.depositar(1500)
conta.exibir_saldo()  
conta.sacar(300)     
conta.exibir_saldo()  
