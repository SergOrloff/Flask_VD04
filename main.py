from flask import Flask, render_template
from datetime import datetime
import random

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Главная страница, отображает текущее время и случайную цитату дня
@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Получаем текущее время
    quotes = [
        "Программирование — это как йога: чем глубже, тем больше ошибок.",
        "Компьютеры никогда не делают ошибки — они только производят случайные сбои.",
        "В программировании можно всё, кроме тех случаев, когда нельзя.",
        "Сначала код работает, потом не работает, потом работает снова — это и есть магия.",
        "Лучше один раз увидеть код, чем сто раз услышать об ошибке.",
        "Программисту легче исправить код, чем объяснить, как он работает.",
        "Кодить — это как строить дом из спичек: просто, но одна ошибка, и всё рушится.",
        "В коде есть две проблемы: имена переменных и кэширование.",
        "Программисты не делают ошибки, они просто создают баги.",
        "Хороший код как хорошее вино — с годами становится только лучше."
    ]
    # Случайно выбираем одну цитату из списка
    random_quote = random.choice(quotes)
    # Передаем время и цитату в шаблон
    return render_template('index.html', current_time=current_time, quote=random_quote)

# Страница блога, отображает статьи о Python
@app.route('/blog')
def blog():
    articles = [
        {
            "title": "Основы языка программирования Python",
            "content": "Python — это высокоуровневый язык программирования, который известен своей простотой и "
                       "легкостью в изучении. Он поддерживает множество парадигм программирования, "
                       "включая объектно-ориентированное, процедурное и функциональное программирование..."
        },
        {
            "title": "Работа с файлами в Python",
            "content": "Python предоставляет множество удобных методов для работы с файлами. Открытие, чтение, "
                       "запись и закрытие файлов — все это можно сделать с помощью встроенных функций языка..."
        },
        {
            "title": "Создание веб-приложений с Flask",
            "content": "Flask — это легковесный веб-фреймворк на Python, который используется для разработки "
                       "веб-приложений. Flask минималистичен, но расширяем, что делает его отличным выбором как для "
                       "небольших проектов, так и для масштабируемых приложений..."
        },
        {
            "title": "Обработка исключений в Python",
            "content": "Обработка исключений — это механизм, который помогает управлять ошибками в программном коде. "
                       "В Python используются конструкции try, except и finally для контроля за исключениями и "
                       "предотвращения падения программы..."
        },
        {
            "title": "Использование библиотек NumPy и Pandas",
            "content": "NumPy и Pandas — это мощные библиотеки Python, которые широко используются в научных "
                       "вычислениях и анализе данных. NumPy предоставляет поддержку многомерных массивов и "
                       "математических функций, тогда как Pandas предоставляет инструменты для работы с таблицами "
                       "данных..."
        }
    ]
    return render_template('blog.html', articles=articles)  # Передаем статьи в шаблон блога

# Страница контактов с формой обратной связи
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Запускаем приложение в режиме отладки
if __name__ == '__main__':
    app.run(debug=True)