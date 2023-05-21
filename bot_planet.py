import ephem, logging
logging.basicConfig(filename='bot.log', level=logging.INFO)
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

planet_names = {
    'меркурий': 'mercury',
    'венера': 'venus',
    'земля': 'earth',
    'марс': 'mars',
    'юпитер': 'jupiter',
    'сатурн': 'saturn',
    'уран': 'uranus',
    'нептун': 'neptune',
    'плутон': 'pluto'
}


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет,  Введи название планеты: Планета Марс')


 
    

def talk_to_me(update, context):
    

     user_text = update.message.text.lower()
   
     
     if user_text in planet_names:
        planet_info(update, context)
       
     else:
        print("Неправильное название планеты.")
        update.message.reply_text("Неправильное название планеты.")

def planet_info(update, context):

    planet_name = update.message.text.lower()
    planet = getattr(ephem, planet_names[planet_name].capitalize())()
    planet.compute()
    constellation = ephem.constellation(planet)[1]
    print(constellation)
    update.message.reply_text(f'Планета {planet_name.capitalize()} сегодня находится в созвездии {constellation}')
   


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_info))
   
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main() 


