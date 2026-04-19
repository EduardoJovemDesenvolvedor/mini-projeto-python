const API = "https://mini-projeto-python.onrender.com/";

// LISTAR TAREFAS
async function listarTarefas() {
    const resposta = await fetch(`${API}/listar_tarefas`);
    const dados = await resposta.json();

    const lista = document.getElementById("listaTarefas");
    lista.innerHTML = "";

    dados.tarefas.forEach(tarefa => {
        const li = document.createElement("li");

        li.innerHTML = `
            ${tarefa.id} - ${tarefa.nome}
            <button onclick="deletarTarefa(${tarefa.id})">Excluir</button>
        `;

        lista.appendChild(li);
    });
}

// ADICIONAR TAREFA
async function adicionarTarefa() {
    const input = document.getElementById("novaTarefa");
    const nome = input.value;

    if (!nome) return;

    await fetch(`${API}/tarefas?nome=${nome}`, {
        method: "POST"
    });

    input.value = "";
    listarTarefas();
}

// DELETAR TAREFA
async function deletarTarefa(indice) {
    await fetch(`${API}/tarefas/${indice}`, {
        method: "DELETE"
    });

    listarTarefas();
}

// CARREGAR AUTOMATICAMENTE
listarTarefas();