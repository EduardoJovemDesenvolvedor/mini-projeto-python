"""
Objetivo - Criar um back-end onde podemos adicionar item, apagar item e renomear item. 
após criar a lógica, fazer uma conexão com o front-end.

OBS: mini projeto sugerido pelo chat.
"""

tarefas = []

def adicionar_tarefa(nome):
    tarefas.append(nome)
    return {"mensagem": "Tarefa adicionada", "tarefas": tarefas}


def listar_tarefas():
    return {"tarefas": tarefas}


def renomear_tarefa(indice, novo_nome):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = novo_nome
        return True
    return False


def deletar_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        return True
    return False