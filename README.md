# Cadastro de Pessoas — API REST Full Stack

Aplicação web completa para cadastro e listagem de pessoas, desenvolvida com **Python**, **FastAPI**, **MySQL** e **Docker**. Projeto de portfólio demonstrando integração entre backend, banco de dados, frontend e containerização.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red)

---

## Sobre o projeto

Sistema CRUD básico (Create + Read) com arquitetura em camadas:

- **Frontend:** página HTML com JavaScript consumindo a API via `fetch`
- **Backend:** API REST com FastAPI e validação de dados (Pydantic)
- **Banco de dados:** MySQL com SQLAlchemy ORM
- **Infraestrutura:** Docker Compose com 2 containers (API + MySQL)

Ideal para demonstrar conhecimentos em desenvolvimento backend, persistência de dados e DevOps básico.

---

## Funcionalidades

- Cadastro de pessoas (nome + e-mail)
- Listagem de todas as pessoas cadastradas
- Validação de e-mail e bloqueio de duplicatas
- Documentação interativa automática (Swagger)
- Ambiente containerizado — roda com um comando

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.11, FastAPI, Uvicorn |
| Banco de dados | MySQL 8.0, SQLAlchemy, PyMySQL |
| Frontend | HTML, CSS, JavaScript |
| DevOps | Docker, Docker Compose |
| Versionamento | Git, GitHub |

---

## Arquitetura

```
Navegador (HTML + JS)
        │  HTTP (JSON)
        ▼
   API FastAPI (Python)
        │  SQL
        ▼
     MySQL 8.0
```

**Containers Docker:**

| Container | Função | Porta |
|---|---|---|
| `api_cadastro` | API FastAPI | 8000 |
| `mysql_cadastro` | Banco MySQL | 3306 |

---

## API Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Página web |
| `POST` | `/pessoas` | Cadastra uma pessoa |
| `GET` | `/pessoas` | Lista todas as pessoas |
| `GET` | `/docs` | Documentação Swagger |

**Exemplo de requisição:**

```json
POST /pessoas
{
  "nome": "Maria Silva",
  "email": "maria@email.com"
}
```

---

## Como executar

**Pré-requisito:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado.

```bash
git clone https://github.com/mendgabriel/pocgithub.git
cd pocgithub
docker compose up --build
```

Acesse:

- **Aplicação:** http://localhost:8000
- **Swagger:** http://localhost:8000/docs

Para parar:

```bash
docker compose down
```

---

## Estrutura do projeto

```
pocgithub/
├── app/
│   ├── main.py          # Rotas da API
│   ├── database.py      # Conexão com MySQL
│   ├── models.py        # Modelo da tabela pessoas
│   └── schemas.py       # Validação Pydantic
├── static/
│   └── index.html       # Interface web
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Competências demonstradas

- Desenvolvimento de API REST
- Integração com banco de dados relacional (ORM)
- Validação e tratamento de erros
- Containerização com Docker
- Versionamento com Git/GitHub
- Documentação de projeto

---

## Autor

**Gabriel Mendonça** — [GitHub](https://github.com/mendgabriel)

---

## Licença

Este projeto é de código aberto e está disponível para fins de estudo e portfólio.
