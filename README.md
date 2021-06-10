# wishlist
## Motivação

O projeto foi desenvolvido utilizando Python juntamente com o framework FastAPI para a criação das APIs para o projeto de lista de desejo. Como banco de dados foi utilizado o PostgreSQL.
Além disso foi utilizado o Docker para a implantação da API.

## Execução

Para executar a aplicação no local será necessário ter o Docker instalado e rodar o seguinte comando:

```
docker compose up --build
```

Se não possuir o Docker instalado basta seguir o [tutorial](https://www.notion.so/Instalando-o-Docker-e9ee20c07444455fa40675de80696a6e) para a instalação.

## APIs

### Documentação OpenAPI 3.0

Para acessar a documentação OpenAPI 3.0 acessar a url no navegador:

```
http://localhost:8080/docs
```

#### Endpoint criar novos usuários

##### Método: POST
##### URL: http://localhost:8080/user/

Parâmetros que serão passados para essa API:
```
{
    "email": <Email do usuario>,
    "name": <Nome do usuario>
    "password": <Senha do usuario>
}
```
Resposta esperada:
```
{
    "email": <Email do usuario 1>,
    "name": <Nome do usuario 1>,
    "id": <Id do usuario>,
    "items": []
}
```

#### Endpoint obter todos usuários do banco

##### Método: GET
##### URL: http://localhost:8080/users/

Resposta esperada:
```
[
    {
        "email": <Email do usuario 1>,
        "name": <Nome do usuario 1>,
        "id": 1
    },
    {
        "email": <Email do usuario 2>,
        "name": <Nome do usuario 2>,
        "id": 2
    },
    ...
]
```

#### Endpoint obter detalhes de um usuário específico

##### Método: GET
##### URL: http://localhost:8080/users/{user_id}

Parâmetro de rota esperado:
```
user_id: <Id do usuario>
```
Resposta esperada:
```
{
        "email": <Email do usuario {user_id}>,
        "name": <Nome do usuario {user_id}>,
        "id": {user_id},
        "items": []
}
```

#### Endpoint criar novos items

##### Método: POST
##### URL: http://localhost:8080/item/{user_id}/user

Parâmetro de rota esperado:
```
user_id: <Id do usuario>
```
Parâmetros do corpo esperado:
```
{
    "name": <Nome do item>,
    "description": <Descrição do item>,
    "link": <Link do item>,
    "user_have": <Booleano de status de obtenção do item>
}
```
Resposta esperada:
```
{
    "name": <Nome do item>,
    "description": <Descrição do item>,
    "link": <Link do item>,
    "user_have": <Booleano de status de obtenção do item>,
    "id": <Id do item>,
    "owner_id": <{user_id}>
}
```

#### Endpoint obter todos itens

##### Método: GET
##### URL: http://localhost:8080/items

Resposta esperada:
```
[
    {
        "name": <Nome do item 1>,
        "description": <Descrição do item 1>,
        "link": <Link do item 1>,
        "user_have": <Booleano de status de obtenção do item 1>,
        "id": <Id do item 1>,
        "owner_id": <Id do usuario 1>
    },
    {
        "name": <Nome do item 2>,
        "description": <Descrição do item 2>,
        "link": <Link do item 2>,
        "user_have": <Booleano de status de obtenção do item 2>,
        "id": <Id do item 2>,
        "owner_id": <Id do usuario 1>
    },
    ...
]
```

#### Endpoint obter item aleatório de um usuário

##### Método: GET
##### URL: http://localhost:8080/item/{user_id}/random

Parâmetro de rota esperado
```
user_id: <Id do usuario>
```
Resposta esperada:
```
{
    "name": <Nome do item aleatório>,
    "description": <Descrição do item> aleatório,
    "link": <Link do item aleatório>,
    "user_have": <Booleano de status de obtenção do item aleatório>,
    "id": <Id do item aleatório>,
    "owner_id": <{user_id}>
}
```
#### Endpoint atualizar a obtenção de um item

##### Método: PUT
##### URL: http://localhost:8080/item/{user_id}/got
Parâmetro de rota esperado
```
user_id: <Id do usuario>
```
Parâmetros do corpo esperado:
```
{
    "name": <Nome do item>,
    "user_have": <Booleano de status de obtenção do item>
}
```
Resposta esperada:
```
{
    "name": <Nome do item aleatório>,
    "description": <Descrição do item> aleatório,
    "link": <Link do item aleatório>,
    "user_have": <Booleano de status de obtenção do item aleatório>,
    "id": <Id do item aleatório>,
    "owner_id": <{user_id}>
}
```
