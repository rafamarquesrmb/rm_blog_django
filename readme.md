
![author](https://img.shields.io/badge/author-rafamarquesrmb-red.svg) ![Python](https://img.shields.io/badge/Python-3.10.4-blue.svg) ![Django](https://img.shields.io/badge/Django-4.0.5-blue.svg)     


# RM Blog with Django

<sub>by [Rafael Marques @rafamarquesrmb](https://github.com/rafamarquesrmb)</sub>

## About


This project is a blog with integrated CMS, developed with Django Framework (4.0.5).

You can see a demo of this project at: [RM Blog (https://rafamarquesrmb-rm-blog.herokuapp.com/)](https://rafamarquesrmb-rm-blog.herokuapp.com/).

It consists of an MVT application with Posts, Categories and Tags.

It has an easy template to configure title and description meta tags for SEO.

Integrated with Highligh.js to include code in the post.

All app administration must be done through django admin. The django admin is properly configured with CKEditor, allowing better writing and also the inclusion of attached files.

It has a contact page!

<sub>by [Rafael Marques @rafamarquesrmb](https://github.com/rafamarquesrmb)</sub>

## Instructions
1. It should run initially
    python manage.py migrate
    
2. Then Create the superuser:
    python manage.py createsuperuser
3. Then it should run:
    python manage.py collectstatic 

4. Finally, run the server:
    python manage.py runserver