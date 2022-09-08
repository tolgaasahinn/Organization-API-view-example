# Organization-API-view-example
Organization API view example
# Introduction

The goal of this project is to provide  django organization api  project  that everyone can use, which _just works_ out of the box and has the basic setup you can expand on. 


### Main features

* Basic organization create put update delete methods 

* custom user model can create a organization can see other organizaiton

* User registration and logging in 

* User and organizations data from json

* You can create your fake data as many as you want

* Docker-compose 

# Usage

To start to project:
bellow code it will create a container on your desktop then start to server

    $   docker-compose -f
    $   docker-compose.yml up
    
When you start your server on docker container it is going to lcreate a directory named code  then workdir will be code then coppy all files to code directory then dependencies will load from requirements.txt file after that your sever will be starts on 127.0.0.1:8000 port


To load data from fixtures:
    $   python manage.py loaddata user_data.json
    $   python manage.py loaddata organization_data.json


İf you want to add more  data to your database you need to 
open shell_plus on your terminal then you need to import fake_DAta.py from scripts file then 

    $ python manage.py shell_plus
    $ from scripts.fakedata import set_user_and_organization
    $for i in range(1,10):
        $ set_user_and_organization()
it will set 10 user and organization members to your database


{% endif %}
