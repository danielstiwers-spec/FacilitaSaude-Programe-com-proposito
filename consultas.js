/**
 * Função para tratar o cancelamento de uma consulta
 * @param {HTMLElement} botaoClicado - O botão "X" que disparou o evento
 * @param {string} nomeMedico - Nome do médico para exibir no alerta
 */
function cancelarConsulta(botaoClicado, nomeMedico) {
    // Exibe a janela de confirmação nativa do navegador
    const confirmacao = confirm(`Tem certeza que deseja cancelar sua consulta com o(a) ${nomeMedico}?`);
    
    if (confirmacao) {
        // Encontra o elemento <li> mais próximo que envelopa o botão clicado
        const itemLista = botaoClicado.closest('li');
        
        // Aplica um efeito visual suave de sumiço (fade-out)
        itemLista.style.opacity = '0';
        itemLista.style.transform = 'scale(0.95)';
        itemLista.style.transition = 'all 0.3s ease';
        
        // Remove definitivamente do HTML após a animação terminar
        setTimeout(() => {
            itemLista.remove();
            checarConsultasVazias();
        }, 300);
    }
}

/**
 * Função para reagendar uma consulta
 * @param {string} nomeMedico - Nome do médico para exibir no alerta
 */
function reagendarConsulta(nomeMedico) {
    // Redireciona para a página de serviços
    window.location.href = 'services.html';
}

/**
 * Função auxiliar que verifica se a lista ficou vazia e exibe um aviso amigável
 */
function checarConsultasVazias() {
    const lista = document.querySelector('.consultas ul');
    const itensRestantes = lista.querySelectorAll('li');

    if (itensRestantes.length === 0) {
        lista.innerHTML = `
            <div style="text-align: center; padding: 30px; color: #718096; font-size: 14px; border: 1px dashed #cbd5e1; border-radius: 8px;">
                📅 Nenhuma consulta agendada para os próximos dias.
            </div>
        `;
    }
}