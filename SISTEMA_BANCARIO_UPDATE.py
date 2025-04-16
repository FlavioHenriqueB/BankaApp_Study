def mostrar_menu():
   
    menu = """

    ========== BankApp ============ 

    Escolha abaixo a opção desejada: 

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Saldo
    [5] Criar usuário
    [6] Criar conta
    [9] Sair

    * Apenas numeros inteiros são aceitos. 

    => """
    return input(menu)

def depositar(saldo, extrato, /):
    try:
      valor =  float(input("""
Informe o valor a ser depositado:
                           
* Para fracionar valores, use ".". Os demais caracteres especiais não serão aceitos.
                           
==> """))
      if valor > 0:
         saldo += valor
         extrato += f"Deposito: R$ {valor:.2f}\n"
         print("Valor depositado com sucesso!")
      
      else:
         print("Valor informado está incorreto. Tente novamente")
    except ValueError: 
      print("Entrada inválida. Digite apenas caracteres aceitos.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES, negativo):
    try:
        valor = float(input("""
Informe o valor a ser sacado:
                          
* Para fracionar o valores, use ".". Os demais caracteres especiais não serão aceitos.
                          
=>"""))
      
        excedeu_limite = valor > limite
        sem_saldo = valor > saldo
        valor_incorreto = valor < negativo
        ultrapassou_limite_saques = numero_saques >= LIMITE_SAQUES

        if ultrapassou_limite_saques:
            print("O limite de saques foi ultrapassado.")
        elif valor_incorreto:
            print("Valor informado incorreto. Tente novamente.")
        elif sem_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Valor superior ao limite de saque diário. Tente novamente ou entre em contato com o seu gerente.")   
        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Valor sacado com sucesso!")
        else:
            print("Algo falhou! Tente novamente mais tarde.")
        
    except ValueError:
      print("Entrada inválida. Digite apenas caracteres aceitos.")
    return saldo, extrato, numero_saques

def exibir_extrato(*, extrato):
    print(f"======== EXTRATO: ========\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("==========================")

def exibir_saldo(saldo, /):
    print(f"======== SEU SALDO ========:\n")
    print(f"Saldo: R${saldo:.2f}\n")
    print("===========================")

def criar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    try:
        for novo_usuario in usuarios:
            if novo_usuario["cpf"] == cpf:
                print("Erro: CPF já está cadastrado no sistema. Por favor, tente outro CPF")
                return None    
        novo_usuario = {
        "nome": nome,
        "data de nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereco,
        }
    except ValueError:
       print("Algo deu errado. Tente novamente.") 
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return novo_usuario

def criar_contacorrente(contas, usuarios):
    cpf = input("Informe o CPF do usuário (Somente números): ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if not usuario:
        print("Erro: Nenhum usuário encontrato. Tente outro CPF. Caso não tenha criado um usuário anteriormente, acesse o 5 no Menu Principal.") 
        return
    
    numero_conta = len(contas) + 1

    conta = {
        "Agência": "0001",
        "Numero da conta": numero_conta,
        "usuário": usuario
    }
          
    contas.append(conta)
    print(f"Conta criada com sucesso! Numero da conta: {numero_conta}")

def main():
    saldo = 0
    limite = 500
    negativo = 0
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, negativo=negativo)
        elif opcao == "3":
            exibir_extrato(extrato=extrato)
        elif opcao == "4":
            exibir_saldo(saldo)
        elif opcao == "5":
            print("=== Cadastro de novo usuário ===")
            nome = input("Digite o seu nome: ")
            data_nascimento = input("Digite sua data de nascimento (ex: 01/01/2001): ")
            cpf = input("Digite o seu CPF (apenas os números): ")
            endereco = input("Digite o seu endereço completo: ")
            criar_usuario(nome, data_nascimento, cpf, endereco, usuarios)
        elif opcao == "6":
            criar_contacorrente(contas, usuarios)
        elif opcao == "9":
            print("Obrigado. Volte sempre! :)")
            break
        else:
            print("Opção inválida. Tente novamente!")

# Executa o programa
main()