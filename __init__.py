from mycroft import MycroftSkill, intent_file_handler


class EasyShop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shop.easy.intent')
    def handle_shop_easy(self, message):
        self.speak_dialog('shop.easy')


def create_skill():
    return EasyShop()

