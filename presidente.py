from funcionario import Funcionario

class Presidente (Funcionario):
    def __init__ (self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)