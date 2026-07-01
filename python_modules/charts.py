"""Versão em Python das configurações de gráficos do projeto.

Este módulo traduz a lógica de inicialização do Chart.js para uma estrutura
Python baseada em dicionários, facilitando uso em scripts, APIs ou testes.
"""

from copy import deepcopy

COLORS = {
    "primary": "rgba(43, 108, 176, 1)",
    "secondary": "rgba(0, 135, 90, 1)",
    "warning": "rgba(255, 193, 7, 1)",
    "danger": "rgba(220, 53, 69, 1)",
    "info": "rgba(54, 162, 235, 1)",
    "success": "rgba(75, 192, 75, 1)",
}

COMMON_OPTIONS = {
    "responsive": True,
    "maintain_aspect_ratio": True,
    "plugins": {
        "legend": {
            "display": True,
            "position": "bottom",
            "labels": {
                "font": {"size": 12, "family": '"Rawline", sans-serif'},
                "padding": 15,
                "use_point_style": True,
            },
        }
    },
}


def build_chart_configs():
    """Retorna um dicionário com as configurações dos gráficos."""
    return {
        "mealChart": {
            "type": "doughnut",
            "data": {
                "labels": ["Proteínas", "Carboidratos", "Gorduras"],
                "datasets": [
                    {
                        "data": [40, 45, 15],
                        "backgroundColor": [
                            "rgba(220, 53, 69, 0.8)",
                            "rgba(255, 193, 7, 0.8)",
                            "rgba(255, 99, 132, 0.8)",
                        ],
                        "borderColor": [
                            "rgba(220, 53, 69, 1)",
                            "rgba(255, 193, 7, 1)",
                            "rgba(255, 99, 132, 1)",
                        ],
                        "borderWidth": 2,
                    }
                ],
            },
            "options": {
                **deepcopy(COMMON_OPTIONS),
                "plugins": {
                    **deepcopy(COMMON_OPTIONS["plugins"]),
                    "tooltip": {
                        "callbacks": {
                            "label": lambda context: f"{context['label']}: {context['parsed']}g"
                        }
                    },
                },
            },
        },
        "waterChart": {
            "type": "bar",
            "data": {
                "labels": ["08h", "10h", "12h", "14h", "16h", "18h"],
                "datasets": [
                    {
                        "label": "Copos de Água",
                        "data": [1, 2, 2, 1, 2, 1],
                        "backgroundColor": "rgba(54, 162, 235, 0.8)",
                        "borderColor": "rgba(54, 162, 235, 1)",
                        "borderWidth": 1,
                        "borderRadius": 4,
                    }
                ],
            },
            "options": {
                **deepcopy(COMMON_OPTIONS),
                "indexAxis": "x",
                "scales": {
                    "y": {
                        "beginAtZero": True,
                        "max": 3,
                        "ticks": {"stepSize": 1},
                    }
                },
            },
        },
        "activityChart": {
            "type": "pie",
            "data": {
                "labels": ["Caminhada", "Academia", "Corrida", "Futebol"],
                "datasets": [
                    {
                        "data": [30, 60, 20, 90],
                        "backgroundColor": [
                            "rgba(75, 192, 75, 0.8)",
                            "rgba(54, 162, 235, 0.8)",
                            "rgba(255, 99, 132, 0.8)",
                            "rgba(255, 159, 64, 0.8)",
                        ],
                        "borderColor": [
                            "rgba(75, 192, 75, 1)",
                            "rgba(54, 162, 235, 1)",
                            "rgba(255, 99, 132, 1)",
                            "rgba(255, 159, 64, 1)",
                        ],
                        "borderWidth": 2,
                    }
                ],
            },
            "options": {
                **deepcopy(COMMON_OPTIONS),
                "plugins": {
                    **deepcopy(COMMON_OPTIONS["plugins"]),
                    "tooltip": {
                        "callbacks": {
                            "label": lambda context: f"{context['label']}: {context['parsed']} min"
                        }
                    },
                },
            },
        },
        "heartChart": {
            "type": "line",
            "data": {
                "labels": ["08h", "10h", "12h", "14h", "16h", "18h"],
                "datasets": [
                    {
                        "label": "BPM (Batidas por Minuto)",
                        "data": [72, 75, 78, 120, 88, 74],
                        "borderColor": "rgba(220, 53, 69, 1)",
                        "backgroundColor": "rgba(220, 53, 69, 0.1)",
                        "borderWidth": 3,
                        "fill": True,
                        "tension": 0.4,
                        "pointRadius": 5,
                        "pointBackgroundColor": "rgba(220, 53, 69, 1)",
                        "pointBorderColor": "#fff",
                        "pointBorderWidth": 2,
                    }
                ],
            },
            "options": {
                **deepcopy(COMMON_OPTIONS),
                "scales": {
                    "y": {
                        "beginAtZero": False,
                        "min": 60,
                        "max": 140,
                    }
                },
                "plugins": {
                    **deepcopy(COMMON_OPTIONS["plugins"]),
                    "tooltip": {
                        "backgroundColor": "rgba(0, 0, 0, 0.8)",
                        "padding": 12,
                        "callbacks": {
                            "label": lambda context: f"BPM: {context['parsed']['y']}"
                        },
                    },
                },
            },
        },
        "sleepChart": {
            "type": "line",
            "data": {
                "labels": ["22h", "23h", "00h", "01h", "02h", "03h", "04h"],
                "datasets": [
                    {
                        "label": "Qualidade do Sono (%)",
                        "data": [70, 78, 75, 82, 88, 85, 90],
                        "borderColor": "rgba(54, 162, 235, 1)",
                        "backgroundColor": "rgba(54, 162, 235, 0.2)",
                        "borderWidth": 3,
                        "fill": True,
                        "tension": 0.3,
                        "pointRadius": 5,
                        "pointBackgroundColor": "rgba(54, 162, 235, 1)",
                        "pointBorderColor": "#fff",
                        "pointBorderWidth": 2,
                    }
                ],
            },
            "options": {
                **deepcopy(COMMON_OPTIONS),
                "scales": {
                    "y": {
                        "beginAtZero": True,
                        "min": 0,
                        "max": 100,
                    }
                },
                "plugins": {
                    **deepcopy(COMMON_OPTIONS["plugins"]),
                    "tooltip": {
                        "backgroundColor": "rgba(0, 0, 0, 0.8)",
                        "padding": 12,
                        "callbacks": {
                            "label": lambda context: f"Qualidade: {context['parsed']['y']}%"
                        },
                    },
                },
            },
        },
    }


def register_service_worker():
    """Simula o registro de service worker para ambiente Python."""
    return {"registered": False, "reason": "service_worker_not_available_in_python"}
