from telegrinder import Telegrinder, API, Token, Message
from telegrinder.rules import Text
from env import BOT_TOKEN
import handlers

api = API(Token(str(BOT_TOKEN)))
bot = Telegrinder(api)


@bot.on.message(Text("ping"))
async def message_handler(message: Message):
    await message.answer("pong")


if __name__ == "__main__":
    bot.on.load(handlers.dp)
    bot.run_forever()
