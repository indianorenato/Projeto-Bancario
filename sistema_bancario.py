import getpass
import time

class ContaBancaria:
    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.data_nascimento = ""
        self.agencia = ""
        self.conta = ""
        self.saldo = 0
        self.saques_realizados = []
        self.depositos_realizados = []
        self.senha_deposito = "1234"  # Senha padrão para o depósito

    def depositar(self, valor):
        if valor <= 0:
            print('O valor do depósito deve ser maior que zero.')
            self.error_message('Algo deu errado. Tente novamente.')
            return

        senha_digitada = getpass.getpass('Digite sua senha de 4 dígitos para confirmar o depósito: ')
        if senha_digitada != self.senha_deposito:
            print('Senha incorreta.')
            return

        self.saldo += valor
        self.depositos_realizados.append(valor)
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        self.show_thanks()

    def sacar(self, valor):
        if len(self.saques_realizados) >= 3:
            print('Você já atingiu o limite diário de saques.')
            self.error_message('Algo deu errado. Tente novamente.')
            return
        if valor > 500:
            print('O valor máximo por saque é de R$500.')
            self.error_message('Algo deu errado. Tente novamente.')
            return
        if self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
            self.error_message('Algo deu errado. Tente novamente.')
            return

        senha_digitada = getpass.getpass('Digite sua senha de 4 dígitos para confirmar o saque: ')
        if senha_digitada != self.senha_deposito:
            print('Senha incorreta.')
            return

        self.saldo -= valor
        self.saques_realizados.append(valor)
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        self.show_thanks()

    def extrato(self):
        print(f'Extrato da conta de {self.nome}:')
        print('Saques realizados:')
        for saque in self.saques_realizados:
            print(f'- Saque de R${saque:.2f}')
        print('Depósitos realizados:')
        for deposito in self.depositos_realizados:
            print(f'- Depósito de R${deposito:.2f}')
        print(f'Saldo atual: R${self.saldo:.2f}')
        self.show_thanks()

    def error_message(self, message):
        print(message)
        time.sleep(3)
        # Limpa apenas a linha da mensagem de erro
        print('\033[1A\033[K', end='\r')
        time.sleep(0.5)

    def show_thanks(self):
        print('O ITAÚ AGRADECE A PREFERÊNCIA!')


def main():
    print("BEM VINDO AO BANCO ITAÚ!")

    conta_bancaria = ContaBancaria()

    # Solicitação e validação do nome completo
    while True:
        nome = input('Digite seu nome completo: ')
        if nome != conta_bancaria.nome:
            conta_bancaria.error_message('Nome incorreto. Digite seu nome completo.')
        else:
            conta_bancaria.nome = nome
            break

    # Solicitação e validação do CPF
    while True:
        cpf = input('Digite seu CPF: ')
        if len(cpf) != 11 or not cpf.isdigit():
            conta_bancaria.error_message('Algo deu errado. Digite o CPF sem traços.')
        else:
            conta_bancaria.cpf = cpf
            break

    # Solicitação e validação da data de nascimento
    while True:
        data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
        if len(data_nascimento) != 10 or '/' not in data_nascimento:
            conta_bancaria.error_message('Algo deu errado. Digite a data de nascimento completa.')
        else:
            conta_bancaria.data_nascimento = data_nascimento
            break

    # Solicitação e validação da agência
    while True:
        agencia = input('Digite o número da agência: ')
        if len(agencia) != 4 or not agencia.isdigit():
            conta_bancaria.error_message('Algo deu errado. A agência possui 4 digitos.')
        else:
            conta_bancaria.agencia = agencia
            break

    # Solicitação e validação do número da conta
    while True:
        conta = input('Digite o número da conta: ')
        if len(conta) < 6 or not conta[:-1].isdigit() or not conta[-1].isdigit():
            conta_bancaria.error_message('Algo deu errado. A conta deverá constar 5 números e 1 digito.')
        else:
            conta_bancaria.conta = conta
            break

    while True:
        print('\nEscolha uma operação:')
        print('1 - Depositar')
        print('2 - Sacar')
        print('3 - Visualizar Extrato')
        print('4 - Sair')

        opcao = input('Digite o número da operação desejada: ')

        if opcao == '1':
            valor = float(input('Digite o valor a ser depositado: '))
            conta_bancaria.depositar(valor)
        elif opcao == '2':
            valor = float(input('Digite o valor a ser sacado: '))
            conta_bancaria.sacar(valor)
        elif opcao == '3':
            conta_bancaria.extrato()
        elif opcao == '4':
            print('Saindo...')
            print('O ITAÚ AGRADECE A PREFERÊNCIA!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


if __name__ == "__main__":
    main()



