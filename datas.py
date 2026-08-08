import calendar
from datetime import date


DIAS_SEMANA = {
    "Segunda": 0,
    "Terça": 1,
    "Quarta": 2,
    "Quinta": 3,
    "Sexta": 4,
    "Sábado": 5,
    "Domingo": 6
}


def obter_datas(dia_semana, mes, ano):

    calendario = calendar.Calendar()

    datas = []

    dia_desejado = DIAS_SEMANA[dia_semana]

    for data in calendario.itermonthdates(ano, mes):

        if data.month == mes and data.weekday() == dia_desejado:

            datas.append(
                data.strftime("%d/%m/%Y")
            )

    return datas