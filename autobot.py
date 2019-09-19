from telegram.ext import Updater

def main():
    mybot = Updater("982211473:AAEyxoYmVLq1hBHEadUuLtKb7To8_oDkebo")
    mybot.start_polling()
    mybot.idle()

main()