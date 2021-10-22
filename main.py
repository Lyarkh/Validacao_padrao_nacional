#Testes das classes do arquivo
from Documentos import Documento

cpf = Documento.cria_documento("05456925125")
print(cpf)

cnpj =Documento.cria_documento("35379838000112")
print(cnpj) 
