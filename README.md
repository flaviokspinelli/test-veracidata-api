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