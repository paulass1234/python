from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
from secretario import Secretario
from presidente import Presidente

func1 = Funcionario('Maria', '111.111.111-11', 2500.00, '123456')
func1.Bonificacao()

ger1 = Gerente('José', '222.222.222-22', 3500.00, '123456789', 10)

dir1 = Diretor('Marcos', '333.333.333-33', 4500.00, '1234')

sec1 = Secretario('Josefa', '444.444.444-44', 2000.00, '12345')

pre1 = Presidente('Paulo', '555.555.555-55', 10000.00, '1234567')