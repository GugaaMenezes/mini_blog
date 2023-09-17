# Mini Blog

#### Exercício teste, contendo o cadastro de artigos em um mini blog, com login e autenticação em rotas as requisições. 


### Backend 
- Python (3.11.3);
- Django (4.2.5)
- PyJWT(2.8.0);
### Frontend
- HTML
- Javascript
### Banco de Dados
- SQLite

### Dependências

- asgiref(3.7.2);
- djangorestframework(3.14.0);
- djangorestframework-simplejwt(5.3.0);
- pytz(2023.3.post1);
- sqlparse(0.4.4);
- tzdata(2023.3);
### Execução

1. Clone este repositório:

   ```
   git clone https://github.com/GugaaMenezes/mini_blog.git
   ```

2. Navegue até a pasta principal do projeto:

   ```
   cd mini_blog
   ```

2.1 Crie um ambiente virtual para testes (opcional):  
   ```
   python -m venv venv
   ```
2.2 Acesse o ambiente virtual:
   ```
   venv\Scripts\activate
   ```

3. Realize a instalação de todas as dependências, do arquivo **requirements.txt**:

   ```
   pip install -r requirements.txt
   ```

4. Navegue até subpasta **mini_blog** para executar a aplicação:

   ```
   cd mini_blog
   ```

5. Crie o banco de dados, juntamente com as tabelas pré-definidas:

   ```
   python manage.py migrate
   ```

5. Crie um novo usuário para ter acesso à aplicação (será criado com privilégios de superuser ):

   ```
   python manage.py createsuperuser
   ```

> *Será criado com privilégios de superuser*.


6. Execute o servidor:

   ```
   python manage.py runserver
   ```


> *O **Frontend** está configurado para ser executado no endereço http://127.0.0.1:8000*.


## Documentação da API

#### Retorna token de acesso 

```http
  POST /token/
```
| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. |
| `password` | `string` | **Obrigatório**|

Status 200 OK:

```
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTA2ODQzNiwiaWF0IjoxNjk0OTgyMDM2LCJqdGkiOiJkOWI2YWQ2MWYxNTk0ZjljOWE5MTRmNTJlNjgwOGJkYyIsInVzZXJfaWQiOjF9.7D_xq_5_wv965zGnIVn_zTOVjN2HuQWXHCY4h4LzKbE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0OTgyMzM2LCJpYXQiOjE2OTQ5ODIwMzYsImp0aSI6ImM1OWM0M2Y4N2QwYjQ5MzdiNjEzMWI4ODliMTE1NjY4IiwidXNlcl9pZCI6MX0.Fe6Qhe1haaR-npuDwO1EQfnVi_A0niBzmcR2E-BBPK0"
}
```

#### Retorna todos os artigos 
> **_Necessário ter gerado o token access._**

```http
  GET /api/articles/
```


#### Inclui novo artigo no Banco de dados via API
> **_Necessário ter gerado o token access._**

```http
  POST /api/articles/
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `title` | `string` | **Obrigatório**. |
| `subtitle` | `string` | **Obrigatório**|
| `type` | `int` | **Obrigatório** |
| `content` | `string` | **Obrigatório** |
| `status` | `int` | **Obrigatório** |
| `keyword_set` | `itensArray` | opcional |


#### Retorna todas as plaavras  chaves 
> **_Necessário ter gerado o token access._**

```http
  /api/keywords/
```

## Referência

 - [Descrição do teste](https://github.com/GugaaMenezes/mini_blog/blob/master/Exercício%20Desenvolvedor%20Backend%20-%20Python%20Django.pdf)
 - [Descrição de construção](https://github.com/GugaaMenezes/mini_blog/blob/master/Desafio%20Samplemed%20-%20Gustavo%20Menezes.pdf)
 - [Queries de construção do Banco de dados](https://github.com/GugaaMenezes/mini_blog/blob/master/mini_blog.sql)
 - [Descrição do Banco de Dados](https://github.com/GugaaMenezes/mini_blog/blob/master/Tabelas%20banco%20de%20dados.pdf)

## Autores

- Gustavo Menezes - [@gugaamenezes](https://github.com/GugaaMenezes) 


## Funcionalidades

- Login com autenticação JWT
- Cadastro de artigos com definição de palavras-chave
- APIs com validação JWT para consumo

