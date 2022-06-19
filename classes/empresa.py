from datetime import datetime as dt


import json
import os
from helper import Helpers
from classes.gerente import Gerente


class Empresa:
    def __init__(self, nome: str, cnpj: str, contratados: list = []):
        self.nome = Helpers.helper_title(nome)
        self.cnpj = cnpj
        self.contratados = contratados

    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self, funcionario: dict):
        self._snake_name = Helpers.helper_func(funcionario.nome_completo)

        for item in self.contratados:

            if item.cpf == funcionario.cpf:
                return f"Funcionário já cadastrado!"

        funcionario.email = f"{self._snake_name}@{self.nome}.com"
        funcionario.empresa = self.nome
        self.contratados.append(funcionario)

        return f"Funcionário adicionado!"

    def gerar_holerite(self, funcionario):

        funcionario_data = {**funcionario.__dict__, "mes": dt.now().strftime("%B")}
        print(funcionario_data)

        for item in self.contratados:
            if item.cpf == funcionario.cpf:

                try:
                    os.mkdir(f"./empresas/{self.nome}")
                except:
                    print(f"Diretório já existente!")
                with open(
                    f"./empresas/{self.nome}/{Helpers.helper_func(funcionario.nome_completo)}.json",
                    "w",
                ) as data_holerite:
                    json.dump(funcionario_data, data_holerite, indent=2)

            return False

    @staticmethod
    def ler_holerite(empresa, funcionario):

        try:
            with open(
                f"./empresas/{empresa.nome}/{Helpers.helper_func(funcionario.nome_completo)}.json",
                "r",
            ) as data_holerite:
                return json.load(data_holerite)
        except:
            return "Holerite não gerado!"

    def demissao(self, funcionario):

        for item in self.contratados:
            print(item.__dict__)
            if item.cpf == funcionario.cpf:
                self.contratados.remove(funcionario)
                for item in self.contratados:
                    if type(item) == Gerente:
                        for item2 in item.funcionarios:
                            if item2.cpf == funcionario.cpf:
                                item.funcionarios.remove(funcionario)
                return f"{funcionario.funcao} demitido!"

        return "Não consta esse CPF na empresa!"

    def promocao(self, funcionario):
        for item in self.contratados:
            if item.cpf == funcionario.cpf:
                new_gerente = Gerente(funcionario.nome_completo, funcionario.cpf)
                new_gerente._salario = funcionario._salario
                return new_gerente
        return False
