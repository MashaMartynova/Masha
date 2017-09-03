import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(bot, update):
    mytext = """Привет, {}{}
Я простой бот и понимаю только команду /start
    """.format(update.message.chat.first_name,update.message.chat.last_name)
    update.message.reply_text(mytext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updtr = Updater('418242420:AAH-Viyzq3tc-gwL63pMhdGnwT2xYNeaAI0')
    
    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()


logging.info('Bot started')
main()
