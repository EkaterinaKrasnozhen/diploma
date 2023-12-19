# Приложение является дипломным проектом автора.
## Оно позволяет вести базу данных клиентов турагентства.

### Для установки на локальном компьетере Windows необходимо:

- создать папку проекта:   
 mkdir  project

- перейти в папку:  
 cd  project

- создать локальный репозиторий git:  
 git init

- создать виртуальное окружение под новый проект Django:  
python -m venv .venv

- активировать вирутальное окружение:  
 venv\Scripts\activate

 - клонировать проект с github:  
 git clone https://github.com/EkaterinaKrasnozhen/diploma.git
 
 - установить необходимые компоненты:  
 pip install requirements.txt

 - выполнить миграции:  
 python manage.py makemigrations  
 python manage.py migrate

 - запустить приложение:  
 python manage.py runserver

 - перейти по ссылке localhost