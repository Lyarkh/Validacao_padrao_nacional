from validate_docbr import CPF, CNPJ
from abc import ABCMeta, abstractmethod

class Documento(metaclass = ABCMeta):

    def __str__(self):
        return self.formata()

    @abstractmethod
    def formata(self):
        pass

class Cnpj(Documento):
    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")  

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)

        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def  formata(self):
        return self.cnpj
        
class Cpf(Documento):

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validando = CPF()
            return validando.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválido!!")

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)        