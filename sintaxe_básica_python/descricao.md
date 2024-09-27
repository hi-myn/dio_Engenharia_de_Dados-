# Desafio de Projeto: Criando um Sistema Bancário

Este desafio faz parte do Bootcamp de Engenharia de Dados oferecido pela [Digital Innovation One (DIO)](https://www.dio.me/) em parceria com a NTT Data.

## Objetivo Geral

O objetivo deste projeto é criar um sistema bancário utilizando a linguagem Python, com operações básicas de **saque**, **depósito** e **visualização de extrato**.

## Descrição do Desafio

Fomos contratados por um grande banco para desenvolver seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem **Python** como base do projeto. A primeira versão do sistema deve implementar as seguintes funcionalidades:

1. **Depósito**
2. **Saque**
3. **Extrato**

### Regras para as Operações

- **Operação de Depósito**:  
  - Deve ser possível depositar valores **positivos** na conta bancária.
  - A v1 do projeto trabalha apenas com um usuário, portanto não há necessidade de se preocupar com número de agência ou conta bancária.
  - Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

- **Operação de Saque**:  
  - O sistema deve permitir realizar até **3 saques diários**, com um limite máximo de **R$ 500,00 por saque**.
  - Caso o usuário não tenha saldo insuficiente em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
  - Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

- **Operação de Extrato**:  
  - A operação deve listar todos os **depósitos** e **saques** realizados na conta.
  - Ao fim da listagem, deve ser exibido o saldo atual da conta.
  - Se o extrato estiver em branco, exibir a mensagem: **"Não foram realizadas movimentações."**
  - Os valores devem ser exibidos no formato **R$ xxx.xx**, por exemplo:
    - 1500.45 = R$ 1500.45

## Solução Proposta

A implementação foi feita utilizando a linguagem Python, aproveitando as funcionalidades básicas para controle de fluxo e armazenamento dos dados. Para cada operação, são realizadas as seguintes etapas:

1. O sistema solicita ao usuário o valor a ser depositado ou sacado.
2. As operações são validadas conforme as regras descritas acima.
3. O extrato é gerado dinamicamente com base nas operações armazenadas e exibe o saldo final da conta.

Este projeto serve como base para entender a lógica por trás de sistemas bancários e como podemos estruturar suas operações de maneira simples e eficiente utilizando Python.

## Como Executar

1. Clone este repositório em sua máquina.
2. Abra o arquivo `sistema_bancario.py` no seu editor de código Python.
3. Execute o script e siga as instruções exibidas no terminal.

---

Desafio concluído com sucesso como parte do processo de aprendizado do Bootcamp de Engenharia de Dados!
