# Sistema simples de hotel com menu

clientes = {}

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    idade = input("Idade: ")
    documento = input("CPF ou RG: ")

    clientes[documento] = {
        "nome": nome,
        "idade": idade
    }

    print("Cliente cadastrado com sucesso!")

def selecionar_hospede():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    print("\n--- Lista de Clientes ---")
    for doc, dados in clientes.items():
        print(f"{doc} - {dados['nome']}")

    documento = input("\nDigite o CPF/RG do hóspede: ")

    if documento in clientes:
        quarto = input("Número do quarto: ")
        dias = input("Quantidade de diárias: ")

        print("\n--- Check-in realizado ---")
        print(f"Hóspede: {clientes[documento]['nome']}")
        print(f"Quarto: {quarto}")
        print(f"Diárias: {dias}")
    else:
        print("Cliente não encontrado.")

def deletar_cliente():
    documento = input("\nDigite o CPF/RG do cliente a deletar: ")

    if documento in clientes:
        del clientes[documento]
        print("Cliente removido com sucesso.")
    else:
        print("Cliente não encontrado.")

def listar_hospedes():
    if not clientes:
        print("\nNenhum hóspede cadastrado.")
        return

    print("\n--- Lista de Hóspedes ---")
    for doc, dados in clientes.items():
        print(f"Nome: {dados['nome']} | Idade: {dados['idade']} | Documento: {doc}")

# Loop principal
while True:
    print("\n=== MENU DO HOTEL ===")
    print("1 - Cadastrar cliente")
    print("2 - Selecionar hóspede (check-in)")
    print("3 - Deletar cliente")
    print("4 - Listar hóspedes")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        selecionar_hospede()
    elif opcao == "3":
        deletar_cliente()
    elif opcao == "4":
        listar_hospedes()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")