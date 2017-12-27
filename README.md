# dj-extend-user

Experiment Extend User in Django

## Objetivo

Explorar os recursos de [Extending the existing User model](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#extending-the-existing-user-model) e [How to Add User Profile To Django Admin](https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html).

## Como desenvolver?

* Clone o repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Execute as migrações no banco de dados.
* Crie um usuário
* Rode a aplicação

```
git clone https://github.com/rg3915/dj-extend-user.git
cd dj-extend-user
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

