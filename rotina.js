// Variáveis de controle para o registro de água
let aguaConsumidaMl = 0;
const META_AGUA_ML = 2000; // 2 Litros

/**
 * Adiciona 250ml de água ao contador e atualiza a barra de progresso visual
 */
function adicionarAgua() {
    if (aguaConsumidaMl >= META_AGUA_ML) {
        alert("Parabéns! Você já atingiu 100% da sua meta de água de hoje! 💧");
        return;
    }

    aguaConsumidaMl += 250;
    atualizarInterfaceAgua();
}

/**
 * Reseta o contador de água para zero
 */
function resetarAgua() {
    aguaConsumidaMl = 0;
    atualizarInterfaceAgua();
}

/**
 * Atualiza todos os textos e elementos visuais da barra de água na tela
 */
function actualizarInterfaceAgua() {
    // Cálculos matemáticos
    const porcentagem = Math.min((aguaConsumidaMl / META_AGUA_ML) * 100, 100);
    const litrosFormatados = (aguaConsumidaMl / 1000).toFixed(2) + "L";

    // Atualização dos elementos do HTML
    document.getElementById('barraAgua').style.width = `${porcentagem}%`;
    document.getElementById('qtdAtual').textContent = litrosFormatados;
    document.getElementById('porcentagemTexto').textContent = `${Math.round(porcentagem)}%`;
}

/**
 * Inicialização dos Gráficos assim que a página estiver carregada
 */
document.addEventListener('DOMContentLoaded', function() {
    
    // Configuração do gráfico de Histórico de Sono
    const ctxSono = document.getElementById('sonoRotinaChart').getContext('2d');
    
    new Chart(ctxSono, {
        type: 'line',
        data: {
            labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
            datasets: [{
                label: 'Horas Dormidas',
                data: [7.5, 6.0, 8.2, 5.5, 7.0, 9.0, 8.5], // Horas de exemplo de cada noite
                borderColor: '#2b6cb0', // Azul idêntico ao theme-color do seu projeto
                backgroundColor: 'rgba(43, 108, 176, 0.1)', // Azul bem transparente para o preenchimento de fundo
                borderWidth: 3,
                fill: true,
                tension: 0.3 // Deixa a linha curvada de forma suave e elegante
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 12, // Limite máximo do gráfico de horas
                    title: {
                        display: true,
                        text: 'Horas'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false // Esconde a legenda para deixar o visual mais limpo como o gov.br
                }
            }
        }
    });

    // Inicia a interface da água zerada no primeiro carregamento
    atualizarInterfaceAgua();
});
