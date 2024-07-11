# Gerenciamento de Tarefas

# Estrutura para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionarTarefa(nome):
    tarefa = {"nome": nome, "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para remover uma tarefa
def removerTarefa(nome):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa["nome"] != nome]
    print(f"Tarefa '{nome}' removida com sucesso!")

# Função para marcar uma tarefa como concluída
def concluirTarefa(nome):
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["concluida"] = True
            print(f"Tarefa '{nome}' marcada como concluída!")
            return
    print(f"Tarefa '{nome}' não encontrada!")

# Função para listar todas as tarefas
def listarTarefa():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas:
            status = "Concluída" if tarefa["concluida"] else "Não Concluída"
            print(f"- {tarefa['nome']} ({status})")

# Função para listar tarefas por status
def listarTarefaPorStatus(concluida=True):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["concluida"] == concluida]
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Não Concluída"
            print(f"- {tarefa['nome']} ({status})")

# Função para exibir o menu interativo
def menu():
    while True:
        print("\nGerenciamento de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Concluir tarefa")
        print("4. Listar todas as tarefas")
        print("5. Listar tarefas concluídas")
        print("6. Listar tarefas não concluídas")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite o nome da tarefa: ")
            adicionarTarefa(nome)
        elif escolha == "2":
            nome = input("Digite o nome da tarefa a ser removida: ")
            removerTarefa(nome)
        elif escolha == "3":
            nome = input("Digite o nome da tarefa a ser concluída: ")
            concluirTarefa(nome)
        elif escolha == "4":
            listarTarefa()
        elif escolha == "5":
            listarTarefaPorStatus(concluida=True)
        elif escolha == "6":
            listarTarefaPorStatus(concluida=False)
        elif escolha == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, por favor escolha novamente.")

# Executar o menu
menu()
