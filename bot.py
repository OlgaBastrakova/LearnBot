import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь!')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


#означает, что main будет работать, если вызвали python bot.py,  а если для импорта, то работать не будет
if __name__ == "__main__":
    main()
