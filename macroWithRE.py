from pytg.sender import Sender
from pytg.receiver import Receiver
from pytg.utils import coroutine
import re
import time
receiver = Receiver(host="localhost", port=1338)
sender = Sender(host="localhost", port=1338)
bot_username = 'WastelandWarsBot'
bot_username1 = 'WastelandWarsHelperBot'
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
    if username ==  bot_username1:
      # включение и выключени бота по команде Команды при лагах
        if text.find('использовать эти команды') != -1 and on == 1:
            on = 0
            print('ВЫКЛ')
        elif text.find('использовать эти команды') != -1 and on == 0:
            on = 1
            print('ВКЛ')
            #/

    if username == bot_username:
              # подхавка, если проебано сообщение о голоде и голод уже 100%
        if on == 1:
            if text.find('100%') != -1:
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/myfood')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/use_101')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/use_107')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/use_114')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/use_114')
                    #/
         # Logika ispolzovania aptechek i prochej huetoti
        if on == 1:
           Life = re.search(\d{3}\/)
           MaxLife = re.search(\/\d{3})
# Находим переменные вида 123/ и /123
           Life = Life[0:(len(Life)-1)]
           MaxLife = Life[0:(len(MaxLife)-1)]  # MISTAKE KOSTYA ALO BLIAD
# Организуем из них числа
            while Maxlife - Life > 60
                if medpack > 0:
                send_msg('@', bot_username, '/medpack')
            while 59 > Maxlife - Life > 30
                if medx1 > 0:
                   send_msg('@', bot_username, '/medx1')
                   time.sleep(random.randint(2, 7))
            while 29 > Maxlife - Life > 17
                if buffout > 0:
                   send_msg('@', bot_username, '/buffout')
                   time.sleep(random.randint(2, 7))
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
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '👓Инженер')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '⛑Аптечка')
                time.sleep(random.randint(2, 7))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(2, 7))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(2, 7))
                if medpack < 3:
                    send_msg('@', bot_username, '💌 Медпак')
                    time.sleep(random.randint(2, 7))
                if medx1 < 2:
                    send_msg('@', bot_username, '💉 Мед-Х')
                    time.sleep(random.randint(2, 7))
                if medx1 < 2:
                    send_msg('@', bot_username, '💉 Мед-Х')
                    time.sleep(random.randint(2, 7))
                if buffout < 2:
                    send_msg('@', bot_username, '💊 Баффаут')
                    time.sleep(random.randint(2, 7))
                if buffout < 2:
                    send_msg('@', bot_username, '💊 Баффаут')
                medpack = 3
                medx1 = 2
                buffout = 2
                time.sleep(random.randint(2, 7))
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
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '⚔️Дать отпор')
                    #/
                    # Точка поворота в лагерь + хил в лагере + уход в Нью-Рино
            elif text.find('42км от лагеря') != -1 or text.find('Расстояние: 38') != -1:
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '⛺️Вернуться')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '🛠Верстак')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '⛑Аптечка')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '💉++ Суперстим')
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '🏘В Нью-Рино')
                    #/
                    # Точки с которых начинаются попытки хила
            elif text.find('39км от лагеря') != -1 or text.find('Расстояние: 35') != -1:
                time.sleep(random.randint(2, 7))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(2, 7))
                        if medpack > 0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(2, 7))
                    else:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(2, 7))
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '👣Идти дальше')
            elif text.find('40км от лагеря') != -1 or text.find('Расстояние: 36') != -1:
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '/medpack')
                time.sleep(random.randint(2, 7))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(2, 7))
                        if medpack >0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(2, 7))
                    elif medx1 > 0:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(2, 7))
                        if medx1 > 0:
                            send_msg('@', bot_username, '/medx1')
                            time.sleep(random.randint(2, 7))
                    else:
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(2, 7))
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '👣Идти дальше')
            elif text.find('41км от лагеря') != -1 or text.find('Расстояние: 37') != -1:
                time.sleep(random.randint(2, 7))
                if text.find('нанес тебе удар') != -1:
                    if medpack > 0:
                        send_msg('@', bot_username, '/medpack')
                        time.sleep(random.randint(2, 7))
                        if medpack >0:
                            send_msg('@', bot_username, '/medpack')
                            time.sleep(random.randint(2, 7))
                    elif medx1 > 0:
                        send_msg('@', bot_username, '/medx1')
                        time.sleep(random.randint(2, 7))
                        if medx1 > 0:
                            send_msg('@', bot_username, '/medx1')
                            time.sleep(random.randint(2, 7))
                    elif buffout > 0:
                        send_msg('@', bot_username, '/buffout')
                        time.sleep(random.randint(2, 7))
                        if buffout > 0:
                            send_msg('@', bot_username, '/buffout')
                            time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '👣Идти дальше')
                        #/
                        # Идти дальше
            elif text.find('км от лагеря') != -1 or text.find('Расстояние:') != -1:
                time.sleep(random.randint(2, 7))
                send_msg('@', bot_username, '👣Идти дальше')
                        #/

def send_msg(pref, to, message):
    sender.send_msg(pref + to, message)


receiver.start()  # start the Connector.
receiver.message(work_with_message(receiver))
receiver.stop()


