from random import randrange

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from search import Search


class VKinder(Search):

    def __init__(self, token):
        super().__init__()
        self.vkapi = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(self.vkapi)

    def write_msg(self, user_id, message):
        self.vkapi.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })

    def run(self):

        print("Running...")

        for event in self.longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:

                if event.to_me:

                    request = event.text

                    if request == "Топ":
                        search = self.top(event.user_id, self.vkapi)
                        self.write_msg(event.user_id, search)
                        print("User {} starting top query".format(event.user_id))
                    elif request == "Начать":
                        self.write_msg(event.user_id, "Команды:\n\nТоп - получить топ 3 по лайкам и комментариям")
                        print("User {} starting".format(event.user_id))
                    else:
                        self.write_msg(event.user_id, "Не поняла вашего ответа...")
