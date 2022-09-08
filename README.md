# Проект автоматизации веб-приложения "Duolingo"

![logo1](https://cdn.otus.ru/media/public/c0/65/c065ae1eba3b4278849438384aab23a2.png)

*NOTE:*
Необходимо создать папку **.env** в корне и указать переменные LOGIN1, LOGIN2 и PASSWORD - где LOGIN1 логин нового 
зарегистрированного пользователя, а LOGIN2 старого пользователя (прошедшего как минимум вступительный урок), 
в переменную PASSWORD указать пароль от логина (создать при необходимости PASSWORD2 если пароли отличаются от УЗ),
например:

*LOGIN1=testemail@gmail.com1*

*LOGIN2=testemail@gmail.com2*

*PASSWORD=123456*

**Для запуска через selenoid ввести команды:**
- Запуск Selenoid - **./cm selenoid start** из директории где лежит Selenoid
- Запуск Selenoid-UI - **./cm selenoid-ui start** из директории где лежит Selenoid

**Для запуска в контейнере использовать команду:**
- sudo docker run --name tests_run --network selenoid tests; docker cp tests_run:/app/allure-results . && docker cp 
tests_run:/app/logs . && ~/Downloads/allure/bin/allure generate --clean

**Для запуска из Pycharm использовать команду:**
- pytest --executor local --browser chrome -n 1

*параметр* **--executor local** *устанавливает как тесты будут запущены,* **local** *на локальном окружении, без 
этого параметра или с указанием* **--executor 192.168.1.70** *тесты будут запущены в selenoid*

*параметр* **--browser chrome** *указывает на каком браузере будут запущены тесты ('chrome', 'firefox', 'opera')*

*параметр* **-n 1** *позволяет указать количество потоков для запуска тестов ('auto','1','2' и тд. в зависимости от
производительности процессора)* 

*23.08.2022*