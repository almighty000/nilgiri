## Nilgiri: Eucalyptus Management Tool

Nilgiri is an open-source AWS webconsole with the ability to manage compute, network, and storage resources in an AWS-compatible cloud, and create (and use) one-click installs for commonly hosted web applications. It is based on Django and Boto and designed to work with Eucalyptus.

<img src="http://mdshaonimran.github.com/images/nilgiri.png" width=400>

### Eucalyptus 3.1 Compatible

### Description

Demo: http://www.youtube.com/watch?v=E-lfEkBFxwg


### Getting Started


1. Install virtualenv

2. Install boto

3. Install Django

4. Install MySQL-python

5. Create a database "nilgiri"

7. Run syncdb:
    
    $ python manage.py syncdb

6. Run the server with:

    $ python manage.py runserver

7. Create an user (not the admin user)

8. Register, login and edit credentials
