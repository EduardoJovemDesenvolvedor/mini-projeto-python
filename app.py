from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
import backend.lista_tarefas
from pydantic import BaseModel

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/", response_class=HTMLResponse)
def home():
    path = os.path.join("frontend", "index.html")
    with open(path, encoding="utf-8") as f:
        return f.read()
    
@app.get('/listar_tarefas')
def listar_tarefas_route():
    tarefas = backend.lista_tarefas.listar_tarefas()

    return {
        "tarefas": [
            {"id": i + 1, "nome": tarefa}
            for i, tarefa in enumerate(tarefas)
        ]
    }



class Tarefa(BaseModel):
    nome: str

@app.post("/tarefas")
def adicionar_tarefas(tarefa: Tarefa):
    return {
        "adicionado": backend.lista_tarefas.adicionar_tarefa(tarefa.nome)
    }

@app.put('/tarefas/{indice}')
def renomear_tarefa(indice: int, novo_nome: str):
    indice -= 1
    resultado = backend.lista_tarefas.renomear_tarefa(indice, novo_nome)

    if resultado:
        return {
            "mensagem": "Tarefa renomeada com sucesso",
            "tarefas": backend.lista_tarefas.listar_tarefas()
        }
    else:
        return {
            "erro": "Índice inválido"
        }
    
@app.delete('/tarefas/{indice}')
def deletar_tarefa(indice: int):
    indice -= 1

    resultado = backend.lista_tarefas.deletar_tarefa(indice)

    if resultado:
        return {
            "mensagem": "Tarefa deletada com sucesso",
            "tarefas": backend.lista_tarefas.listar_tarefas()
        }
    else:
        return {
            "erro": "Índice inválido"
        }
    






