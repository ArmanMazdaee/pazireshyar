## Requirements

you can install postgresql dependencies via this command:

```bash
sudo apt-get install libpq-dev
```

for setting up postgresql :

```
sudo su - postgres # login to postgres user
psql # enter postgres shell

#run following commands line by line

CREATE DATABASE pazireshyar;
CREATE USER django WITH PASSWORD 'django';
GRANT ALL PRIVILEGES ON DATABASE pazireshyar TO django ;

\q  #exit postgres shel
```
now go to pazireshayer directory and run
```
python manage.py migrate
python manage.py runserver
```
open 127.0.0.1:8000 and user pazireshyar 
