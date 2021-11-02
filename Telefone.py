import re

class TelefoneBR:
    
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Numero Incorreto!")    
    
    def __str__(self):
        return self.formata()

    def padrao_numero(self):
        return "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

    def valida_telefone(self, telefone):
        padrao = self.padrao_numero()
        resposta = re.findall(padrao, telefone)

        if resposta:
            return True
        else:
            return False

    def formata(self):
        padrao =self.padrao_numero()
        res = re.search(padrao, self.telefone)
        numero_formatado = (f"+{res.group(1)} ({res.group(2)}) {res.group(3)}-{res.group(4)}")
        return numero_formatado


