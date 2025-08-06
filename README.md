# Домашнее задание к занятию "`Платформа мониторинга Sentry`" - `Татаринцев Алексей`




---

### Задание 1



1. `Описание к 1 заданию`

```
Так как Self-Hosted Sentry довольно требовательная к ресурсам система, мы будем использовать Free Сloud account.

Free Cloud account имеет ограничения:
- 5 000 errors;
- 10 000 transactions;
- 1 GB attachments.

Для подключения Free Cloud account:
- зайдите на sentry.io;
- нажмите «Try for free»;
- используйте авторизацию через ваш GitHub-аккаунт;
```
![1](https://github.com/Foxbeerxxx/sentry/blob/main/img/img1.png)

2. `Добавляю новый проект , создаю файлик для генерации ошибки и проверяю`
```
Делаю файл sentry_test.py
с наполнением:

import sentry_sdk

sentry_sdk.init(
    dsn="https://57bcf494b3e17c6ca2d43da38a9ca2e1@o4509798640386048.ingest.de.sentry.io/4509798785220688",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

# Вот ошибка, которая создаст событие:
division_by_zero = 1 / 0

Затем ставлю виртуальную среду и запускаю файл.

alexey@dellalexey:~/dz/sentry$ python3 -m venv venv
alexey@dellalexey:~/dz/sentry$ source venv/bin/activate
(venv) alexey@dellalexey:~/dz/sentry$ pip install sentry-sdk
Collecting sentry-sdk
  Downloading sentry_sdk-2.34.1-py2.py3-none-any.whl.metadata (10 kB)
Collecting urllib3>=1.26.11 (from sentry-sdk)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi (from sentry-sdk)
  Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Downloading sentry_sdk-2.34.1-py2.py3-none-any.whl (357 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 357.7/357.7 kB 22.1 kB/s eta 0:00:00
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 161.2/161.2 kB 24.9 kB/s eta 0:00:00
Installing collected packages: urllib3, certifi, sentry-sdk
Successfully installed certifi-2025.8.3 sentry-sdk-2.34.1 urllib3-2.5.0
(venv) alexey@dellalexey:~/dz/sentry$ python sentry_test.py
Traceback (most recent call last):
  File "/home/alexey/dz/sentry/sentry_test.py", line 11, in <module>
    division_by_zero = 1 / 0
                       ~~^~~
ZeroDivisionError: division by zero
Sentry is attempting to send 2 pending events
Waiting up to 2 seconds
Press Ctrl-C to quit

```
![2](https://github.com/Foxbeerxxx/sentry/blob/main/img/img2.png)

![3](https://github.com/Foxbeerxxx/sentry/blob/main/img/img3.png)

![4](https://github.com/Foxbeerxxx/sentry/blob/main/img/img4.png)





3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
`


---

### Задание 2

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота 2](ссылка на скриншот 2)`


---

### Задание 3

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота](ссылка на скриншот)`

### Задание 4

`Приведите ответ в свободной форме........`

1. `Заполните здесь этапы выполнения, если требуется ....`
2. `Заполните здесь этапы выполнения, если требуется ....`
3. `Заполните здесь этапы выполнения, если требуется ....`
4. `Заполните здесь этапы выполнения, если требуется ....`
5. `Заполните здесь этапы выполнения, если требуется ....`
6. 

```
Поле для вставки кода...
....
....
....
....
```

`При необходимости прикрепитe сюда скриншоты
![Название скриншота](ссылка на скриншот)`
