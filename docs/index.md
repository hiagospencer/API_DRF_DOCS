# API Profissional com Django REST Framework

## Visão Geral

Esta documentação descreve uma **API profissional construída com Django REST Framework (DRF)**,
projetada para servir como base sólida para aplicações modernas, seguindo boas práticas
utilizadas em ambientes corporativos.

O projeto foi estruturado de forma modular, com foco em **segurança, escalabilidade,
manutenibilidade e facilidade de onboarding** para novos desenvolvedores.

---

## Objetivo do Projeto

O objetivo desta API é fornecer:

- Uma base **production-ready**
- Um exemplo realista de arquitetura de API REST
- Padrões claros para crescimento e manutenção
- Documentação acessível e completa

---

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- JWT (SimpleJWT)
- django-filter
- DRF Spectacular (OpenAPI / Swagger)
- MkDocs (Documentação)

---

## Funcionalidades Principais

- Autenticação JWT com refresh token
- CRUD completo de produtos
- Controle de permissões por endpoint
- Paginação automática
- Filtros avançados, busca e ordenação
- Versionamento da API

---

## Endpoints Principais

| Recurso  | Método | Rota                    | Descrição                     |
| -------- | ------ | ----------------------- | ----------------------------- |
| Auth     | POST   | /api/v1/auth/token/     | Obter token JWT               |
| Auth     | POST   | /api/v1/auth/refresh/   | Renovar token JWT             |
| Users    | GET    | /api/v1/users/me/       | Perfil do usuário autenticado |
| Users    | POST   | /api/v1/users/register/ | Criar novo usuário            |
| Products | GET    | /api/v1/products/       | Listar produtos               |
| Products | POST   | /api/v1/products/       | Criar produto (staff)         |
| Products | GET    | /api/v1/products/{id}/  | Detalhar produto              |
| Products | PUT    | /api/v1/products/{id}/  | Atualizar produto (staff)     |
| Products | DELETE | /api/v1/products/{id}/  | Remover produto (staff)       |

---

## Documentação da API

A API possui documentação automática baseada em **OpenAPI**:

- `GET /api/schema/` → Esquema OpenAPI
- `GET /api/docs/` → Swagger UI

Esses endpoints permitem explorar e testar a API diretamente pelo navegador.

---

## Como Utilizar a Documentação

Esta documentação está organizada da seguinte forma:

- **Visão Geral** → Introdução e objetivos
- **Autenticação** → Fluxo JWT e segurança
- **Usuários** → Registro e perfil
- **Produtos** → CRUD, filtros e ordenação
- **Arquitetura** → Decisões técnicas e organização interna
- **Convenções** → Padrões adotados no projeto

---

## Rodando a Documentação Localmente

No terminal, instale as dependências:

```bash
pip install mkdocs mkdocs-material
```

```
pip install mkdocs mkdocs-material
```

### Rodar Servidor

`mkdocs serve`

Abra no navegador:

```
http://127.0.0.1:8000

```
