# coding=utf-8
from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine
import re
import time
receiver = Receiver(host="localhost", port=1338)
sender = Sender(host="localhost", port=1338)
bot_username = 'WastelandWarsBot'
bot_username1 = 'WastelandWarsHelperBot'
bot_username2 = 'YTranslateBot'
import random


# Стартовать бота для корректного счетчика хилок уже с полным закупом!!
medpack = 3
medx1 = 2
buffout = 2
#/
on = 1

# ⛑Аптечка
# 💌 Медпак
# 💉 Мед-Х
# 💊 Баффаут
# 👣Пустошь
# ⚔️Дать отпор
# 👣Идти дальше
# ⛺️Лагерь
# 📟Пип-бой
# ⛺️Вернуться
# 🏘В Нью-Рино

@coroutine
def work_with_message(receiver):
    global bot_user_id
    while True:
        msg = (yield)
        try:
            print('Получили сообщение от бота. Проверяем условия')
            if msg['event'] == 'message' and 'text' in msg and msg['peer'] is not None:
                if 'username' in msg['sender']:
                    parse_text(msg['text'], msg['sender']['username'], msg['id'])
        except Exception as err:
            if apikey is not None:
                ifttt("bot_error", "coroutine", err)
            print('Ошибка coroutine: {0}'.format(err))

def parse_text(text, username, message_id):
    global medpack
    global medx1
    global buffout
    global on
    if username == bot_username2:
      # включение и выключени бота по команде Включить ВЫКЛючить
        if text.find('off') != -1:
            on = 0
            print('ВЫКЛ')
        elif text.find('include') != -1:
            on = 1
            print('ВКЛ')
            dalnost = '44км от лагеря'

        elif text.find('10km') != -1:
            on = 2
            print('10km')
            dalnost = '10км от лагеря'
            distancia = 'Расстояние: 10'
        elif text.find('12km') != -1:
            on = 2
            print('12km')
            dalnost = '12км от лагеря'
            distancia = 'Расстояние: 12'
        elif text.find('15km') != -1:
            on = 2
            print('15km')
            dalnost = '15км от лагеря'
            distancia = 'Расстояние: 15'
        elif text.find('19km') != -1:
            on = 2
            print('19km')
            dalnost = '19км от лагеря'
            distancia = 'Расстояние: 19'
        elif text.find('22km') != -1:
            on = 2
            print('22km')
            dalnost = '22км от лагеря'
            distancia = 'Расстояние: 22'
        elif text.find('29km') != -1:
            on = 2
            print('29km')
            dalnost = '29км от лагеря'
            distancia = 'Расстояние: 29'
        elif text.find('36km') != -1:
            on = 2
            print('36km')
            dalnost = '36км от лагеря'
            distancia = 'Расстояние: 36'

            #/

    if username == bot_username:
              # подхавка, если проебано сообщение о голоде и голод уже 100%
        if on == 1:
            if text.find('100%') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/myfood')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_101')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_103')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_108')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_114')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_114')
                    #/
       
        # счетчик хилок
            if text.find('+60') != -1:
                medpack = medpack - 1
            if text.find('+30') != - 1:
                medx1 = medx1 - 1
            if text.find('+17') != - 1:
                buffout = buffout - 1
                    #/
                    # Нью-рино закупка хилок и го
            if text.find('Самый большой маленький городок в мире') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '👓Инженер')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '⛑Аптечка')
                time.sleep(random.randint(6, 15))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(6, 15))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(6, 15))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(6, 15))
                if medx1 < 2:
                    send_msg('@', bot_username, '💉 Мед-Х')
                    time.sleep(random.randint(6, 15))
                if medx1 < 2:
                    send_msg('@', bot_username, '💉 Мед-Х')
                    time.sleep(random.randint(6, 15))
                if buffout < 2:
                    send_msg('@', bot_username, '💊 Баффаут')
                    time.sleep(random.randint(6, 15))
                if buffout < 2:
                    send_msg('@', bot_username, '💊 Баффаут')
                medpack = 3
                medx1 = 2
                buffout = 2
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '👣Пустошь')
                    #/
                    # хил по сообщению о голоде
            elif text.find('Ты очень голоден') != -1:
                time.sleep(2)
                send_msg('@', bot_username, '/myfood')
                time.sleep(3)
                send_msg('@', bot_username, '/use_101')
                time.sleep(2)
                send_msg('@', bot_username, '/use_107')
                time.sleep(3)
                send_msg('@', bot_username, '/use_114')
                time.sleep(1)
                send_msg('@', bot_username, '/use_114')
                    #/
                    # Отаке
            elif text.find('на тебя напал') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '⚔️Дать отпор')
                    #/
                    # Точка поворота в лагерь + хил в лагере + уход в Нью-Рино
            elif text.find('44км от лагеря') != -1 or text.find('Расстояние: 44') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '⛺️Вернуться')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '🛠Верстак')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '⛑Аптечка')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '💉++ Суперстим')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '🏘В Нью-Рино')
                    #/
                    # Точки с которых начинаются попытки хила
            elif text.find('41км от лагеря') != -1 or text.find('Расстояние: 35') != -1:
                time.sleep(random.randint(6, 15))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(6, 15))
                        if medpack > 0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(6, 15))
                    else:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(6, 15))
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '👣Идти дальше')
            elif text.find('42км от лагеря') != -1 or text.find('Расстояние: 36') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/medpack')
                time.sleep(random.randint(6, 15))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(6, 15))
                        if medpack >0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(6, 15))
                    elif medx1 > 0:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(6, 15))
                        if medx1 > 0:
                            send_msg('@', bot_username, '/medx1')
                            time.sleep(random.randint(6, 15))
                    else:
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(6, 15))
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '👣Идти дальше')
            elif text.find('43км от лагеря') != -1 or text.find('Расстояние: 37') != -1:
                time.sleep(random.randint(6, 15))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(6, 15))
                        if medpack >0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(6, 15))
                    elif medx1 > 0:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(6, 15))
                        if medx1 > 0:
                            send_msg('@', bot_username, '/medx1')
                            time.sleep(random.randint(6, 15))
                    elif buffout > 0:
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(6, 15))
                        if buffout > 0:
                            send_msg('@', bot_username, '/buffout')
                            time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '👣Идти дальше')
                        #/
                        # Идти дальше
            elif text.find('км от лагеря') != -1 or text.find('Расстояние:') != -1:
                time.sleep(random.randint(5, 13))
                send_msg('@', bot_username, '👣Идти дальше')
                        #/

        if on == 2:
              # подхавка, если проебано сообщение о голоде и голод уже 100%
            if text.find('100%') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/myfood')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_101')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_103')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_108')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_114')
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '/use_114')
                    #/
                    # хил по сообщению о голоде
            elif text.find('Ты очень голоден') != -1:
                time.sleep(2)
                send_msg('@', bot_username, '/myfood')
                time.sleep(3)
                send_msg('@', bot_username, '/use_101')
                time.sleep(2)
                send_msg('@', bot_username, '/use_107')
                time.sleep(3)
                send_msg('@', bot_username, '/use_114')
                time.sleep(1)
                send_msg('@', bot_username, '/use_114')
                    #/
                    # Отаке
            elif text.find('на тебя напал') != -1:
                time.sleep(random.randint(6, 15))
                send_msg('@', bot_username, '⚔️Дать отпор')
                    #/
            elif text.find(dalnost) != -1 or text.find(distancia) != -1:
                on = 0
            elif text.find('км от лагеря') != -1 or text.find('Расстояние:') != -1:
                time.sleep(random.randint(5, 10))
                send_msg('@', bot_username, '👣Идти дальше')


def send_msg(pref, to, message):
    sender.send_msg(pref + to, message)


receiver.start()  # start the Connector.
receiver.message(work_with_message(receiver))
receiver.stop()


