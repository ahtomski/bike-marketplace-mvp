Bike Marketplace MVP
====================

A prototype for exploring trust and buying decisions in peer to peer marketplaces.

Screenshots
-----------

!["Home"](screenshots/home.png)

!["Results"](screenshots/results.png)

!["Detail 1"](screenshots/detail-1.png)

!["Detail 2"](screenshots/detail-2.png)

!["Contact Us"](screenshots/contact-us.png)

!["Contact Seller"](screenshots/contact-seller.png)

Made with
---------

- Django
- Pinax
- Vagrant
- Heroku
- Bootstrap
- Google Forms

--------------------------------------------------------------------------------

Developing locally
------------------

See http://docs.vagrantup.com/v2/getting-started/index.html for more information.

Boot up a local Virtual Machine using Vagrant.

```sh
(local machine) $ vagrant up
```

SSH into machine and install.

```sh
(local machine) $ vagrant ssh
(vagrant vm) $ virtualenv venv
(vagrant vm) $ source venv/bin/activate
(vagrant vm) $ pip install -r requirements.txt
```

Run server.

```sh
# Get IP address of VM.
(vagrant vm) $ ifconfig | grep 'inet addr'

# Configure database.

(vagrant vm) $ export DATABASE_URL='sqlite:////tmp/bike-marketplace-mvp.sqlite'

# Sync DB.
(vagrant vm) $ python manage.py syncdb

(vagrant vm) $ python manage.py runserver 0.0.0.0:8000
```

View in browser on host machine, e.g. at http://10.250.7.241:8000/.

Deploying to Heroku
-------------------

See https://devcenter.heroku.com/articles/getting-started-with-django for more information.

Test whether Procfile works.

```sh
$ foreman start
```

Create and configure a Heroku app, if one hasn't already been created.

```sh
# Create.
$ heroku create bike-marketplace-mvp

# Configure database.
heroku config:set DATABASE_URL={{production value here}}
```

Push code to Heroku remote to deploy.

```sh
$ git push heroku master
```

Sync the database.

```sh
$ heroku run python manage.py syncdb
```

View in browser.

```sh
$ heroku open
```

Resources
---------

http://docs.vagrantup.com/v2/getting-started/index.html

https://devcenter.heroku.com/articles/getting-started-with-django

http://jordanktakayama.wordpress.com/2013/02/20/lessons-learned-from-deploying-django-on-heroku/

http://www.deploydjango.com/django_project_structure/index.html

https://github.com/etianen/django-herokuapp

https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

http://blog.crowdint.com/2011/08/11/postgresql-in-vagrant.html

http://stackoverflow.com/questions/17036301/configuring-postgresql-database-for-local-development-in-django-while-using-hero

http://blog.smalleycreative.com/tutorials/setup-a-django-vm-with-vagrant-virtualbox-and-chef/

https://github.com/pinax/pinax-project-account

https://github.com/tjetzinger/django-pinax-skel/blob/master/docs/source/running-on-heroku.rst