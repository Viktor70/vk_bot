from _token import token
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


class Bot:
    def __init__(self):
        self.group_id = 194541815
        self.vk_session = vk_api.VkApi(token=token)

        self.longpoll = VkBotLongPoll(self.vk_session, self.group_id)
        self.vk = self.vk_session.get_api()

    def run(self):
        """ Пример использования bots longpoll
            https://vk.com/dev/bots_longpoll
        """

        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                print('Новое сообщение:')
                print('Для меня от: ', end='')
                print(event.obj.from_id)
                print('Текст:', event.obj.text)
                print()
                self.vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=("Новое сообщение - " + event.obj.text)
                )
                print('ok')
            elif event.type == VkBotEventType.MESSAGE_REPLY:
                print('Новое сообщение:')
                print('От меня для: ', end='')
                print(event.obj.peer_id)
                print('Текст:', event.obj.text)
                print()
            elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                print('Печатает ', end='')
                print(event.obj.from_id, end=' ')
                print('для ', end='')
                print(event.obj.to_id)
                print()
            elif event.type == VkBotEventType.GROUP_JOIN:
                print(event.obj.user_id, end=' ')
                print('Вступил в группу!')
                print()
            elif event.type == VkBotEventType.GROUP_LEAVE:
                print(event.obj.user_id, end=' ')
                print('Покинул группу!')
                print()
            else:
                print(event.type)
                print()


if __name__ == '__main__':
    vkbot = Bot()
    vkbot.run()