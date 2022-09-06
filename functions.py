import datetime
import webbrowser     # работа с браузером

import pyttsx3     # преобразование текста в речь
import speech_recognition as speech_rec     # модули для распознавания речи
import pyaudio

#нечеткое сравнение строк
from fuzzywuzzy import fuzz

from googletrans import Translator     # переводчик

import transliterate     # транскрибирование с кириллицы на латиницу

# для парсинга
from bs4 import BeautifulSoup
import urllib.request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#словарь команд
dict = {
    "cmds": {
        'browser': ("открой браузер", "браузер", "включи браузер"),
        'time': ("сколько времени", "который час", "время", "сколько сейчас времени", "скажи время"),
        'date': ("какая сегодня дата", "какое сегодня число", "сегодняшняя дата", "назови дату"),
        'wiki': ("что такое", "что есть"),
        'trans': ("перевод", "переведи", "переведи фразу"),
        'weather': ("какая погода город", "погода город", "погода", "какая сейчас погода", "какая сейчас погода город"),
        'stop': ("стоп", "остановка", "остановись", "хватит")
    }
}


# определение индекса записывающего устройства   P.S. скорее всего, не понадобится
""" 
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
"""


window = None


def def_window(win):
    global window
    window = win


def write_text(text):
    window.ui.voiceRecText.insertPlainText(text + '\n')


# речь голосового помощника
def bot_talk(words):
    write_text(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


# функция прослушивания пользователя и вызова функций
def user_speech():
    r = speech_rec.Recognizer()
    while True:
        with speech_rec.Microphone() as source:
            write_text("Скажите что-нибудь:")
            #r.pause_threshold = 1     # пауза в 1 секунду
            r.adjust_for_ambient_noise(source, duration=1)     # удаление лишних шумов с фона 1 секунду
            voice = r.listen(source)     # прослушивание микрофона

        try:
            text_speech = r.recognize_google(voice, language="ru-RU").lower()    # перевод голоса в текст
            write_text("Вы сказали: " + text_speech)

            cmd = text_speech.strip()
            cmd = find_command(text_speech)
            cont = do_command(cmd['ncmd'], text_speech, cmd['num'])

            if not cont:
                break

        except speech_rec.UnknownValueError:
            bot_talk("Говорите чётче")

        except speech_rec.RequestError:
            bot_talk("Неизвестная ошибка. Проверьте подключение")


#та же фунуция, что и user_speech, но только для считывания речи
def speech():
    r = speech_rec.Recognizer()

    with speech_rec.Microphone() as source:
        write_text("Скажите что-нибудь:")
        # r.pause_threshold = 1     # пауза в 1 секунду
        r.adjust_for_ambient_noise(source, duration=1)  # удаление лишних шумов с фона 1 секунду
        voice = r.listen(source)  # прослушивание микрофона

    try:
        t_speech = r.recognize_google(voice, language="ru-RU").lower()  # перевод голоса в текст
        write_text("Вы сказали: " + t_speech)

    except speech_rec.UnknownValueError:
        bot_talk("Говорите чётче")
        t_speech = speech()

    except speech_rec.RequestError:
        bot_talk("Неизвестная ошибка. Проверьте подключение")
        t_speech = speech()

    return t_speech


#определение команды
def find_command(cmd):
    new_cmd = {'ncmd': '', 'num': 0}
    for i, j in dict['cmds'].items():
        for a in j:
            comp = fuzz.ratio(cmd, a)
            if comp > new_cmd['num']:
                new_cmd['ncmd'] = i
                new_cmd['num'] = comp

    return new_cmd


# команды
def do_command(cmd, text_speech, same):

    do_smth = 1

    if cmd == 'browser' and same >= 50:
        webbrowser.open('https://www.google.com/')
    elif cmd == 'time' and same >= 50:
        now = datetime.datetime.now()
        bot_talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == 'date' and same >= 50:
        now_date = datetime.date.today()
        bot_talk("Сейчас " + str(now_date))
    elif cmd == 'wiki' and same >= 50:     # поиск в википедии
        words = text_speech.split(' ')
        fragment1 = 'что'
        fragment2 = 'такое'
        fragment3 = 'есть'
        new_words = []
        for word in words:
            if fragment1 not in word and fragment2 not in word and fragment3 not in word:
                new_words.append(word)
        webbrowser.open_new_tab('https://ru.wikipedia.org/wiki/' + ' '.join(new_words))
    elif cmd == 'trans' and same >= 50:     #переводчик
        bot_talk("Скажите фразу для перевода")
        phrase = speech()
        do_translate(phrase)
    elif cmd == 'weather' and same >= 50:     #парсер инфы с сайта погоды
        get_html(text_speech)
    elif cmd == 'stop' and same >= 50:
        do_smth = 0
    else:
        bot_talk("Команда не распознана")

    return do_smth


# переводчик
def do_translate(phrase):
    bot_talk("На какой язык желаете перевести?")
    lang = speech()
    translator = Translator()
    result_lang = translator.translate(lang, src='russian', dest='english')
    lang = result_lang.text.lower()
    if lang == 'deutsch':
        lang = 'german'
    try:
        result = translator.translate(phrase, src='russian', dest=lang)
        bot_talk(result.text)
    except ValueError:
        bot_talk("Ошибка, назовите язык перевода")
        do_translate(phrase)


#адрес страницы для парсера
def get_html(text_speech):
    words = text_speech.split(' ')
    fragment1 = 'погода'
    fragment2 = 'какая'
    fragment3 = 'город'
    fragment4 = 'сейчас'
    new_words = []
    for word in words:
        if fragment1 not in word and fragment2 not in word and fragment3 not in word and fragment4 not in word:
            new_words.append(word)

    URL = 'https://yandex.by/pogoda/'
    translator = Translator()
    translated = translator.translate(' '.join(new_words), src='russian', dest='english')
    URL += translated.text.lower()

    try:
        response = urllib.request.urlopen(URL)
        do_parse(response.read())

    except urllib.error.HTTPError:
        bot_talk("Некорректная команда")
        user_speech()

    except AttributeError:
        bot_talk("Яндекс защищает свои данные. Молодцы суки!")
        user_speech()

    """
    except http.client.InvalidURL:
        bot_talk("Некорректная команда")
        user_speech()
    """


#парсер погоды
def do_parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    temp = "В данный момент там "
    temp += soup.find('div', class_='temp fact__temp fact__temp_size_s').get_text().encode('utf-8').decode('utf-8',
                                                                                                          'ignore')
    temp += ' ' + soup.find('div', class_='link__condition day-anchor i-bem').get_text().encode('utf-8').decode('utf-8',
                                                                                                          'ignore')
    bot_talk(temp)


# перевод аудио в текст из файла
def from_audio_to_text(file):
    sample_audio = speech_rec.AudioFile(file)     # OSR_us_000_0018_8k     Nikolai_Alekseyev_Helsinki_forum
    rec = speech_rec.Recognizer()
    with sample_audio as audio_file:
        rec.adjust_for_ambient_noise(audio_file, duration=1)
        audio_content = rec.record(audio_file, duration=20)     # duration это длительность прослушиваемого фрагмента

    text_file = rec.recognize_google(audio_content).lower()
    print(text_file)


#bot_talk("Здравствуй хозяин")
#user_speech()
#from_audio_to_text('C:/Users/olegd/Downloads/Nikolai_Alekseyev_Helsinki_forum.wav')
