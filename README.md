# Cadastro de Pessoas

Projeto acadêmico simples para cadastrar e listar pessoas usando **Python**, **FastAPI**, **MySQL**, **Docker** e **GitHub**.

## Descrição do projeto

Esta aplicação permite:

- Cadastrar pessoas com **nome** e **e-mail**
- Visualizar todas as pessoas cadastradas

A solução possui:

- Uma **API REST** em Python (FastAPI)
- Um **banco de dados MySQL**
- Uma **página HTML** para interagir com a API
- **Docker Compose** para subir tudo com um único comando

## Tecnologias utilizadas

| Tecnologia | Função no projeto |
|---|---|
| **Python** | Linguagem principal da API |
| **FastAPI** | Framework para criar a API de forma simples |
| **MySQL** | Banco de dados relacional |
| **SQLAlchemy** | Biblioteca que conecta Python ao MySQL |
| **Docker** | Empacota a aplicação em containers |
| **Docker Compose** | Sobe a API e o MySQL juntos |
| **HTML + JavaScript** | Página web para cadastro e listagem |
| **Git / GitHub** | Controle de versão e publicação do código |

## Estrutura de pastas

```
pocgithub/
├── app/
│   ├── __init__.py      # Marca a pasta como pacote Python
│   ├── main.py          # API FastAPI (rotas e inicialização)
│   ├── database.py      # Conexão com o MySQL
│   ├── models.py        # Tabela "pessoas" no banco
│   └── schemas.py       # Validação dos dados de entrada/saída
├── static/
│   └── index.html       # Página web do cadastro
├── Dockerfile           # Receita do container Python
├── docker-compose.yml   # Orquestra API + MySQL
├── requirements.txt     # Dependências Python
├── .gitignore           # Arquivos que o Git deve ignorar
└── README.md            # Este arquivo
```

## Pré-requisitos

Você precisa ter instalado:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows ou Mac)
- [Git](https://git-scm.com/downloads)

> **Nota:** Não é necessário instalar Python ou MySQL manualmente na sua máquina. O Docker cuida disso dentro dos containers.

## Como instalar o Docker

1. Acesse: https://www.docker.com/products/docker-desktop/
2. Baixe o **Docker Desktop** para o seu sistema operacional
3. Instale e reinicie o computador, se solicitado
4. Abra o Docker Desktop e aguarde ele iniciar
5. Teste no terminal:

```bash
docker --version
docker compose version
```

Se os dois comandos mostrarem a versão, o Docker está pronto.

## Como clonar o projeto do GitHub

Depois de publicar o repositório no GitHub, qualquer pessoa pode baixar o projeto com:

```bash
git clone https://github.com/SEU_USUARIO/pocgithub.git
cd pocgithub
```

Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

## Como executar o projeto

Na pasta do projeto, execute:

```bash
docker compose up --build
```

O que esse comando faz:

- `--build` → constrói a imagem da API
- `up` → sobe os containers da API e do MySQL

Na primeira execução, pode demorar alguns minutos para baixar as imagens.

Para parar os containers, pressione `Ctrl + C` no terminal ou execute:

```bash
docker compose down
```

## Como acessar a aplicação

Com os containers rodando, abra no navegador:

- **Página web:** http://localhost:8000
- **Documentação Swagger da API:** http://localhost:8000/docs

### Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/pessoas` | Cadastra uma nova pessoa |
| `GET` | `/pessoas` | Lista todas as pessoas |

Exemplo de cadastro via Swagger ou curl:

```json
{
  "nome": "Maria Silva",
  "email": "maria@email.com"
}
```

## Como publicar no GitHub

### 1. Inicializar o repositório Git

```bash
git init
```

Cria a pasta `.git` e começa a rastrear o projeto.

### 2. Adicionar os arquivos

```bash
git add .
```

Prepara todos os arquivos para o commit (exceto os listados no `.gitignore`).

### 3. Criar o primeiro commit

```bash
git commit -m "Primeiro commit: projeto de cadastro de pessoas"
```

Salva uma "foto" do projeto no histórico do Git.

### 4. Renomear a branch principal

```bash
git branch -M main
```

Define `main` como nome da branch principal.

### 5. Conectar ao GitHub

Crie um repositório vazio no GitHub (sem README) e execute:

```bash
git remote add origin https://github.com/SEU_USUARIO/pocgithub.git
```

Vincula o projeto local ao repositório remoto.

### 6. Enviar o código

```bash
git push -u origin main
```

Envia o código para o GitHub.

## Como qualquer pessoa pode executar

Qualquer pessoa com Docker instalado pode rodar o projeto:

1. Clonar o repositório
2. Entrar na pasta do projeto
3. Executar `docker compose up --build`
4. Acessar http://localhost:8000

Não é necessário configurar banco de dados manualmente.

## Solução de problemas

| Problema | Possível solução |
|---|---|
| Porta 8000 em uso | Pare outros serviços na porta 8000 ou altere a porta no `docker-compose.yml` |
| Docker não encontrado | Verifique se o Docker Desktop está aberto |
| Erro de conexão com MySQL | Aguarde o container `db` ficar saudável e rode `docker compose up --build` novamente |

## Autor

Projeto acadêmico — Cadastro de Pessoas com Python, FastAPI, MySQL e Docker.
