# corseco_ps


# Table of Contents

- [Description](#description)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Usage](#usage)
- [Tests](#tests)

### description
A sample django application to demonstrate a simple case use of django rest-framework.
as the scenario goes, the application allow you to enter / get details of individual 
visitors to specific companies in a co-working space.

### dependencies

python == 2.7
#### required python packages
  - Django==1.10.4
  - djangorestframework==3.5.3
  - Pillow==3.4.2
  - pkg-resources==0.0.0


requirements.txt given in the repository mentions all pthon dependencies.
assuming you are inside a virtual environment, run following command in your terminal to install them.

```sh
pip install -r requirements.txt
```


## deployment
assuming that you are inside your virtual environment and have installed all before mentioned dependencies.
run the following commands in your terminal inside the project directory to migrate and sync database models.

```sh
python manage.py makemigrations
python manage.py migrate
```

after successful migration, run below command in your terminal to start the django development server
```sh
python manage.py runserver
```


## usage
assuming that the development server ran successfully without errors, hit following curl commands to test Visitor api end points

- for get request

```sh
curl http://<host>:<port>/api/peopleinfo/
```

- for post request
```sh
curl -F "name=test-name" -F "email=test@gmail.com" -F "phone=+91 XXXXXXXXXX" -F "whom_to_meet=test-name" -F "compane_name=test" \
-F "photo=@<local absolute path of your image>" http://<host>:<port>/api/peopleinfo/

```

## tests
the project has two unit tests, one for both get and post request api end point.
switch to your virtual environment with all the dependencies and inside your project directory,
run following commands in your terminal.

```sh
python manage.py test
```