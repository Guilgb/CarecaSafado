from datetime import datetime


class DateBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        self.mes_cadastro = self.momento_cadastro.month
        return print(meses_do_ano[self.mes_cadastro-1])

    def dia_da_semana(self):
        dia_semana_lista = [
            "Segunda", "Terça"
            "Quarta", "Quinta", "Sexta"
        ]
        dia_da_semana = self.momento_cadastro.weekday()
        return print(dia_semana_lista[dia_da_semana - 1])

    def data_cadastrada(self):
        data_format = self.momento_cadastro.strftime("%d/%m/%Y  %H:%M:%S")
        return data_format

    def __str__(self) -> str:
        return self.data_cadastrada()
