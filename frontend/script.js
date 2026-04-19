const API = "https://mini-projeto-python.onrender.com";

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
    console.log("clicou adicionar");
    
    const input = document.getElementById("novaTarefa");
    const nome = input.value;

    if (!nome) return;

    await fetch(`${API}/tarefas`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome })
    });

    input.value = "";
    listarTarefas();
}

// DELETAR TAREFA
async function deletarTarefa(indice) {
    console.log("clicou excluir");
    const resposta = await fetch(`${API}/tarefas/${indice}`, {
        method: "DELETE"
    });

    const dados = await resposta.json();
    console.log("DELETE:", dados);

    await listarTarefas();
}

// CARREGAR AUTOMATICAMENTE
listarTarefas();