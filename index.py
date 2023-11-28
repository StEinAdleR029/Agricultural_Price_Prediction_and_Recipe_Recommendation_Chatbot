import bs4
import random
import telegram
import telepot
import requests
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from urllib.request import urlopen
import urllib.parse
from apscheduler.schedulers.blocking import BlockingScheduler
from telepot.loop import MessageLoop # 봇 구동
from telepot.namedtuple import InlineKeyboardMarkup as MU # 마크업
from telepot.namedtuple import InlineKeyboardButton as BT # 버튼
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import googletrans
from google.cloud import vision
import io
import datetime as dt
from dateutil.relativedelta import relativedelta
#파이썬 파일
import main
import apple
import cabbage
import getleaf
import minari
import paprika
import piment

# 시간 관련 코드

x = dt.datetime.now()
#print(x.strftime('%Y-%m-%d'))
before_one_year = x - relativedelta(years=1)
#print(before_one_year.strftime('%Y-%m-%d'))

# 봇과 관련된 파트

# 김태현

my_api_key = '5465262269:AAHTrY13Lg_AjkL0IemFSsY-hOWxXYdaqIA'
chat_room_id = 5488274887
bot = telegram.Bot(token = '5465262269:AAHTrY13Lg_AjkL0IemFSsY-hOWxXYdaqIA')

# 변수
chepeast_food_ingredient = ''
cheapest_food_name = ''

# Updater 관련 코드

updater = Updater(token=my_api_key, use_context=True)
dispatcher = updater.dispatcher

# 전송 코드
def start(update, context):
    foods = main.main()
    recipe = []
    #db에서 레시피 받는 코드
    update.message.reply_text("환영합니다! 농산물 가격 예측 후 레시피를 알려주는 시스템입니다.")
    update.message.reply_text("현재 날짜는 " + x.strftime('%Y-%m-%d') + " 이고, 1년 전 데이터를 기준으로 언제 사는 것이 저렴한지 이야기 해드리도록 하겠습니다.")
    
    
    for food in foods.keys():
        update.message.reply_text(before_one_year.strftime('%Y-%m-%d') + "을 기준으로, "  + str(list(foods.keys()).index(food) + 1) +"번째로 싼 농산물은 " + food + " 입니다.")
        update.message.reply_text("레시피를 추천해드리자면, " + food + "을/를 이용해 만든 " + cheapest_food_name + "이 있습니다.")
    
        #레시피 출력
    
    
updater.dispatcher.add_handler(CommandHandler('start', start))
    
# polling

updater.start_polling()
updater.idle()

start()