class Usuario:
    def __init__(self, nome, cpf, salario, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.email = email
        self.senha = senha


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def Cadastro(self):
        print("--- CADASTRO ---")
        nome = input("Digite o seu nome: ")
        cpf = input("Digite o seu CPF: ")
        salario = input("Digite o seu salário: ")
        email = input("Cadastre um email: ")
        senha = input("Cadastre uma senha: ")

        print("-------------------------------")
        print("----Informações Cadastradas----")
        print("Nome: ", nome)
        print("Cpf: ", cpf)
        print("Salário: ", salario)
        print("Email: ", email)
        print("Senha: ******")
        print("-------------------------------")

    def Autentica(self):
        print("-------LOGIN-------")
        email = input("Digite o email: ")
        senha = input("Digite uma senha: ")
        
        if ((email == self.email) and (senha == self.senha)):
            print("Funcionário autenticado no sistema!")
        else:
            print("Funcionário não logado!")

        print("-----------------")

