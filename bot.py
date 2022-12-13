from keyboard import sender
from VKinder import *


for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            print("User {} starting top query".format(user_id))
            creating_database()
            bot.write_msg(user_id, f'Привет, {bot.name(user_id)}')
            bot.find_user(user_id)
            bot.write_msg(event.user_id, f'Нашла для тебя пару, жми на кнопку "Вперёд"')
            bot.find_persons(user_id, offset)

        elif request == 'вперёд':
            for i in line:
                offset += 1
                bot.find_persons(user_id, offset)
                print("User {} next top query".format(user_id))
                break

        else:
            bot.write_msg(event.user_id, 'Простите но я вас не понела.')
