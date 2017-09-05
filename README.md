A publication portal for Career Counselling developed during Microsoft code.fund.do 2017. It's aim is to **help people to read, write and learn from Career stories and experiences**.

### Requirements
* Python 2.7
* Django 1.8
* MySQL-Python [MySQLdb]
* MySQl Server

### Set up Database
* Restore Database from backup
```
mysql -u root -p < colog_dump.sql
```

* Make migration
```
Change directory to colog/ folder.
Run 
  python manage.py makemigrations app
  python manage.py migrate
```

### Run site
```
Run python manage.py runserver from colog/ folder.
Goto 127.0.0.1:8000 on browser.
```

### Site Functionality
* User can register on site.
* Once registered user can login and add posts for their academic experiences.
* User can read others experiences and like them and comment on them.