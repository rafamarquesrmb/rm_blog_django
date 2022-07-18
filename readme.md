
  

![author](https://img.shields.io/badge/author-rafamarquesrmb-red.svg) ![Python](https://img.shields.io/badge/Python-3.10.4-blue.svg) ![Django](https://img.shields.io/badge/Django-4.0.5-blue.svg)

  
  

# RM Blog with Django

  

<sub>by [Rafael Marques @rafamarquesrmb](https://github.com/rafamarquesrmb)</sub>

  

## About

  
  

This project is a blog with integrated CMS, developed with Django Framework (4.0.5).

  

You can see a demo of this project at: [RM Blog (https://rafamarquesrmb-rm-blog.herokuapp.com/)](https://rafamarquesrmb-rm-blog.herokuapp.com/).

  


It consists of a Django MVT application with Posts, Categories and Tags.

It has an easy template to set up title and description meta tags for SEO.

Integrated with Highligh.js to include code in the post.

All application administration must be done through django admin. The django admin is properly configured with CKEditor, allowing for better writing and also the inclusion of attached files.

In addition, it is pre-configured for direct deployment to Heroku and using storage with Amazon S3. Static files are read directly from heroku.

However, the uploaded files are sent to a bucket on amazon S3.

It also has a contact page, with a contact form working perfectly.

I started the newsletter, but it's not finished. So far it only stores the contact in the database.

There are still some features to implement:
- Include a better way of dealing with newsletters (such as using an email marketing service)
- include comment system.
- Implement a better caching practice

  

## External services

It is possible to run 100% locally, and deploy on other servers and VPS. However, it is pre-adapted to run alongside **Heroku** Server and **Amazon S3 Storage**.
  

## Instructions
Initially, don't forget to make the necessary changes and settings in the .env file. You can find an example in "*.env.example*"
1. It should run initially

    python manage.py migrate

2. Then Create the superuser:

    python manage.py createsuperuser

3. Then it should run:

    python manage.py collectstatic

4. Finally, run the server:

    python manage.py runserver


<sub>by [Rafael Marques @rafamarquesrmb](https://github.com/rafamarquesrmb)</sub>