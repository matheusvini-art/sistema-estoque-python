# Sistema de Controle de Produtos e Validade

Projeto Integrador desenvolvido em Python para apoiar pequenos comerciantes no cadastro, na consulta e no acompanhamento da validade de produtos.

## Autor

**Mateus Vinícius Duarte**  
Curso: Análise e Desenvolvimento de Sistemas  
RA: 5965101  
E-mail: mateusviniciusduartesouza@gmail.com

## Sobre o projeto

O sistema foi desenvolvido como um protótipo de aplicação de terminal para pequenos estabelecimentos que precisam manter um registro simples de produtos. A aplicação permite realizar um cadastro básico de usuário, efetuar login, cadastrar produtos, salvar os dados em um arquivo JSON e consultar produtos pelo nome.

Além do cadastro e da consulta, o sistema analisa a data de vencimento informada. O produto pode ser classificado como vencido, próximo do vencimento ou dentro do prazo.

## Funcionalidades implementadas

- Identificação inicial do usuário;
- cadastro de usuário durante a execução do programa;
- login com validação de usuário e senha;
- bloqueio do acesso quando o cadastro ainda não foi realizado;
- cadastro de produtos com nome, marca e data de vencimento;
- validação de campos obrigatórios;
- validação da data no formato `dd/mm/aaaa`;
- persistência dos produtos no arquivo `estoque.json`;
- carregamento dos produtos salvos quando o arquivo já existe;
- consulta de produto pelo nome;
- comparação sem diferenciação entre letras maiúsculas e minúsculas na consulta;
- identificação de produto não encontrado;
- alerta para produto vencido;
- alerta para produto próximo do vencimento, quando faltam até sete dias;
- mensagem para produto dentro do prazo;
- encerramento pelos menus do sistema.

## Tecnologias utilizadas

- Python 3;
- módulo `json`, da biblioteca padrão do Python;
- módulo `datetime`, da biblioteca padrão do Python;
- arquivo JSON para persistência local;
- execução em terminal, PowerShell ou console integrado do PyCharm.

O projeto não utiliza bibliotecas externas. Portanto, não é necessário executar `pip install` para rodar a versão atual.

## Requisitos para execução

- Python 3 instalado;
- Windows, Linux ou macOS;
- PyCharm, Visual Studio Code ou outro terminal compatível;
- permissão de leitura e gravação na pasta do projeto.

## Como executar no Windows

### Pelo PowerShell ou Prompt de Comando

1. Instale o Python 3 pelo site oficial: <https://www.python.org/downloads/>.
2. Baixe ou clone este repositório.
3. Abra o PowerShell na pasta do projeto.
4. Execute o arquivo principal:

```powershell
python Projetointegrador.py
```

Caso o comando `python` não seja reconhecido, tente:

```powershell
py Projetointegrador.py
```

### Pelo PyCharm

1. Abra o PyCharm.
2. Selecione **Open** e escolha a pasta do projeto.
3. Abra o arquivo `Projetointegrador.py`.
4. Confira se o interpretador Python 3 está selecionado.
5. Clique no botão **Run** ou pressione `Shift + F10`.
6. Responda às perguntas no painel **Run**.

## Fluxo de utilização

Ao iniciar, o programa solicita o nome do usuário e apresenta três opções:

```text
1 - Fazer Login
2 - Cadastrar
3 - Sair
```

Caso ainda não exista um cadastro durante a execução, selecione a opção `2`, informe um usuário e uma senha e, em seguida, selecione a opção `1` para realizar o login.

Depois do login, o sistema apresenta o menu do estoque:

```text
1 - Cadastrar um produto
2 - Verificar estoque
3 - Sair do sistema
```

Na opção de cadastro, informe:

- nome do produto;
- marca do produto;
- data de vencimento no formato `dd/mm/aaaa`.

Na opção de consulta, informe o nome do produto que deseja localizar. O sistema exibirá nome, marca, vencimento e a situação da validade.

## Regra de validade

A aplicação compara a data informada com a data atual do computador:

| Condição | Mensagem apresentada |
|---|---|
| Data anterior à atual | Produto vencido |
| De zero a sete dias restantes | Produto próximo do vencimento |
| Mais de sete dias restantes | Produto dentro do prazo |

A regra utiliza dias corridos e uma janela fixa de até sete dias para o alerta de proximidade.

## Persistência dos dados

Os produtos são armazenados no arquivo `estoque.json`, criado na pasta de execução do programa. O arquivo utiliza uma lista de registros, e cada produto possui as seguintes informações:

```json
[
    {
        "nome": "Biscoito",
        "marca": "Adria",
        "data": "05/12/2026"
    }
]
```

Quando o programa é executado novamente e o arquivo existe, os produtos são carregados para consulta. O cadastro de usuário não é persistido nesta versão: usuário e senha permanecem disponíveis apenas durante a execução atual.

## Testes realizados

Os principais cenários funcionais testados foram:

| ID | Cenário | Resultado |
|---|---|---|
| T01 | Login sem cadastro | O sistema solicita que o usuário realize o cadastro. |
| T02 | Cadastro de usuário | Usuário e senha são registrados durante a execução. |
| T03 | Login correto | O acesso ao menu do estoque é liberado. |
| T04 | Login incorreto | O sistema informa que usuário ou senha estão incorretos. |
| T05 | Campo de produto vazio | O produto não é cadastrado e uma mensagem é exibida. |
| T06 | Data inválida | O cadastro é interrompido e o formato correto é informado. |
| T07 | Cadastro de produto | O produto é salvo no arquivo `estoque.json`. |
| T08 | Consulta de produto existente | Os dados e a situação da validade são exibidos. |
| T09 | Consulta de produto inexistente | O sistema informa que o produto não foi encontrado. |
| T10 | Produto vencido | O sistema apresenta alerta de vencimento. |
| T11 | Produto próximo do vencimento | O sistema apresenta alerta quando faltam até sete dias. |
| T12 | Produto dentro do prazo | O sistema informa a quantidade de dias restantes. |

## Limitações conhecidas

A versão atual é um protótipo inicial e não implementa:

- controle de quantidade numérica;
- entradas e saídas de mercadorias;
- saldo quantitativo de estoque;
- edição ou exclusão de produtos;
- persistência do usuário após o encerramento;
- armazenamento de senha com hash;
- perfis ou níveis de permissão;
- banco de dados relacional;
- interface gráfica ou aplicação web;
- backup automático;
- relatórios;
- tratamento de letras digitadas nos campos que esperam opções numéricas.

Essas características podem ser desenvolvidas em versões futuras. A ausência delas não faz parte do escopo funcional desta versão acadêmica.

## Possíveis evoluções

Como continuidade do projeto, podem ser implementados:

- funções separadas para autenticação, persistência, cadastro e consulta;
- tratamento seguro de opções não numéricas;
- persistência de usuários;
- hash de senhas;
- controle de quantidade;
- entradas e saídas de produtos;
- edição e exclusão de registros;
- relatórios;
- banco de dados SQLite ou outro SGBD;
- interface gráfica ou aplicação web;
- backup e restauração dos dados.

## Estrutura básica do projeto

```text
projeto/
├── Projetointegrador.py
├── estoque.json       # criado automaticamente após o primeiro cadastro de produto
└── README.md
```

## Observação acadêmica

Este repositório corresponde à versão do sistema apresentada no Projeto Integrador. O sistema foi documentado de acordo com as funcionalidades efetivamente implementadas no código. As funcionalidades listadas como evoluções futuras não devem ser consideradas recursos disponíveis na versão atual.
