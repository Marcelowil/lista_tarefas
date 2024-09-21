import tarefas

show_menu = """
1 - Adicionar Tarefa
2 - Listar Tarefas
3 - Excluir Tarefa
4 - Concluir Tarefa
5 - Cancelar Tarefa
0 - Sair

"""

show_opcao = """
1 - Todas
2 - Concluídas
3 - Em andamento
4 - Canceladas

"""

while True:
    try:
        opcao = int(input(show_menu))
        if opcao == 1:
            tarefas.adicionar_tarefa()
        elif opcao == 2:
            opcao = int(input(show_opcao))
            tarefas.listar_tarefas(opcao)
        elif opcao == 3:
            tarefas.excluir_tarefa()
        elif opcao == 4:
            tarefas.editar_tarefa("Concluida")
        elif opcao == 5:
            tarefas.editar_tarefa("Cancelada")
        elif opcao == 0:
            break
    except:
        print("Opção inválida")
