
# Lista que armazena as demandas
demandas = []

# Controle do próximo ID
proximo_id = 1


# CREATE - Cadastrar demanda
def cadastrar_demanda():
    global proximo_id

    titulo = input("Digite o título: ")
    solicitante = input("Digite o solicitante: ")
    prioridade = input("Digite a prioridade: ")
    cep = input("Digite o CEP: ")
    cidade = input("Digite a cidade: ")

    demanda = {
        "id": proximo_id,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Pendente"
    }

    demandas.append(demanda)
    proximo_id += 1

    print("Demanda cadastrada com sucesso!")


# READ - Listar demandas
def listar_demandas():
    if len(demandas) == 0:
        print("Nenhuma demanda cadastrada.")
    else:
        for demanda in demandas:
            print("--------------------")
            print("ID:", demanda["id"])
            print("Título:", demanda["titulo"])
            print("Solicitante:", demanda["solicitante"])
            print("Prioridade:", demanda["prioridade"])
            print("CEP:", demanda["cep"])
            print("Cidade:", demanda["cidade"])
            print("Status:", demanda["status"])


# UPDATE - Atualizar demanda
def atualizar_demanda():
    try:
        id_busca = int(input("Digite o ID da demanda: "))

        for demanda in demandas:
            if demanda["id"] == id_busca:
                novo_status = input("Digite o novo status: ")
                demanda["status"] = novo_status

                print("Demanda atualizada!")
                return

        print("Demanda não encontrada.")

    except ValueError:
        print("Digite um ID numérico válido.")


# DELETE - Excluir demanda
def excluir_demanda():
    try:
        id_busca = int(input("Digite o ID da demanda: "))

        for demanda in demandas:
            if demanda["id"] == id_busca:
                demandas.remove(demanda)
                print("Demanda excluída!")
                return

        print("Demanda não encontrada.")

    except ValueError:
        print("Digite um ID numérico válido.")


# MENU PRINCIPAL
def menu():
    while True:
        print("\n===== TECHFLOW CORE =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Atualizar demanda")
        print("4 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            atualizar_demanda()

        elif opcao == "4":
            excluir_demanda()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


# EXECUÇÃO DO SISTEMA
menu()
