import speech_recognition as sr
import os
import sys
import webbrowser
from gtts import gTTS
import time

from time import sleep

def talk(words):
    print(words) # Дополнительно выводим на экран
    os.system("say " + words) # Проговариваем слова
    

talk("Привет, чем я могу помочь вам?")
mytext = "Привет, чем я могу помочь вам?"
audio = gTTS(text=mytext, lang='ru', slow=False)
audio.save('example.mp3')
os.system('start example.mp3')
sleep(2)

# speech.say("Привет, чем я могу помочь вам?")
def command():
    # Создаем объект на основе библиотеки
    # speech_recognition и вызываем метод для определения данных
    r = sr.Recognizer()
    # Начинаем прослушивать микрофон и записываем данные в source
    with sr.Microphone() as source:
        
        # Просто вывод, чтобы мы знали когда говорить
        print("Говорите")
        sleep(1)
        mytext = 'говорите'
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        # Устанавливаем паузу, чтобы прослушивание
        # началось лишь по прошествию 1 секунды
        # r.pause_threshold = 5
        # используем adjust_for_ambient_noise для удаления
        # посторонних шумов из аудио дорожки
        r.adjust_for_ambient_noise(source, duration=1)
        # Полученные данные записываем в переменную audio
        # пока мы получили лишь mp3 звук
        audio = r.listen(source)
    try: # Обрабатываем все при помощи исключений
        """
        Распознаем данные из mp3 дорожки.
        Указываем что отслеживаемый язык русский.
        Благодаря lower() приводим все в нижний регистр.
        Теперь мы получили данные в формате строки,
        которые спокойно можем проверить в условиях
        """
        
        zadanie = r.recognize_google(audio, language="ru-RU",).lower()
        # Просто отображаем текст что сказал пользователь
        print("Вы сказали: " + zadanie)
        mytext = 'Вы сказали'+ zadanie
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        sleep(2)
    # Если не смогли распознать текст, то будет вызвана эта ошибка
    except sr.UnknownValueError:
        # Здесь просто проговариваем слова "Я вас не поняла"
        # и вызываем снова функцию command() для
        # получения текста от пользователя
        talk("Я вас не поняла")
        mytext = 'Я вас не поняла'
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        zadanie = command()
        sleep(2)
        # В конце функции возвращаем текст задания
        # или же повторный вызов функции
    return zadanie
    # Данная функция служит для проверки текста,
    # что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
    # Попросту проверяем текст на соответствие
    # Если в тексте что сказал пользователь есть слова
    # "открыть сайт", то выполняем команду
    if 'открыть сайт' in zadanie:
        # Проговариваем текст
        talk("Уже открываю")
        mytext = 'Уже открываю'
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        
        # Указываем сайт для открытия
        url = 'https://itproger.com'
        # Открываем сайт
        webbrowser.open(url)
        sleep(2)
        # если было сказано "стоп", то останавливаем прогу
    elif 'стоп' in zadanie:
        # Проговариваем текст
        talk("Да, конечно, без проблем")
        mytext = 'Да, конечно, без проблем'
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        sleep(2)
        # Выходим из программы
        sys.exit()
        
        # Аналогично
    elif 'имя' in zadanie:
        talk("Меня зовут Сири")
        mytext = 'Меня зовут Сири'
        audio = gTTS(text=mytext, lang='ru', slow=False)
        audio.save('example.mp3')
        os.system('start example.mp3')
        sleep(2)
        # Вызов функции для проверки текста будет
        # осуществляться постоянно, поэтому здесь
        # прописан бесконечный цикл while
    elif 'youtube' in zadanie:
        url = 'https://www.youtube.com/watch?v=HKznjE9w4a0&ab_channel=BlendMusic'
        webbrowser.open(url)
while True:
    makeSomething(command())
