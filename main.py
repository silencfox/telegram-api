import json
import pprint
import datetime
import time
import csv
import requests 
import logging




if __name__ == '__main__':

    def bot_send_text(bot_message):

        bot_token = '5447******:AAEjEi3qbVrC0c*********************'
        bot_chatID = '1564******'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response


    while True:
        try:
            public = requests.get('http://checkip.amazonaws.com').text.strip()
            text = (f"todo bien: hola kelvin alcala, ip publica {public}")
            bot_send_text(text)
            print("todavia activo")
            time.sleep(18000)

        except Exception as error:
            print(f"catch error: hola error")
            text = (f"catch error: hola error")
            bot_send_text(text)
            print("Con error")
            time.sleep(18000)
