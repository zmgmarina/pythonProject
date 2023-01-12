import logging
from token_1 import *
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, Filters, MessageHandler

reply_keyboard = [['/play', '/setting'],  
                  ['/instruction', '/close'],
                  ['/picture']] 

candies = 50
step = 15
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False) 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

TOKEN = token1


def start(update, context):
    name = f"{update.message.from_user.first_name} {update.message.from_user.last_name}"
    update.message.reply_text(
        f"Привет, {name}! Я бот, приглашаю тебя в игру Конфетки.",
        reply_markup=markup   

def close(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove() 
    )

def instruction(update, context):
    update.message.reply_text(
        "Игру начинает человек. В начале игры нужно определить количество конфет на кону "
        "и количество конфет, которое можно взять за один ход. Для этого"
        " нажмите settings и введите 2 числа. Игроки ходят по очереди. Выигрывает тот, кто сделал последний ход и забрал оставшиеся конфеты.")


def setting(update, context):
    update.message.reply_text(
        "Введите количество конфет на кону и максимальное количество конфет на один ход через пробел")
    return 1

def set_setting(update, context):
    global candies
    global step      
    candies, step = map(int, update.message.text.split())
    update.message.reply_text("Правила установлены, можно начать игру, нажмите кнопку /play!")
    return ConversationHandler.END  


def play(update, context):
    update.message.reply_text(f"Ваш ход. На кону {candies} конфет. Сколько конфет вы возьмете?"
                              f"Максимальное = {step}")
    return 1

def play_step(update, context):
    global candies
    candy = int(update.message.text)
    candies -= candy
    if candies <= step:
        update.message.reply_text("Игра окончена, я забираю конфеты, я победил!")
        return ConversationHandler.END
    else:
        update.message.reply_text(f"На кону {candies} конфет, я беру {candies % (step + 1)} конфет")
        candies -= candies % (step + 1)
        if candies <= step:
            update.message.reply_text("Поздравляю, ты победил!")
            return ConversationHandler.END


def picture(update, context):
    context.bot.send_photo(update.effective_chat.id, photo=open('candy.jpg', 'rb'))


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    setting_handler = ConversationHandler(
        entry_points=[CommandHandler('setting', setting)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_setting)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("instruction", instruction))
    dp.add_handler(setting_handler)
    dp.add_handler(play_handler)
    dp.add_handler(CommandHandler("close", close))
    dp.add_handler(CommandHandler("picture", picture))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
