# Usuários

> Este módulo é responsável pelo gerenciamento de usuários da API, incluindo
> registro de novas contas e acesso ao perfil do usuário autenticado.
> As operações seguem boas práticas de segurança e controle de acesso.

## Registro de Usuário

Cria um novo usuário no sistema.

### Endpoint

`POST /api/v1/users/register/`
`Content-Type: application/json`

### Corpo da Requisição

```json
{
  "username": "usuario",
  "email": "usuario@email.com",
  "password": "senha_segura123"
}
```

### Reposta de Sucesso

```json
{
  "id": 1,
  "username": "usuario",
  "email": "usuario@email.com"
}
```

## Perfil do Usuário Autenticado

Retorna os dados do usuário autenticado.

`GET /api/v1/users/me/`
`Authorization: Bearer <ACCESS_TOKEN>`

### Resposta de Sucesso

```json
{
  "id": 1,
  "username": "usuario",
  "email": "usuario@email.com"
}
```

## Permissões

| Endpoint            | Permissão           |
| ------------------- | ------------------- |
| Registro de usuário | Público             |
| Perfil do usuário   | Usuário autenticado |

## Regras de Negócio

1.  Senha mínima de 8 caracteres

2.  Usuários são criados usando create_user

3.  Senhas são armazenadas de forma segura (hash)

4.  O usuário só pode acessar seus próprios dadoss

## Segurança

1.  Endpoints protegidos exigem autenticação JWT

2.  Tokens inválidos ou ausentes retornam HTTP 401 Unauthorized

3.  Não é permitido acesso a dados de outros usuários

## Considerações Finais

> O módulo de usuários foi projetado para garantir segurança, simplicidade
> e facilidade de manutenção, seguindo padrões comuns em APIs REST modernas.
