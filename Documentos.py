from validate_docbr import CPF, CNPJ
from abc import ABCMeta, abstractmethod

class Documento(metaclass = ABCMeta):

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de números inválida!!")

    def __str__(self):
        return self.formata()

    @abstractmethod
    def eh_valido(self, documento):
        pass
    @abstractmethod
    def formata(self):
        pass

class Cnpj(Documento):
    def __init__(self, documento):
        if self.eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")  

    def eh_valido(self, documento):
        if len(documento)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(documento)
    

    def  formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)   
        
class Cpf(Documento):

    def __init__(self, documento):
        if self.eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def eh_valido(self, cpf):
        if len(cpf) == 11:
            validando = CPF()
            return validando.validate(cpf)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)        