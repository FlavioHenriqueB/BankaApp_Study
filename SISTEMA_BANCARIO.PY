menu = """

========== BankApp ============ 

Escolha abaixo a opção desejada: 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[9] Sair

* Apenas numeros inteiros são aceitos. 

=> """

saldo = 0
limite = 500
negativo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
   
   opcao = input(menu)
   
   if opcao == "1":
      valor = float(input("""
Informe o valor a ser depositado:
                          
* Para fracionar o valor, use ".". Os demais caracteres especiais não são aceitos.
                          
=>"""))
      if valor > 0:
         saldo += valor
         extrato += f"Deposito: R$ {valor:.2f}\n"
         print("Valor depositado com sucesso!")
      
      else:
         print("Valor informado está incorreto. Tente novamente")

   elif opcao == "2":
      valor = float(input("""
Informe o valor a ser sacado:
                          
* Para fracionar o valor, use ".". Os demais caracteres especiais não são aceitos.
                          
=>"""))
      
      excedeu_limite = valor > limite
      sem_saldo = valor > saldo
      valor_incorreto = valor < negativo

      if valor_incorreto:
         print("Valor informado incorreto. Tente novamente.")
      elif sem_saldo:
         print("Saldo insuficiente.")
      elif excedeu_limite:
         print("Valor superior ao limite de saque diário. Tente novamente ou entre em contato com o seu gerente.")   
      elif valor <= saldo:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         print("Valor sacado com sucesso!")
      else:
         print("Algo falhou! Tente novamente mais tarde.")

   elif opcao == "3":
      print(f"======== EXTRATO: ========\n")
      print("Não foram relizadas movimentações." if not extrato else extrato)
      print("==========================")

   elif opcao == "4":
      print(f"======== SEU SALDO ========:\n")
      print(f"Saldo: R${saldo:.2f}\n")
      print("===========================")

   elif opcao == "9":
      print("Obrigado! Volte sempre.")
      break

   else:
      print("Opção invalida. Tente novamente.")