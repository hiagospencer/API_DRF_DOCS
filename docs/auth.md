# Autenticação e Segurança

## Visão Geral

Esta API utiliza **JWT (JSON Web Token)** para autenticação stateless, garantindo segurança,
escalabilidade e independência de sessão no servidor.

A autenticação é baseada em tokens e segue o padrão **Bearer Token** via header HTTP.

### Biblioteca Utilizada

- `djangorestframework-simplejwt`

---

## Conceitos Importantes

### Access Token

- Token de curta duração
- Utilizado em todas as requisições protegidas
- Enviado no header `Authorization`

### Refresh Token

- Token de longa duração
- Utilizado apenas para gerar um novo access token
- Não deve ser enviado em requisições comuns

---

## Fluxo de Autenticação

1. O usuário envia suas credenciais (username e password)
2. A API valida as credenciais
3. A API retorna um **access token** e um **refresh token**
4. O cliente utiliza o access token para acessar endpoints protegidos
5. Quando o access token expira, o refresh token é usado para gerar um novo

---

## Endpoints de Autenticação

### Obter Token JWT

`POST /api/v1/auth/token/`
`Content-Type: application/json`

## Corpo da Requisição

```json
{
  "username": "usuario",
  "password": "senha"
}
```

## Resposta de Sucesso

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### Renovar Access Token

`POST /api/v1/auth/refresh/`
`Content-Type: application/json`

## Corpo da Requisição

```json
{
  "refresh": "jwt_refresh_token"
}
```

## Resposta de Sucesso

```json
{
  "access": "novo_jwt_access_token"
}
```

## Uso do Token nas Requisições

Todo os endpoints protegidos exigem o envio do access token no header:

`Authorization: Bearer <ACCESS_TOKEN>`

⚠️ Requisições sem token ou com token inválido retornarão HTTP 401 Unauthorized.

## Segurança e Boa Práticas

### Recomendações

1.  Nunca exponha tokens em URLs

2.  Nunca armazene tokens em texto puro

3.  Utilize HTTPS em produção

4.  Utilize expiração curta para access tokens

5.  Utilize refresh tokens apenas quando necessário

6.  Faça rotação de secrets em produção

## Erros comuns

### Credenciais Inválidas

```
{
"detail": "No active account found with the given credentials"
}
```

### Token Expirado ou Inválido

```
{
"detail": "Given token not valid for any token type"
}
```

### Considerações Finais

> A autenticação JWT permite que a API seja escalável e desacoplada de sessão,
> sendo ideal para aplicações modernas como SPAs, mobile apps e integrações externas.
