from datetime import datetime

class DatasBR:
    def __init__(self,):
        self.momento_cadastro = datetime.today()
    
    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = {
            1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho",
            7:"Julho",8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

        mes_cadastro = self.momento_cadastro.month 

        return meses_do_ano[mes_cadastro]
        
    def dia_da_semana(self):
        dias_da_semana = [
            "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        
        dia_semana = self.momento_cadastro.weekday()

        return dias_da_semana[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y às %H:%M")

        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro

        return tempo_cadastro

        