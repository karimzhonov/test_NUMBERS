# test_NUMBERS
Тестовая задача в компании Numbers 

Результат ([Google Sheet](https://docs.google.com/spreadsheets/d/1_qARCaIOTcXhny9NXHHkdAm1-OFjlfDeZGrMoQFRuQM/edit#gid=1844212246)): 
[kht-test-numbers.herokuapp.com](https://kht-test-numbers.herokuapp.com/)

Админка (login=root, password=9009) [kht-test-numbers.herokuapp.com/admin](https://kht-test-numbers.herokuapp.com/admin)

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Django](https://img.shields.io/badge/-Django-0aad48?style=flat-square&logo=Django)
![Postgresql](https://img.shields.io/badge/-Postgresql-%232c3e50?style=flat-square&logo=Postgresql)
![Docker](https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/-Nginx-0aad48?style=flat-square&logo=nginx&logoColor=black)
![CELERY](https://img.shields.io/badge/-Celery-%232c3e50?style=flat-square&logo=celery&logoColor=green)
# Описание задачи

Необходимо разработать скрипт на языке Python 3, 

который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI/edit?usp=sharing) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:

1. a. Упаковка решения в docker контейнер
    
    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    
    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.
    

1. Решение на проверку передается в виде ссылки на проект на Github.
В описании необходимо указать ссылку на ваш Google Sheets документ (открыть права чтения и записи для пользователя sales@numbersss.com ), а также инструкцию по запуску разработанных скриптов.

# Проделанная работа

Запуск проекта

```docker-compose up --build```

После выполнения docker script сайт будет запущен 
тут: [http://localhost:1337](http://localhost:1337)

Проект разделен на 2 части. 
Первый веб сайт, который просто показывает данные, а второй планировшик задач, 
который обновляет базу данных каждый 5 секунд.

Планировшик задач содержить 2 задачи, первая задача - обновления данных:
- создан сервисный аккаунт и этот аккаунт используется для получения данных с Google drive.
- Полученные данные валидируются, потом проверяется 
изменились ли что-то в этой таблице относительно базой данных.
- Строка валидируется таким образом, что если все поля корректно запольнены, тогда 
валидатся объявляется успешним и рассчитывается цена в рублях с помощью полученних курсов вальют с ЦБР.

Тут в конечном результате я использовал библиотеку schedule, но из начальна планировалось сделать 
с помощью Celery (docker тоже был настроен для этого). Но было такое, что Celery планировал 
задачу, но не выполнял (ссылька на [commit](https://github.com/karimzhonov/test_NUMBERS/tree/011451c0593fb2adcfa50d6d0a74f2cbb18c219d)). 
Если вы скажете свое мнение по поводу этого, буду очень благодарен.  

Вторая задача - отправка сообщений (проверка каждый день в 9 утра) через Telegram bot о истичении сроки. 
Я тут не стал использовать какой-то api, думаю тут такой подход избыточен. 
По этому я делаю просто запрос на telegram api с помощью requests.

