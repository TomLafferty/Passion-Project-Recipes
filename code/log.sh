
# commands for djangox demo

git clone https://github.com/xt0fer/d22-django-templ.git

python3 -m venv djxenv
source djxenv/bin/activate
# edit .gitignore to exclude the venv

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver

# in the vscode terminal

source djxenv/bin/activate

python manage.py startapp blog
# edit settings.py


# for the templates.

{% extends "_base.html" %}
{% load static %}

{% block content %}
