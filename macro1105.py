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
admin_username = 'YTranslateBot'
import random

# Стартовать бота для корректного счетчика хилок уже с полным закупом!!
medpack = 3
medx1 = 2
buffout = 2
#/
on = 1
distance1 = None
distance2 = None

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
# 🤖 ⚙️ 🏆 💣 👨‍🎤 ✅
# 📦 [3км] 🕳 [7км] 💊 [10км] 🍗 [12км] 🔹 [15км] ❤️ [19км] 💡 [22км] 💾 [29км] 🔩 [36км]

@coroutine
def work_with_message(receiver):
    global bot_user_id
    global on
    while True:
        msg = (yield)
        try:
            if msg['event'] == 'message' and 'text' in msg and msg['peer'] is None and msg['receiver']['username'] == admin_username:
                print('Получена комманда управления от ' + msg['sender']['username'], on)
                handling(msg['text'])
            
            elif msg['event'] == 'message' and 'text' in msg and msg['peer'] is not None:
                if 'username' in msg['sender']:
                    print('Получили сообщение от бота. Проверяем условия', on)
                    parse_text(msg['text'], msg['sender']['username'], msg['id'])
        except Exception as err:
            if apikey is not None:
                ifttt("bot_error", "coroutine", err)
            print('Ошибка coroutine: {0}'.format(err))

# Управление ботом
def handling(text):
    
    global on
    global distance1
    global distance2
    
    if text.find('🤖') == -1:
        if text.find('/gofull') != -1:
            on = 1
            distance1 = None
            distance2 = None
            print('бот ВКЛ', on)
            send_msg('@', admin_username, '🤖 ВКЛ')
        elif text.find('/stopit') != -1:
            on = 0
            distance1 = None
            distance2 = None
            print('бот ВЫКЛ', on)
            send_msg('@', admin_username, '🤖 ВЫКЛ')
        elif text.find('/raid3') != -1:
            on = 1
            distance1 = '3км от лагеря'
            distance2 = 'Расстояние: 3'
            print('Идем на 3км')
            send_msg('@', admin_username, '🤖 Идем на 3км')
        elif text.find('/raid7') != -1:
            on = 1
            distance1 = '7км от лагеря'
            distance2 = 'Расстояние: 7'
            print('Идем на 7км')
            send_msg('@', admin_username, '🤖 Идем на 7км')
        elif text.find('/raid10') != -1:
            on = 1
            distance1 = '10км от лагеря'
            distance2 = 'Расстояние: 10'
            print('Идем на 10км')
            send_msg('@', admin_username, '🤖 Идем на 10км')
        elif text.find('/raid12') != -1:
            on = 1
            distance1 = '12км от лагеря'
            distance2 = 'Расстояние: 12'
            print('Идем на 12км')
            send_msg('@', admin_username, '🤖 Идем на 12км')
        elif text.find('/raid15') != -1:
            on = 1
            distance1 = '15км от лагеря'
            distance2 = 'Расстояние: 15'
            print('Идем на 15км')
            send_msg('@', admin_username, '🤖 Идем на 15км')
        elif text.find('/raid19') != -1:
            on = 1
            distance1 = '19км от лагеря'
            distance2 = 'Расстояние: 19'
            print('Идем на 19км')
            send_msg('@', admin_username, '🤖 Идем на 19км')
        elif text.find('/raid22') != -1:
            on = 1
            distance1 = '22км от лагеря'
            distance2 = 'Расстояние: 22'
            print('Идем на 22км')
            send_msg('@', admin_username, '🤖 Идем на 22км')
        elif text.find('/raid29') != -1:
            on = 1
            distance1 = '29км от лагеря'
            distance2 = 'Расстояние: 29'
            print('Идем на 29км')
            send_msg('@', admin_username, '🤖 Идем на 29км')
        elif text.find('/raid36') != -1:
            on = 1
            distance1 = '36км от лагеря'
            distance2 = 'Расстояние: 36'
            print('Идем на 36км')
            send_msg('@', admin_username, '🤖 Идем на 36км')
        else:
            print('Список комманд управления', on)
            send_msg('@', admin_username, '🤖Список комманд:\n/gofull Старт\n/stopit Стоп\n📦 [3км] /raid3\n🕳 [7км] /raid7\n💊 [10км] /raid10\n🍗 [12км] /raid12\n🔹 [15км] /raid15\n❤️ [19км] /raid19\n💡 [22км] /raid22\n💾 [29км] /raid29\n🔩 [36км] /raid36')
#/

def parse_text(text, username, message_id):
    
    global medpack
    global medx1
    global buffout
    global on
    global distance1
    global distance2
    
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
            if text.find('+30') != -1:
                medx1 = medx1 - 1
            if text.find('+17') != -1:
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
            elif text.find('48км от лагеря') != -1 or text.find('Расстояние: 48') != -1:
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
            elif text.find('45км от лагеря') != -1 or text.find('Расстояние: 45') != -1:
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
            elif text.find('46км от лагеря') != -1 or text.find('Расстояние: 46') != -1:
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
            elif text.find('47км от лагеря') != -1 or text.find('Расстояние: 47') != -1:
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
                if distance1 is not None or distance2 is not None:
                    if text.find(distance1) != -1 or text.find(distance2) != -1:
                        send_msg('@', admin_username, '🤖 Усе, тута я')
                        on = 0
                    else:
                        time.sleep(random.randint(5, 13))
                        send_msg('@', bot_username, '👣Идти дальше')
                else:
                    time.sleep(random.randint(5, 13))
                    send_msg('@', bot_username, '👣Идти дальше')
                        #/
            elif text.find('закончилась выносливость') != -1:
                time.sleep(random.randint(30, 60))
                send_msg('@', bot_username, '👣Идти дальше')



def send_msg(pref, to, message):
    sender.send_msg(pref + to, message)


receiver.start()  # start the Connector.
receiver.message(work_with_message(receiver))
receiver.stop()


