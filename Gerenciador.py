# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefas": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

# Lista principal que armazena as tarefas
tarefas = []

# Função para exibir todas as tarefas
def listar_tarefas(tarefas):
    print("\nLista de tarefas:")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["completada"] else ""
        nome_tarefa = tarefa["tarefas"]
        print(f"{indice}. [{status}] {nome_tarefa} ")

# Função para editar o nome de uma tarefa com base no índice informado
def editar_tarefa(tarefas, indice, novo_nome):
    indice_tarefa_ajustado = int(indice) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefas"] = novo_nome
        print(f"Tarefa {indice} editada com sucesso para '{novo_nome}'")
    else:
        print("Índice inválido. Tarefa não encontrada.")

# Função para marcar uma tarefa como concluída
def completar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"Tarefa {indice} marcada como completa.")
    else:
        print("Índice inválido. Tarefa não encontrada.")

# Função para remover todas as tarefas que foram marcadas como concluídas
def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("Tarefas completadas removidas com sucesso.")

# Loop principal do programa
while True:
    print("\nGerenciador de Tarefas 1.0")
    print("1 - Criar tarefa")   
    print("2 - Listar tarefas")
    print("3 - Editar tarefa")
    print("4 - Completar tarefa")
    print("5 - Remover tarefas completadas")
    print("6 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        listar_tarefas(tarefas)

    elif escolha == "3":
        listar_tarefas(tarefas)
        try:
            indice = int(input("Digite o número da tarefa que deseja editar: "))
            novo_nome = input("Digite o novo nome da tarefa: ")
            editar_tarefa(tarefas, indice, novo_nome)
        except ValueError:
            print("Por favor, insira um número válido.")

    elif escolha == "4":
        listar_tarefas(tarefas)
        try:
            indice = int(input("Digite o número da tarefa que deseja marcar como completada: "))
            completar_tarefa(tarefas, indice)
        except ValueError:
            print("Por favor, insira um número válido.")

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        listar_tarefas(tarefas)

    elif escolha == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
