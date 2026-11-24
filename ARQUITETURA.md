# RELATÓRIO DE ARQUITETURA – TECHFLOW CORE

## 1. Identificação do Projeto

**Nome:** TechFlow Core  
**Linguagem:** Python  
**Tipo de aplicação:** CLI  

## 2. Arquitetura do Sistema

O TechFlow Core será desenvolvido utilizando Python, com uma arquitetura modular, permitindo separar as responsabilidades do sistema em diferentes arquivos.

A aplicação será organizada para facilitar a manutenção, a leitura e a evolução do código.

## 3. Tecnologias Utilizadas

- Python: linguagem principal do projeto.
- VS Code: ambiente de desenvolvimento.
- SQLite3: banco de dados para armazenamento das informações.
- JSON: formato utilizado para trabalhar com dados de APIs.
- urllib.request: biblioteca para realizar requisições HTTP.
- Git e GitHub: controle de versão e armazenamento do projeto.

## 4. Funcionamento do Sistema

O sistema permitirá:

- Cadastrar novas demandas.
- Listar demandas cadastradas.
- Atualizar informações das demandas.
- Excluir demandas.
- Consultar informações de CEP.
- Consultar conversão de moedas.
- Filtrar demandas por prioridade.

## 5. Justificativa da Escolha do Python CLI

A escolha do Python ocorreu devido à sua sintaxe simples, facilidade de manutenção e disponibilidade de bibliotecas nativas.

A interface CLI foi escolhida por permitir a interação direta com o usuário pelo terminal, sem exigir o desenvolvimento de uma interface gráfica.

Essa abordagem facilita o desenvolvimento, os testes e a implementação das funcionalidades.

## 6. Organização dos Arquivos

A estrutura planejada do projeto será:

```text
TechFlow-Core/
│
├── main.py
├── utils.py
├── requisitos.md
├── arquitetura.md
├── testes.md
├── README.md
└── banco.db
```

## 7. Considerações Finais

A arquitetura proposta busca garantir organização, modularidade, facilidade de manutenção e possibilidade de expansão do TechFlow Core.