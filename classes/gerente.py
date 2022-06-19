from classes.funcionario import Funcionario
from helper import Helpers


class Gerente(Funcionario):
    funcao = "Gerente"

    def __init__(
        self, nome_completo: str, cpf: str, salario: int = 8000, funcionarios: list = []
    ):
        self.nome_completo = Helpers.helper_name_title(nome_completo)
        self.cpf = cpf
        self.salario = salario
        self.funcionarios = funcionarios

    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario):
        # for item in self.funcionarios:
        if funcionario.funcao == "Gerente":
            return False
        if funcionario.empresa != self.empresa:
            return False
        for item in self.funcionarios:
            if item.cpf == funcionario.cpf:
                return False

        self.funcionarios.append(funcionario)

        return True

    def aumento_salarial(self, funcionario, empresa):
        for item in self.funcionarios:
            if item.cpf == funcionario.cpf:
                funcionario.salario = int(funcionario.salario * 1.1)
                if funcionario.salario > 8000:
                    return empresa.promocao(funcionario)
                return funcionario
            return False
