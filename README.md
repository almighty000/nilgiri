## Nilgiri: Eucalyptus Management Tool

Nilgiri is an open-source AWS webconsole with the ability to manage compute, network, and storage resources in an AWS-compatible cloud, and create (and use) one-click installs for commonly hosted web applications. It is based on Django and Boto and designed to work with Eucalyptus.

<img src="http://mdshaonimran.github.com/images/nilgiri.png" width=400>

### Description

Demo: http://www.youtube.com/watch?v=E-lfEkBFxwg


### Getting Started


1. Install virtualenv

2. Install boto 2.3.0

3. Install Django>=1.3.1 (django==1.4 recommended)

4. Add ACCESS_KEY, SECRET_KEY and ENDPOINT to nilgiri/dashboard/nilgiri/commands/nilgiricommand.py

Run the server with:

    $ python manage.py runserver
