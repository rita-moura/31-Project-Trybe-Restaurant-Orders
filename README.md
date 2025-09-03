# 🍽️ Projeto Restaurant Orders

Este projeto é um sistema de gerenciamento de pedidos para uma lanchonete, desenvolvido como parte do currículo da Trybe. O sistema é capaz de controlar os pedidos dos clientes, os pratos consumidos, os dias de visita e o estoque de ingredientes.

## 🎯 Objetivo

O objetivo principal é implementar uma classe que centraliza e gerencia as informações de uma lanchonete, utilizando estruturas de dados eficientes para rastrear:

- O histórico de pedidos de cada cliente.
- Os dias em que um cliente frequentou a lanchonete.
- O prato que um cliente nunca pediu.
- O dia em que um determinado prato nunca foi pedido.

## ✨ Funcionalidades

- Adicionar novos pedidos para clientes.
- Rastrear o histórico de pedidos de cada cliente.
- Verificar os dias em que um cliente frequentou a lanchonete.
- Calcular o valor total da conta de um cliente.
- Controlar o inventário de pratos disponíveis.

## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3**
- **FastAPI**
- **Programação Orientada a Objetos (POO)**
- **Estruturas de Dados:** Dicionários e Conjuntos (sets) para otimizar a busca e o armazenamento de dados.
- **`pytest`**: Para a execução dos testes automatizados.

## 📂 Estrutura do Projeto

- **`data/`**: Contém os dados base para o cardápio e inventário.
- **`src/`**: Pasta contendo todo o código-fonte desenvolvido para a solução do projeto.
- **`tests/`**: Pasta com os testes.
- **`dev-requirements.txt`**: Dependências de desenvolvimento.
- **`requirements.txt`**: Dependências do projeto.
- **`init.sh`**: Script para setup do ambiente.
- **`test.sh`**: Script para execução dos testes.
- **`pyproject.toml`**: Arquivo de configuração do projeto.


## 🚀 Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone git@github.com:rita-moura/Project_Restaurant_Orders.git
    cd Project_Restaurant_Orders
    ```

2.  **Crie e ative um ambiente virtual e instale as dependecias:**
    ```bash
    bash init.sh
    ```

3.  **Para desativar o ambiente virtual:**
    ```bash
    deactivate
    ```

## ✅ Executando os Testes

Para verificar se a sua solução atende a todos os requisitos, execute os testes com o Pytest:

```bash
bash test.sh