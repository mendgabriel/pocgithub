# Git Flow — Fluxo de Trabalho

Este documento descreve como o projeto utiliza **Git Flow**, um modelo de branches amplamente usado em empresas de tecnologia.

## Branches principais

| Branch | Propósito | Quem usa |
|---|---|---|
| `main` | Código em **produção** — sempre estável | Release final |
| `develop` | Código em **desenvolvimento** — integração de features | Equipe de dev |

## Branches temporárias

| Branch | Origem | Destino | Exemplo |
|---|---|---|---|
| `feature/*` | `develop` | `develop` | `feature/excluir-pessoa` |
| `release/*` | `develop` | `main` + `develop` | `release/1.1.0` |
| `hotfix/*` | `main` | `main` + `develop` | `hotfix/corrigindo-readme` |

## Fluxo de uma nova feature

```
main ─────────────────────────────────────────────► (produção)
  │
develop ──────┬───────────────────────────────────► (integração)
              │
feature/xxx ──┘  (desenvolvimento isolado)
```

### Passo a passo (como em uma empresa)

**1. Receber a tarefa**

Exemplo de user story:
> Como usuário, quero excluir um cadastro para remover dados incorretos.

**2. Atualizar a branch develop**

```bash
git checkout develop
git pull origin develop
```

**3. Criar a branch da feature**

```bash
git checkout -b feature/excluir-pessoa develop
```

**4. Desenvolver e commitar**

```bash
git add .
git commit -m "feat: adiciona endpoint DELETE /pessoas/{id}"
git commit -m "feat: adiciona botão de exclusão na interface web"
```

**5. Enviar para o GitHub**

```bash
git push -u origin feature/excluir-pessoa
```

**6. Abrir Pull Request**

- Base: `develop`
- Compare: `feature/excluir-pessoa`
- Descrever o que foi feito e como testar

**7. Code Review**

Em equipes reais, outro desenvolvedor revisa o código antes do merge.

**8. Merge na develop**

Após aprovação, a feature entra na `develop`.

**9. Release para produção**

Quando há features suficientes:

```bash
git checkout -b release/1.1.0 develop
# testes finais, ajustes de versão
git checkout main
git merge release/1.1.0
git tag v1.1.0
git checkout develop
git merge release/1.1.0
```

## Convenção de commits

| Prefixo | Uso | Exemplo |
|---|---|---|
| `feat:` | Nova funcionalidade | `feat: adiciona exclusão de pessoas` |
| `fix:` | Correção de bug | `fix: corrige validação de e-mail` |
| `docs:` | Documentação | `docs: atualiza README` |
| `refactor:` | Refatoração | `refactor: extrai lógica do banco` |

## Feature implementada neste fluxo

**Branch:** `feature/excluir-pessoa`

**O que foi adicionado:**
- Endpoint `DELETE /pessoas/{id}` na API
- Botão "Excluir" na página web com confirmação
- Tratamento de erro 404 quando pessoa não existe
