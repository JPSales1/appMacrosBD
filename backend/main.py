from metodos import abrir_lista, escrever_alimento, deletar_alimento, procurar_lista
from fastapi import FastAPI, HTTPException
from classes import Alimento
from classes import AlimentoReduzido
from home import home

app = FastAPI()


# Home da aplicação
@app.get("/",
         tags=["Home"])
async def pegar_home():
    return home()


# Consultar lista geral
@app.get("/alimentos/lista",
         tags=["Requisições"],
         name="Consultar lista completa",
         description="Consulta a lista contendo todas as informações de alimento")
async def consultar_lista():
    try:
        return abrir_lista()
    except Exception:
        raise HTTPException(status_code=500, detail="A lista não foi encontrada")


# Consultar alimento específico da lista
@app.get("/alimentos/{id_alimento}",
         tags=["Requisições"],
         name="Consultar alimento específico",
         description="Consulta a lista contendo todas as informações do alimento pesquisado")
async def buscar_alimento(nome: str):
    try:
       return procurar_lista(nome)
    except Exception:
        raise HTTPException(status_code=500, detail="Lista não encontrada")


# Inserção de um novo alimento na lista
@app.post("/novo_alimento",
          tags=["Inserções"],
          name="Incluir alimento",
          description="Inclui um novo alimento na lista.")
async def incluir_alimento(entrada: Alimento):
    try:
        return escrever_alimento(entrada)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao inserir alimento")


# Deletar alimento da lista
@app.delete("/alimentos",
            tags=["Deletar"],
            name='Deletar alimento',
            description="Deleta um alimento da lista")
async def excluir_alimento(entrada:AlimentoReduzido):
    try:
        return deletar_alimento(entrada)
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao deletar alimento")
    