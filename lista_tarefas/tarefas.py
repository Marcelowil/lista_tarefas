import json
import uuid
import os
from datetime import datetime

nome_arquivo = 'tarefas.json'

def adicionar_tarefa():
    titulo = input("Título: ")
    descricao = input("Descrição: ")

    dados = {
        "id":str(uuid.uuid4()),
        "titulo":titulo,
        "descricao": descricao,
        "data_criacao": datetime.now().strftime('%d/%m/%Y'),
        "status": "Em andamento"
    }

    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            dados_existentes = json.load(arquivo)
            if not isinstance(dados_existentes, list):
                dados_existentes = []

    dados_existentes.append(dados)

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados_existentes, arquivo, indent=4)
    
    print(f"Tarefa criada !!")

def listar_tarefas(opcao):
    dados = carregar_tarefas()
    
    for dado in dados:
        if opcao == 1:
            imprimir_tarefas(dado)
        elif opcao == 2:
            if dado['status'] == "Concluida":
                imprimir_tarefas(dado)
        elif opcao == 3: 
            if dado['status'] == "Em andamento":
                imprimir_tarefas(dado)
        elif opcao == 4:
            if dado['status'] == "Cancelada":
                imprimir_tarefas(dado)

def excluir_tarefa():
    dados = carregar_tarefas()
    
    for dado in dados:
        print(f"ID: {dado['id']} - Título: {dado['titulo']}")
    
    id_tarefa = input("Digite o ID da tarefa para excluir: ")

    dados_atualizados = [dado for dado in dados if dado.get('id') != id_tarefa]

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados_atualizados, arquivo, indent=4)

    print("Tarefa excluída !")

def editar_tarefa(status):
    dados = carregar_tarefas()

    for dado in dados:
        if dado['status'] == "Em andamento":
            print(f"ID: {dado['id']} - Título: {dado['titulo']}")
    
    id_tarefa = input("Digite o ID da tarefa que deseja alterar o status: ")

    for dado in dados:
        if dado['id'] == id_tarefa:
            dado['status'] = status

    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

    print(f"Tarefa {status}!")


def imprimir_tarefas(dado):
    print(f"Tarefa ID: {dado['id']} - Título: {dado['titulo']}\nDescrição: {dado['descricao']}\nStatus: {dado['status']} - Data de criação {dado['data_criacao']}\n")


def carregar_tarefas():
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)

    return dados
