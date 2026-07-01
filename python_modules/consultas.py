"""Versão em Python da lógica de consultas do projeto."""


def get_consultas_exemplo():
    """Retorna a lista de consultas exibida na página inicial."""
    return [
        {
            "id": 1,
            "mes": "JUN",
            "dia": "24",
            "nome_medico": "Dr. John Doe",
            "especialidade": "Clínico Geral",
            "horario": "09:30h - Unidade Central",
            "status": "Confirmado",
        },
        {
            "id": 2,
            "mes": "JUL",
            "dia": "02",
            "nome_medico": "Dra. Jane Smith",
            "especialidade": "Pediatra",
            "horario": "14:15h - Bloco B",
            "status": "Confirmado",
        },
        {
            "id": 3,
            "mes": "JUL",
            "dia": "15",
            "nome_medico": "Dr. Bob Johnson",
            "especialidade": "Cardiologista",
            "horario": "10:00h - Instituto do Coração",
            "status": "Confirmado",
        },
    ]


def cancelar_consulta(consultas, consulta_id):
    """Remove uma consulta da lista e retorna a consulta removida."""
    for index, consulta in enumerate(consultas):
        if consulta.get("id") == consulta_id:
            return consultas.pop(index), consulta
    return consultas, None


def reagendar_consulta(nome_medico):
    """Retorna a ação de reagendamento em formato Python."""
    return {"redirect": "services.html", "nome_medico": nome_medico}


def checar_consultas_vazias(consultas):
    """Retorna uma mensagem amigável quando não houver consultas."""
    if not consultas:
        return {
            "mensagem": "📅 Nenhuma consulta agendada para os próximos dias.",
            "tipo": "vazio",
        }
    return {"mensagem": None, "tipo": "com_dados"}
