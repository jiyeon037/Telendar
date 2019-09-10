# Telindar
멋쟁이 사자처럼 해커톤 테린더(테마캘린더)팀

![Alt text](./img/intro.png)


## 이슈


## 가상환경
~~~bash
python -m venv myvenv  
source myvenv/Scripts/activate  
python -m pip install --upgrade pip  
pip install django  
~~~


## DATABASE
* 데스크탑에 postgresql 설치 

* <a href="https://trello.com/c/X6BS8ms4/33-git-https-githubcom-jeongnaehyeok-telindar">trello</a> 참고하여 비밀번호 설정 (로컬 환경 통일 위함)

* pgAdmin4에서 각자 database create

* python manage.py createsuperuser


## 실행
~~~bash
pip install psycopg2
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

## 팀원

### [김다민](깃페이지)

### [김지연](https://github.com/jiyeon037)

### [성주용](https://github.com/jjudrgn)

### [정내혁](https://github.com/jeongnaehyeok)

## 참고

### [Calendar](https://github.com/huiwenhw/django-calendar)

~~~
