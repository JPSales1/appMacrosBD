from pydantic import BaseModel

class Alimento(BaseModel):
    nome: str
    proteinas: int
    carboidratos:  int
    gorduras: int

class AlimentoReduzido(BaseModel):
    nome: str


