# работа с системой
import os
import sys

import datetime
import webbrowser     # работа с браузером

import pyttsx3     # преобразование текста в речь
import speech_recognition as speech_rec     # модули для распознавания речи
import pyaudio     # считывать речь с микрофона

from googletrans import Translator     # переводчик

import transliterate     # транскрибирование с кириллицы на латиницу

# для парсинга
from bs4 import BeautifulSoup
import urllib.request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# определение индекса записывающего устройства   P.S. скорее всего, не понадобится
""" 
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
"""


# речь голосового помощника
def bot_talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


# функция прослушивания пользователя
def user_speech():
    r = speech_rec.Recognizer()
    with speech_rec.Microphone() as source:
        print("Скажите что-нибудь:")
        #r.pause_threshold = 1     # пауза в 1 секунду
        r.adjust_for_ambient_noise(source, duration=1)     # удаление лишних шумов с фона 1 секунду
        voice = r.listen(source)     # прослушивание микрофона

    try:
        text_speech = r.recognize_google(voice, language="ru-RU").lower()    # перевод голоса в текст
        print("Вы сказали: " + text_speech)
    except speech_rec.UnknownValueError:
        bot_talk("Говорите чётче")
        text_speech = user_speech()
    except speech_rec.RequestError:
        bot_talk("Неизвестная ошибка. Проверьте подключение")
        text_speech = user_speech()
    return text_speech


# команды
def do_command():
    while True:
        text_speech = user_speech()
        if "открой браузер" in text_speech:
            webbrowser.open('https://www.google.com/')
        elif "время" in text_speech:
            now = datetime.datetime.now()
            bot_talk("Сейчас " + str(now.hour) + ":" + str(now.minute))
        elif "что такое" in text_speech:     # поиск в википедии
            words = text_speech.split(' ')
            fragment1 = 'что'
            fragment2 = 'такое'
            new_words = []
            for word in words:
                if fragment1 not in word and fragment2 not in word:
                    new_words.append(word)
            webbrowser.open_new_tab('https://ru.wikipedia.org/wiki/' + ' '.join(new_words))
        elif "переводчик" in text_speech:
            do_translate()
        elif "погода" in text_speech:
            html = get_html(text_speech)
            do_parse(html)
        elif "стоп" in text_speech:
            break


# переводчик
def do_translate():
    bot_talk("Скажите фразу для перевода")
    phrase = user_speech()
    bot_talk("На какой язык желаете перевести?")
    lang = user_speech()
    translator = Translator()
    result_lang = translator.translate(lang, src='russian', dest='english')
    lang = result_lang.text
    result = translator.translate(phrase, src='russian', dest=lang)
    bot_talk(result.text)


#адрес страницы для парсера
def get_html(text_speech):
    words = text_speech.split(' ')
    fragment = 'погода'
    new_words = []
    for word in words:
        if fragment not in word:
            new_words.append(word)

    URL = 'https://yandex.by/pogoda/'
    translator = Translator()
    translated = translator.translate(' '.join(new_words), src='russian', dest='english')
    URL += translated.text
    response = urllib.request.urlopen(URL)

    return response.read()


#парсер погоды
def do_parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', class_='temp fact__temp fact__temp_size_s').get_text().encode('utf-8').decode('utf-8',
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
do_command()
#from_audio_to_text('C:/Users/olegd/Downloads/Nikolai_Alekseyev_Helsinki_forum.wav')