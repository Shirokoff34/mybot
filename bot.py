from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = ('Вызван /start')
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("982211473:AAEyxoYmVLq1hBHEadUuLtKb7To8_oDkebo", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()

main()



