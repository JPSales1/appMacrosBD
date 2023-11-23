from classes import Alimento, AlimentoReduzido
from banco_de_dados import banco, comando
#from fastapi import HTTPException

def abrir_lista():
    comando.execute("SELECT * FROM tabela_alimentos")
    return comando.fetchall()

def procurar_lista(nome: str):
    comando.execute("SELECT * FROM tabela_alimentos WHERE nome='{}'".format(nome))
    return comando.fetchall()    

def escrever_alimento(entrada: Alimento):
    comando.execute("INSERT INTO tabela_alimentos VALUES('{}', '{}', '{}','{}')".format(entrada.nome, entrada.carboidratos, entrada.proteinas, entrada.gorduras))
    banco.commit()
    return 'Alimento inserido com sucesso'
   

def deletar_alimento(entrada: AlimentoReduzido):
    comando.execute("DELETE FROM tabela_alimentos WHERE nome='{}'".format(entrada.nome))
    banco.commit()
    return 'Alimento deletado com sucesso'
    
