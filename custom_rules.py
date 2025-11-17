from telegrinder import ABCRule, Message


class IsMessageFromFilterGroup(ABCRule):
    def __init__(self, modchat):
        self.modchat = modchat

    def check(self, message: Message):
        if message.chat.id == self.modchat:
            return True
        else:
            return False
