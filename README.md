# Desafio Técnico - API de Clientes

Este é um projeto backend desenvolvido com Django e Django REST Framework. Ele oferece uma API para gerenciamento de clientes, permitindo operações de criação, listagem, edição e exclusão.

## Tecnologias utilizadas

- Python 3.9
- Django 4.x
- Django REST Framework
- SQLite (padrão, mas pode ser alterado)
- Django CORS Headers

## Requisitos

- Python instalado 3.9
- `pip` para gerenciamento de pacotes
- Ambiente virtual (recomendado)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/flaviokspinelli/test-veracidata-api.git
   cd test-veracidata-api

2. **Instale as dependencias:**

   ```bash
   pip install -r requirements.txt

3. **Crie o banco de dados:**

   ```bash
   python manage.py migrate 

4. **Rode o projeto:**

   ```bash
   python manage.py runserver


## Endpoints

- Login
URL: http://localhost:8000/api/auth/login/
Method: POST
Body: {
    "username": "admin",
    "password": "admin"
}

- Listar clientes
URL: http://localhost:8000/api/customers/
Method: GET

- Criar clientes
URL: http://localhost:8000/api/customers/
Method: POST
Body: {
    "name": "Nome do Cliente",
    "email": "cliente@email.com",
    "phone": "(21) 99999-9999",
    "birthday": "1989-01-01"
}

- Atualizar cliente
URL: http://localhost:8000/api/customers/{id}/
Method: PUT
Body: {
    "name": "Novo Nome do Cliente",
    "email": "novocliente@email.com",
    "phone": "(21) 99999-9991",
    "birthday": "1989-01-02"
}

- Deletar cliente
URL: http://localhost:8000/api/customers/{id}/
Method: DELETE