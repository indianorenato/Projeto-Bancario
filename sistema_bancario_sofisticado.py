class ContaBancaria:
    def __init__(self, agencia, numero_conta, saldo=3500):
        """
        Inicializa uma conta bancária com uma agência, número de conta e saldo inicial.
        """
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.saques_realizados = []
        self.depositos_realizados = []

    def depositar(self, valor):
        """
        Realiza um depósito na conta bancária.
        """
        self.saldo += valor
        self.depositos_realizados.append(valor)

    def sacar(self, valor):
        """
        Realiza um saque na conta bancária.
        """
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques_realizados.append(valor)

    def extrato(self):
        """
        Retorna o extrato da conta bancária.
        """
        return {
            'saldo': self.saldo,
            'saques_realizados': self.saques_realizados,
            'depositos_realizados': self.depositos_realizados
        }


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        """
        Inicializa um usuário com nome, data de nascimento, CPF e endereço.
        """
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


usuarios = []
contas = []
prox_numero_conta = 1


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    """
    Cadastra um novo usuário.
    """
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado.")
            return
    usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
    print("Usuário cadastrado com sucesso.")


def cadastrar_conta(usuario):
    """
    Cadastra uma nova conta bancária para um usuário.
    """
    global prox_numero_conta
    conta = ContaBancaria(agencia="0001", numero_conta=f"{prox_numero_conta:04}")
    prox_numero_conta += 1
    contas.append({'usuario': usuario, 'conta': conta})
    print("Conta cadastrada com sucesso.")


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque em uma conta bancária.
    """
    if len(extrato['saques_realizados']) >= limite_saques:
        print('Você já atingiu o limite diário de saques.')
        return saldo, extrato
    if valor > limite:
        print('O valor máximo por saque é excedido.')
        return saldo, extrato
    if saldo < valor:
        print('Saldo insuficiente para realizar o saque.')
        return saldo, extrato

    saldo -= valor
    extrato['saques_realizados'].append(valor)
    print(f'Saque de R${valor:.2f} realizado com sucesso.')
    return saldo, extrato


def deposito(saldo, valor, extrato):
    """
    Realiza um depósito em uma conta bancária.
    """
    saldo += valor
    extrato['depositos_realizados'].append(valor)
    print(f'Depósito de R${valor:.2f} realizado com sucesso.')
    return saldo, extrato


def extrato(saldo, *, extrato):
    """
    Exibe o extrato de uma conta bancária.
    """
    print('\n=== Extrato ===')
    print(f'Saldo atual: R${saldo:.2f}\n')
    print('Saques realizados:')
    for saque in extrato['saques_realizados']:
        print(f'- Saque de R${saque:.2f}')
    print('\nDepósitos realizados:')
    for deposito in extrato['depositos_realizados']:
        print(f'- Depósito de R${deposito:.2f}')
    print('\n===============')


def listar_contas(usuario):
    """
    Lista as contas de um usuário.
    """
    print('\n--- Contas do Usuário ---')
    for item in contas:
        if item['usuario'] == usuario:
            print(f"Agência: {item['conta'].agencia} - Número da Conta: {item['conta'].numero_conta}")


def main():
    """
    Função principal do programa.
    """
    print("SEJA BEM-VINDO!")
    print('========================= MENU =========================')
    while True:
        print("\nEscolha uma operação:")
        print("1 - Cadastrar Usuário")
        print("2 - Cadastrar Conta Bancária")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Visualizar Extrato")
        print("6 - Listar Contas de um Usuário")
        print("7 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            nome = input("Digite seu nome completo: ")
            data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite seu CPF: ")
            endereco = input("Digite seu endereço: ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                cadastrar_conta(usuario)
            else:
                print("Usuário não encontrado.")
        elif opcao == "3":
            cpf = input("Digite o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                valor = float(input("Digite o valor a ser depositado: "))
                conta = next((c['conta'] for c in contas if c['usuario'] == usuario), None)
                if conta:
                    conta['conta'].saldo, _ = deposito(conta['conta'].saldo, valor, conta['conta'].extrato())
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")
        elif opcao == "4":
            cpf = input("Digite o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                valor = float(input("Digite o valor a ser sacado: "))
                conta = next((c['conta'] for c in contas if c['usuario'] == usuario), None)
                if conta:
                    conta['conta'].saldo, _ = saque(saldo=conta['conta'].saldo, valor=valor,
                                                     extrato=conta['conta'].extrato(), limite=500, numero_saques=3,
                                                     limite_saques=3)
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                conta = next((c['conta'] for c in contas if c['usuario'] == usuario), None)
                if conta:
                    extrato(conta['conta'].saldo, extrato=conta['conta'].extrato())
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")
        elif opcao == "6":
            cpf = input("Digite o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                listar_contas(usuario)
            else:
                print("Usuário não encontrado.")
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
