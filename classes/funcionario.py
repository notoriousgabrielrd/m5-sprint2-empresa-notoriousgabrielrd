from datetime import datetime as dt
import os

from helper import Helpers


class Funcionario:
    funcao = "Funcionário"

    def __init__(self, nome_completo: str, cpf: str, salario: int = 3000):
        self.nome_completo = Helpers.helper_name_title(nome_completo)
        self.cpf = cpf
        self.salario = salario
        self.admissao = dt.now().strftime("%d-%m-%Y")

    def __str__(self) -> str:

        return f"{self.nome_completo} - {self.funcao}"
