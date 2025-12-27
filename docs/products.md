## Visão Geral

Este módulo gerencia produtos com funcionalidades completas de CRUD.

---

## Filtros

A listagem de produtos suporta filtros avançados via query parameters.

### Filtros de Preço

| Parâmetro   | Descrição    |
| ----------- | ------------ |
| min_price   | Preço mínimo |
| max_price   | Preço máximo |
| exact_price | Preço exato  |

**Exemplo:**

`GET /api/v1/products/?min_price=100&max_price=500`

### Filtros por Nome

| Parâmetro   | Descrição                        |
| ----------- | -------------------------------- |
| name        | Busca parcial (case-insensitive) |
| name_exact  | Nome exato                       |
| name_starts | Nome começa com                  |

**Exemplo:**

`GET /api/v1/products/?name=camisa`

### Filtros de Estoque

| Parâmetro    | Descrição          |
| ------------ | ------------------ |
| in_stock     | Produto em estoque |
| min_quantity | Quantidade mínima  |
| max_quantity | Quantidade máxima  |

**Exemplo:**

`GET /api/v1/products/?in_stock=true&min_quantity=5`

### Filtros por Data de Criaçao

| Parâmetro      | Descrição             |
| -------------- | --------------------- |
| created_after  | Criados após a data   |
| created_before | Criados antes da data |

**Exemplo:**

`GET /api/v1/products/?created_after=2024-01-01`

## Ordenação

A ordenação pode ser feita pelos campos:

1.  price

2.  created_at

3.  name

4.  quantity

**Exemplo:**

`GET /api/v1/products/?ordering=-price`

## Observação

1.  Todos os filtros podem ser combinados
2.  A busca é case-insensitive
3.  A paginação contínua funcionando normalmente

## Permissões

Leitura: usuários autenticados

Escrita: usuários staff/admin
