from usuario import Usuario
class Conta(Usuario): 
    def __init__(self, nome, cpf, salario, email, senha, agencia, conta, dinheiro, valor): 
        super().__init__(nome, cpf, salario, email, senha)
        self._agencia = agencia 
        self._conta = conta
        self._dinheiro = dinheiro
        self._valor = valor
        
    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self._agencia =  agencia
        
    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self, conta):
        self._conta = conta
        
    @property
    def dinheiro(self):
        return self._dinheiro
    
    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self._dinheiro = dinheiro
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor (self, valor):
        self._valor = valor
    
    def Dados_Conta(self):
        print("--- DADOS DA CONTA ---")
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Salário: ", self.salario)
        print("E-mail: ", self.email)
        print("Senha: ******")
        print("Agência: ", self.agencia)
        print("Conta: ", self.conta)
        print("Valor em Dinheiro: R$", self.dinheiro)
        print("Valor cheque especial: R$", self.valor)
        print("-----------------------")
    
    def Extrato_Conta(self):
        print("---- DEMONSTRATIVO DE OPERAÇÃO ----")
        print("                         09/08/2023")
        print("CITIBANK                   14:59:13")
        print("Extrato N. 93120001-9628           ")
        print("                                   ")
        print("EXTRATO CONTA CORRENTE -           ")
        print("NOME: 0000{}".format(self.nome))
        print("CONTA: {} AGENCIA: {}".format(self.conta, self.agencia))
        print("DATA HISTORICO                VALOR")
        print("-----------------------------------")
        print("08/20 0131SAQUE BCO24H 7.000.000.000.01")
        print("      0131SAQUE CITICA 2.000.000.000.02")
        print("08/20 0161 PAGO CAIX 8.000.000.000.15")
        print("08/20 0162CH COMPENSAD 7.000.000.000.06")
        print("08/20 0162CH COMPENSAD 4.000.000.000.23")
        print("08/20 0616CH ELETRONIC 9.000.000.000.02")
        print("08/20 0774MAESTRO LOCA 4.000.000.000.00")
        print("                                   ")
        print("     SALDO ATUAL                 {}".format(self.dinheiro))
        print("     DISPONIVEL                  {}".format(self.dinheiro))
        print("                                   ")
        print("     SALDO SUJEITO A CONFIRMACAO   ")
        print("----------------------------------------")
        
    def Saque_Conta(self):
        print("---SAQUE---")
        print("[1]. R$20.00")
        print("[2]. R$50.00")
        print("[3]. R$100.00")
        print("[4]. R$200.00")
        print("[5]. Outro valor")
        
        opcao = int(input("Digite uma opção: "))
        
        if (opcao == 1):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 20.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 2):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 50.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 3):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 100.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 4):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 200.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 5):
            valor_saque = float(input("Digite um valor para saque: "))
        
            senha = input("Digite a sua senha para confirmar o saque:")
            
            if (senha == self.senha):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ {}".format(valor_saque))
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        else:
            print("Digite uma opção válida!")
    
    def Pix_Conta(self):
        print("---PIX---")
        
        chave_pessoa = input("Insira a chave PIX: ")
        print("A chave é {} ".format(chave_pessoa))
        print("----------------------------------")
        
        valor_pix = float(input("Insira o valor do PIX: "))
        print("Confirme o valor do PIX é {}".format(valor_pix))
        
        resp = input("Confirme a transação:_ y ou n ")
        
        if(resp == 'y'):
            print("Você fez um PIX de {} para {}".format(valor_pix, chave_pessoa))
        else:
            print("Encerrando a transação...")
    
    def Saldo_Conta(self):
        print("---SALDO---")
        print("O saldo da sua conta é: {}".format(self.dinheiro))
        print("-------------")
        
    def Pagamento_Conta(self):
        print("---PAGAMENTO---")
        print("{} , você deseja realizar o pagamento do boleto? ".format(self.nome)) 
        print("Seu saldo é {}".format(self.dinheiro))
        print("-------------")
    
    def Emprestimo_Conta(self):
        print("---EMPRÉSTIMO---")
        print("{}, você deseja realizar um empréstimo?".format(self.nome))
        print("Você tem um valor de R$ {} na sua conta disponível ".format(self.valor))
        
        resp = input("Fazer empréstimo: y/n  ")
        
        if(resp =='y'):
            print("Empréstimo efetivado!")
            print("Seu saldo agora é {} + {}".format(self.dinheiro, self.valor))
        else:
            print("Fim de operação!")
          
    def Depositar_Conta(self):
        print("{}, você deseja realizar o depósito de quanto?".format(self.nome))
        print("1. [ 50.00 ]")
        print("2. [ 100.00 ]")
        print("3. [ 200.00 ]")
        print("4. [ 500.00 ]")
        print("5. [ acima de 1000.00 ]")
        
        
        opcao = int(input("Digite a opção que você deseja realizar o depósito: "))
        resp = input("Confirme a transação:_ y ou n ")
        
        while (resp != 'n'):
            if (opcao == 1):
                print("{}, você realizou um depósito de 50.00! ".format(self.nome))
                return 0
            elif(opcao == 2):
                print("{}, você realizou um depósito de 100.00! ".format(self.nome))
                return 0
            elif( opcao == 3):
                print("{}, você realizou um depósito de 200.00! ".format(self.nome))
                return 0
            elif(opcao == 4):
                print("{}, você realizou um depósito de 500.00! ".format(self.nome))
                return 0
            elif(opcao == 5):
                print("{}, você realizou um depósito acima de 1000.00! ".format(self.nome))
                return 0
            else:
                print("Opção inválida!!!")