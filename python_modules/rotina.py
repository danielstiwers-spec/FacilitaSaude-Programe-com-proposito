"""Versão em Python da lógica de rotina e acompanhamento de hábitos."""


class RotinaAgua:
    """Controla o consumo de água e a exibição do progresso."""

    def __init__(self, meta_agua_ml=2000):
        self.agua_consumida_ml = 0
        self.meta_agua_ml = meta_agua_ml

    def adicionar_agua(self):
        """Adiciona 250ml de água ao contador."""
        if self.agua_consumida_ml >= self.meta_agua_ml:
            return {
                "mensagem": "Parabéns! Você já atingiu 100% da sua meta de água de hoje! 💧",
                "atingiu_meta": True,
            }

        self.agua_consumida_ml += 250
        return self.atualizar_interface_agua()

    def resetar_agua(self):
        """Zera o contador de água."""
        self.agua_consumida_ml = 0
        return self.atualizar_interface_agua()

    def atualizar_interface_agua(self):
        """Calcula o percentual e retorna o estado atual para a interface."""
        porcentagem = min((self.agua_consumida_ml / self.meta_agua_ml) * 100, 100)
        litros_formatados = f"{(self.agua_consumida_ml / 1000):.2f}L"

        return {
            "porcentagem": round(porcentagem),
            "litros_formatados": litros_formatados,
            "agua_consumida_ml": self.agua_consumida_ml,
            "meta_agua_ml": self.meta_agua_ml,
        }

    def build_sleep_chart_config(self):
        """Retorna a configuração de um gráfico de histórico de sono."""
        return {
            "type": "line",
            "data": {
                "labels": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
                "datasets": [
                    {
                        "label": "Horas Dormidas",
                        "data": [7.5, 6.0, 8.2, 5.5, 7.0, 9.0, 8.5],
                        "borderColor": "#2b6cb0",
                        "backgroundColor": "rgba(43, 108, 176, 0.1)",
                        "borderWidth": 3,
                        "fill": True,
                        "tension": 0.3,
                    }
                ],
            },
            "options": {
                "responsive": True,
                "maintainAspectRatio": False,
                "scales": {
                    "y": {
                        "beginAtZero": True,
                        "max": 12,
                        "title": {"display": True, "text": "Horas"},
                    }
                },
                "plugins": {
                    "legend": {"display": False}
                },
            },
        }


def inicializar_rotina():
    """Inicializa a rotina retornando o estado inicial da interface."""
    rotina = RotinaAgua()
    return {
        "agua": rotina.atualizar_interface_agua(),
        "sleep_chart": rotina.build_sleep_chart_config(),
    }
