# Бот для скарпинга сайта кинопоиск
## Функционал
- Вы можете запросить описание интересущего вас фильма. 
- В проекте присутствует логирование информации
- ```/start``` - узнать информацию о боте
- ```/help``` - узнать функционал
- ```/GetDescription [filmName]``` - сделать запрос
## Запуск проекта
```
python3 bot.py
```
## Описание архитектуры проекта
В файле requestHTML.py я обрабатываю запросы к странице kinopoisk.ru, используя библиотеки requests и BeautifulSoup. 
Описание работы бота лежит в отдельном файле bot.py, там я обрабатываю запросы пользователя. 
Также я сохраняю лог всех запросов

## Пример работы
![Иллюстрация к проекту](https://github.com/PeregudovSergey/kinopoiskObserver/blob/main/pic.jpg)
