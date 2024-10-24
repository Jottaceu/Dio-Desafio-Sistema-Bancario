# Dio- Criar Desafio Sistema Bancario
Criando um sistema bancário com as operações: sacar, depositar e visualizar extrato.

# Desafio
Desenvolver o novo sistema para um Banco.
Para a primeira versão do sistema foi implementado apenas 3 operações: depósito, saque e extrato.

## Operação de depósito
Deve se rpossível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisa se preocupar em identificar qual é o número da agência e conta bancária.Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 porsaque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato:
R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
