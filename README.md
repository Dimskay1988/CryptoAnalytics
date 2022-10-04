# Crypto Analytics

The first thing to do is to clone the repository:
```sh
$ https://github.com/Dimskay1988/CryptoAnalytics.git
$ cd CryptoAnalytics
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.9.13 -m venv .venv
$ source .venv/bin/activate
```
```
Note the `(.venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.
Once `pip` has finished downloading the dependencies:
Create migrations:
```
```sh
python manage.py migrate
```
Create .env file in CryptoAnalytics root folder:
```sh
touch .env
```
```sh 

If .env by pycharm:
1. Install plugin: envfile plugin from jetbrains.com
2. In PyCharm: Edit Configurations -> Press '+' -> Find Django Server
3. Name it (like 'run django')
4. Enable Django support for the project (Press 'Fix') -> Mark 'Enable Django support'
5. Django project root: Add full path to project (it is called the same, as the main folder of your django project, but inside and contains 'settings.py'. This folder may be renamed in 'project'
6. Check if the pathes to Settings (settings.py) and Manage script (manage.py) are ok
7. Than just Apply -> Ok
8. Once again Apply -> Ok
9. Edit Configurations -> check if pathes in Environment variables in your 'run django' (or how you named it) are correct. If not (f.e. for settings), correct it (f.e. from DJANGO_SETTINGS_MODULE=settings to DJANGO_SETTINGS_MODULE=project.settings) 
10. Edit Configurations -> EnvFile -> Enable EnvFile
11. Press '+' -> Choose .env file -> Press icon with an eye to see hidden files -> find the path to .env file

In the end .env must be in the same folder with manage.py
Now you can import os in settings.py to substitute your secrets in the following way:
```
```sh
SECRET_KEY = config('SECRET_KEY')
```
```sh
DEBUG = config('DEBUG')
```
```sh
TOKEN = config('TOKEN')
```
Your secret key, token and debug should be in .env file like this:
```sh
DJANGO_SECRET=asddsad231jsfjp32ojrjpfjsdoivzoidvhoxicj 
```
```sh
DEBUG=True/False
```
```sh
TOKEN=5483495161:AaaF4AadsdfdaKJdkJ-D9xG_UdkKJSEZfd6c
```
```
Start scheduler it will update the database every minute the command:
```
```sh
python manage.py runapscheduler
```
```
Start the bot with the command:
```
```sh
python manage.py bot
```
```sh
(.venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

List of possible urls may be seen in urls.py in Crypto-analytics.
Have fun! :)
