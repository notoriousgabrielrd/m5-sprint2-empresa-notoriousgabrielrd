from classes.empresa import Empresa
from classes.funcionario import Funcionario
from classes.gerente import Gerente

if __name__ == "__main__":
    pass

    empresa_1 = Empresa("  kenzie   brasil ", 12345678910124)
    funcionario_1 = Funcionario(" jordan  cardoso poole ", 32112343215)
    gerente_1 = Gerente(" bill    gates ", "32132186712")
    gerente_3 = Gerente("elon musk", "12342186574")
    # Adicionando funcionários
    empresa_1.contratar_funcionario(funcionario_1)
    empresa_1.contratar_funcionario(gerente_1)
    empresa_1.contratar_funcionario(gerente_3)
    # Adicionando funcionário ao gerente
    gerente_1.adicionar_funcionario(funcionario_1)
    # Funcionário não contratado
    funcionario_4 = Funcionario("klay mota thompson ", 92478965434)

    empresa_1.gerar_holerite(funcionario_1)
    holerite = Empresa.ler_holerite(empresa_1, funcionario_1)
    print(holerite)

    print(len(empresa_1.contratados))
    # 3
    resposta = empresa_1.demissao(funcionario_4)
    print(resposta)
    # Não consta esse CPF na empresa
    resposta = empresa_1.demissao(gerente_3)
    print(resposta)
    # Gerente demitido!
    print(len(gerente_1.funcionarios))
    # 1
    resposta = empresa_1.demissao(funcionario_1)
    print(resposta)
    # Funcionário demitido!
    print(len(gerente_1.funcionarios))
    # 0
    print(len(empresa_1.contratados))
    # 1
