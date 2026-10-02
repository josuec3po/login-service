# Login Service

## Descrição
Repositório voltado a um projeto pessoal unindo **desenvolvimento de software** e **práticas de cibersegurança** . O objetivo é construir um sistema de autenticação via terminal(simples) aplicando conceitos de arquitetura modular, proteção contra SQL Injection (Prepared Statements) e manipulação segura de banco de dados.

## Tecnologias
* **Python** 
* **SQLite3** 

## Progresso

### Dia 1 - Estrutura Básica
* [x] Criação de funções de cadastro, login
* [x] Criação do banco de dados
* [ ] Validação das funções (Existência, TypeError etc)

## Estrutura do Projeto
* `main.py`: Gerencia a interface do terminal e o loop do menu.
* `funcoes.py`: Processa as regras de negócio e a comunicação com o banco de dados.
* `db.py`: Responsável pelo setup inicial e criação estrutural do banco.