### Desafio de Projeto 1 - Python ###

# SISTEMA BANCÁRIO # V1

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato. 

1 - Depósito

Deve ser possível depositar valores positivos para a conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato. 

2 - Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato. 

3 - Extrato 

Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido o saldo atual da conta. 
Os valores devem ser exibidos utilizando o formato R$ xxx.xx 

# SISTEMA BANCÁRIO # V2 

1 - Criar função para as features existentes (Depósito, Saque e Extrato).

A função "Depósito" deve receber os argumentos apenas por posição (positional only). 
A função "Saque" deve receber os argumentos apenas por nome (keyword only).
A função "Extrato" deve receber os argumentos por posição e nome (positional only e keyword only).

2 - Criar uma função para cadastro de usuários. 

O usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato logradouro, número, bairro, cidade e estado. 
A função deverá validar o usuário para não permitir 2 cpfs iguais. 

3 - Criar uma função para cadastrao de conta corrente. 

As contas deverão ser armazenadas em uma lista, possuinto agência, número da conta e usuário. 
O número da conta é sequencial, iniciante em 1. O número da agência é fixo, 0001. 
O usuário poderá ter mais de uma conta, mas uma conta pertence a somente um usuário. 