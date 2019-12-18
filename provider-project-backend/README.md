
# prodvider-project-backend

## Primeiros passos
Entre na pasta provider-project-backend

* cd backend    

Dentro do diretorio crie e ative a sua Venv

* python3 -m venv venv
* source venv/bin/activate

Instale as dependencias do projeto com o seguinte comando

* pip install -r requirements-dev.txt

Rodando o banco de dados

* create database dbsystemerp;
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* python manage.py startapp NOME_APP


* Pega as informações HTTP_AUTHORIZATION
* request.META['HTTP_AUTHORIZATION']