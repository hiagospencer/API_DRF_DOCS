# Arquitetura do Sistema

## Visão Geral

Este projeto foi desenvolvido seguindo princípios de **arquitetura limpa** e
**separação de responsabilidades**, visando escalabilidade, manutenção facilitada
e clareza para novos desenvolvedores.

A arquitetura foi pensada para suportar crescimento do sistema sem acoplamento excessivo
entre as camadas.

---

## Princípios Arquiteturais

- Separation of Concerns (SoC)
- Single Responsibility Principle (SRP)
- Service Layer Pattern
- APIs stateless
- Segurança por padrão (secure by default)

---

## C4 Model — Contexto

Visão de alto nível mostrando como usuários interagem com o sistema.

```
flowchart LR
User[Usuário / Cliente] -->|HTTP| API[Django REST API]
API --> DB[(Banco de Dados)]
```

## C4 Model — Containers

Mostra os principais containers que compõem a aplicação.

```
flowchart LR
    Client[Frontend / Mobile / Integrações] -->|REST| DjangoAPI[Django REST Framework]
    DjangoAPI -->|ORM| PostgreSQL[(PostgreSQL)]
```

## C4 Model — Componentes

Demonstra a organização interna da API.

```
flowchart TB
    View[Views / ViewSets]
    Serializer[Serializers]
    Service[Services]
    Model[Models]
    Filter[Filters]
    Permission[Permissions]

    View --> Serializer
    View --> Service
    View --> Filter
    View --> Permission
    Service --> Model
```

## Fluxo de Requisição

Exemplo de fluxo para uma requisição autenticada:

1.  Cliente envia requisição HTTP

2.  Middleware valida autenticação JWT

3.  View recebe a requisição

4.  Serializers validam os dados

5.  Services executam regras de negócio

6.  Models interagem com o banco de dados

7.  Resposta é retornada ao cliente

## Reponsabilidade de Cada Camada

1.  Views

    1.  Recebem requisições HTTP

    2.  Definem permissões e autenticação

    3.  Delegam regras de negócio para Services

2.  Serializers

    1.  Validação de dados de entrada

    2.  Transformação de dados para JSON

    3.  Controle de campos expostos

3.  Services

    1.  Centralizam regras de negócio

    2.  Evitam lógica complexa nas views

    3.  Facilitam testes unitários

4.  Models

    1.  Representam entidades do domínio

    2.  Gerenciam persistência de dados

5.  Filters

    1.  Encapsulam regras de busca e filtragem

    2.  Mantêm as views simples

6.  Permissions

    1.  Controlam acesso aos recursos

    2.  Garantem segurança por endpoint

7.  Decisões Arquiteturais Importantes

    1.  Views mantidas leves (thin views)

    2.  Regras de negócio isoladas em services

    3.  Autenticação stateless via JWT

    4.  Versionamento da API via URL (/api/v1/)

    5.  Documentação automática com OpenAPI

8.  Escalabilidade e Evolução

    1.  A arquitetura permite:

    2.  Adição de novos módulos sem impacto nos existentes

    3.  Criação de novas versões da API

    4.  Substituição do banco de dados sem afetar a camada HTTP

    5.  Evolução para arquitetura de microserviços, se necessário

## Considerações Finais

> Esta arquitetura segue padrões amplamente utilizados no mercado e foi projetada
> para atender requisitos reais de aplicações em produção, facilitando manutenção,
> testes e onboarding de novos desenvolvedores.
