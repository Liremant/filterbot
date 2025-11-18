from telegrinder import Dispatch, Message
from telegrinder.rules import IsBot, IsUser, IsChat
from config_loader import config, regex
from custom_rules import IsMessageFromFilterGroup
from env import FILTER_GROUP, ADMIN_GROUP

dp = Dispatch()


@dp.message(IsBot(), IsMessageFromFilterGroup(FILTER_GROUP))
async def bot_message_handler(message: Message):
    if message.from_user.username not in config["bot_exceptions"]["usernames"]:
        return "hey!u will be deleted in 15 min"
    # TODO: логика таймера на 15 минут


@dp.message(IsUser(), IsChat(), IsMessageFromFilterGroup(FILTER_GROUP))
async def regex_uesr_handler(message: Message):
    print("handler triggered")
    print(f"this is regex:{regex['expressions']}")
    print(f"{message.text.unwrap()}")

    if message.text.unwrap() in regex["expressions"]:
        print("regex detected!")
        await message.api.send_message(
            chat_id=ADMIN_GROUP,
            text=(
                "Sussy user detected!\n\n"
                f"From: {message.from_user.full_name}\n"
                f"Username: @{message.from_user.username.unwrap()}\n"
                f"ID: {message.from_user.id}\n\n"
                f"Message: {message.text.unwrap()}"
            ),
        )
