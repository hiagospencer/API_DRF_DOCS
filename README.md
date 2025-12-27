## 🚀 Django REST API – Products & Users

API REST profissional desenvolvida com Django REST Framework, seguindo boas práticas de mercado como separação de responsabilidades, Service Layer, JWT Authentication, filtros avançados, controle de permissões e documentação automática com Swagger (OpenAPI).

## 📌 Visão Geral

### Esta API fornece:

1.  Autenticação via JWT (Access + Refresh Token)

2.  Gerenciamento de Usuários

3.  CRUD completo de Produtos

4.  Filtros avançados e ordenação

5.  Controle de permissões por perfil

6.  Arquitetura limpa e escalável

7.  Documentação interativa com Swagger

O projeto é versionado (/api/v1/) e preparado para ambientes production-ready.

## 🛠️ Tecnologias Utilizadas

1.  Python 3.x

2.  Django

3.  Django REST Framework

4.  Django Filter

5.  Simple JWT

6.  DRF Spectacular (Swagger / OpenAPI)

7.  SQLite / PostgreSQL (compatível)

## 📂 Estrutura do Projeto
```
config/
│── urls.py
│── settings.py
│
apps/
├── products/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── services.py
│ ├── filters.py
│ ├── permissions.py
│ └── urls.py
│
├── users/
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
```
## 🧠 Arquitetura e Boas Práticas

🔹 Separação de Responsabilidades

| Camada             | Responsabilidade                    |
| ------------------ | ----------------------------------- |
| **views.py**       | Camada HTTP (requisição e resposta) |
| **serializers.py** | Validação e serialização de dados   |
| **services.py**    | Regras de negócio                   |
| **filters.py**     | Filtros e ordenações                |
| **permissions.py** | Controle de acesso                  |
| **urls.py**        | Versionamento e rotas               |

## 🔐 Autenticação (JWT)

A API utiliza JWT para autenticação.

### 🔑 Obter Token

`POST /api/v1/auth/token/`

### Body

```json
{
  "username": "admin",
  "password": "12345678"
}
```

### 🔄 Refresh Token

`POST /api/v1/auth/refresh/`

## 👤 Usuários

### 📍 Registrar Usuário

`POST /api/v1/users/register/`

```json
{
  "username": "user01",
  "email": "user@email.com",
  "password": "12345678"
}
```

### 📍 Usuário Logado

`GET /api/v1/users/me/`

🔐 Requer autenticação JWT

## 📦 Produtos

### 📍 Endpoints Principais

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

### 🔐 Permissões

1.  Leitura (GET): qualquer usuário autenticado

2.  Criação / Edição / Exclusão: apenas usuários is_staff

### Implementado via:

`IsAdminOrReadOnly`

## 🔍 Filtros Avançados (Products)

A API utiliza django-filter.

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

## ⚙️ Regras de Negócio (Service Layer)

Toda lógica crítica fica isolada em services.py.

### Exemplo:

1.  ❌ Não permite deletar produto com estoque:

```
if product.quantity > 0:
    raise ValidationError("Cannot delete product with stock")
```

Isso mantém:

1.  Views limpas

2.  Código testável

3.  Fácil manutenção

## 📖 Documentação da API

### Swagger disponível em:

`GET /api/docs/`

### Schema OpenAPI:

`GET /api/schema/`

## ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/hiagospencer/API_DRF_DOCS
```

### 2️⃣ Criar ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### 4️⃣ Migrar banco

```
python manage.py migrate

```

### 5️⃣ Criar superusuário

```
python manage.py createsuperuser
```

### 6️⃣ Rodar o servidor
```

python manage.py runserver

```

## 👨‍💻 Autor

> Projeto desenvolvido com foco em preparação para mercado de trabalho, seguindo padrões reais usados em empresas que utilizam Django REST Framework.
