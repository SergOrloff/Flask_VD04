# Проект Flask: Веб-сайт компании "Спектр"

## Описание

Этот проект представляет собой простой веб-сайт компании "Спектр", созданный с использованием фреймворка Flask. Веб-сайт состоит из трех страниц:

- Главная страница (`index.html`) - содержит информацию о компании.
- Страница сотрудников (`blog.html`) - информация о сотрудниках компании.
- Страница контактов (`contacts.html`) - контактная информация компании.

## Структура проекта

```
my_flask_app/
├── static/
├── templates/
│   ├── index.html
│   ├── blog.html
│   └── contacts.html
├── app.py
└── requirements.txt
```

## Установка

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше).

2. Склонируйте репозиторий проекта или загрузите его архивом.

3. Перейдите в папку проекта и создайте виртуальное окружение:

   ```bash
   python -m venv venv
   ```

4. Активируйте виртуальное окружение:

   - Для Windows:
     ```bash
     venv\Scripts\activate
     ```

   - Для macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Запуск проекта

1. Убедитесь, что виртуальное окружение активировано.

2. Запустите приложение Flask:

   ```bash
   python app.py
   ```

3. Откройте веб-браузер и перейдите по адресу: [http://localhost:5000](http://localhost:5000) для просмотра главной страницы.

## Страницы веб-сайта

- **Главная страница** (`/`): На главной странице размещена информация о компании "Спектр", её продукции и территории поставок.
  
- **Страница сотрудников** (`/person/`): Здесь будет размещена информация о сотрудниках компании (в текущей версии это заглушка).

- **Страница контактов** (`/contacts/`): Содержит контактную информацию компании (в текущей версии это заглушка).

## Используемые технологии

- Flask - микро-фреймворк для создания веб-приложений на Python.
- HTML и CSS - для разработки пользовательского интерфейса.
- Bootstrap - для стилизации и адаптивности страниц.

## Замечания

- Убедитесь, что у вас есть доступ к интернету для загрузки стилей Bootstrap из CDN.
- Это базовый пример использования Flask и может быть расширен и усовершенствован.

## Авторы

Данный проект создан с целью обучения и демонстрации возможностей фреймворка Flask.
