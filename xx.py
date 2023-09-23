import json
import requests
import time
import hashlib
import urllib.parse
import os
import urllib3
import linecache
import sys
import shutil
import base64
from bs4 import BeautifulSoup as s
import string
import os
import pymongo
import re
import random
import timeit
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import timedelta
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random,string
from keeplive import keep_alive
#point users
client2user = pymongo.MongoClient("mongodb+srv://zz:zz@cluster0.7oqai.mongodb.net/zz?retryWrites=true&w=majority")
mydb= client2user["zz"]

mycol = mydb["users"]
allgive="20"
list = ["1659320313"]
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
 'Cookie': 'Cookie:  __attentive_id=81466e6ab1c145daa23b822d696d0c6d; _attn_=eyJ1Ijoie1wiY29cIjoxNjYwNjM3NDAwMzk0LFwidW9cIjoxNjYwNjM3NDAwMzk0LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjgxNDY2ZTZhYjFjMTQ1ZGFhMjNiODIyZDY5NmQwYzZkXCJ9In0=; _ga=GA1.2.1666502904.1660637400; _gid=GA1.2.436161713.1660637400; _gat_UA-20169249-1=1; __attentive_cco=1660637400570; _clck=13u3hn1|1|f42|0; G_ENABLED_IDPS=google; _gcl_au=1.1.1296437601.1675140238; tpc_a=e6aefd9d30d44b318ad0d6c4fe10a78a.1675140241.hlA.1675140241; _hjSessionUser_1400488=eyJpZCI6ImQ3ZjAyZjIwLWFiZGYtNTQyNS1iZmRiLTA3MzMxMWYxNDM5NiIsImNyZWF0ZWQiOjE2NjA2Mzc0MDA2MzMsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=1; _hjSession_1400488=eyJpZCI6ImNlMGIyMmUzLTEwMGMtNGUyMC1iOTRiLTY5MTcyYzBkZjlkNyIsImNyZWF0ZWQiOjE2NzUxNDAyNDI3MDcsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _uetsid=e2ac8e50a12111ed8224490dcacee5db; _uetvid=d32ca6a01d3a11ed9e6ca5a3dc21832e; __attentive_ss_referrer=https://www.google.com/; __attentive_dv=1; _tt_enable_cookie=1; _ttp=V0bjZIJWnaUpUmlHkRzc0RuGydj; _fbp=fb.1.1675140248830.1270113722; attntv_mstore_email=yoyiexx@zeiluv.xyz:0; refreshToken=a22ef88504f7d092be29f1b9029b3037190ee78e; userId=a4f98a3a-e45d-46ef-b6d9-456790185989; userStatus=A1; promotionId=; sku=bb499firstweek_999_intl_learn_3; accessToken=fbdf52d08e5031917a8256215aefc21fe3a6c03d; bartlebyRefreshTokenExpiresAt=2023-03-02T04:45:25.825Z; _hjHasCachedUserAttributes=true; btbHomeDashboardAnimationTriggerDate=2023-02-01T04:45:33.196Z; btbHomeDashboardTooltipAnimationCount=1; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.bartleby.com%252Flogin; ABTasty=uid=v4rw6gr2jarkvdps&fst=1660641056233&pst=1660641056233&cst=1675140331390&ns=2&pvt=4&pvis=2&th=; __attentive_pv=2; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Jan+31+2023+10%3A15%3A35+GMT%2B0530+(India+Standard+Time)&version=6.32.0&isIABGlobal=false&hosts=&consentId=46215052-f18a-4b4f-8a29-b893e0d96e7b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CBG156%3A1&AwaitingReconsent=false; ki_t=1675140338498%3B1675140338498%3B1675140338498%3B1%3B1; ki_r=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%3D; endCycleWhenQuestionsRemainingWasClosed=2023-02-04T18:46:07.000Z'
}

TOKEN = "6062914829:AAFcTEPplFntnRo7SfuN2gn6GrZfeRZJ_Dw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


class ParseMode(object):
    MARKDOWN = 'Markdown'
    MARKDOWN_V2 = 'MarkdownV2'
    HTML = 'HTML'

def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf-8")
        return (content)
    except:
        pass

def post_url(urll , data, file=None):
    try:
        if file is not None:
            response = requests.post(urll, files=file , data=data)
            return json.loads(response.content.decode())
        else:
            response = requests.post(urll , data=data)
            return json.loads(response.content.decode())
    except:
        pass

def get_updates(offset=None):
    try:
        url = URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        content = get_url(url)
        js = json.loads(content)
        return js
    except:
        pass

def get_last_update_id(updates):
    try:
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)
    except:
        pass


def zro(repy_id):
	try:
		mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
		print(mydoc2)
		print("is sub grube")
		g = [mydoc2]
		oldadd = int(g[0]['point'])
		newadd = int(g[0]['point'])
		clc = oldadd - newadd
		print("is clc sub  :" + str(clc))
		mydict77 = {str(repy_id): str(repy_id), "point": str(clc)}
		mydict4 = {"$set": mydict77}
		mycol.update_one(mydoc2, mydict4)
		return str(clc)
	except:
		pass

#sub grupe
def sub_point(user_id):
	try:
		mydoc2 = mycol.find_one({str(user_id): str(user_id)})
		print(mydoc2)
		print("is sub ")
		g = [mydoc2]
		oldadd = int(g[0]['point'])
		newadd = int("1")
		clc = oldadd - newadd
		print("is clc sub  :" + str(clc))
		mydict77 = {str(user_id): str(user_id), "point": str(clc)}
		mydict4 = {"$set": mydict77}
		mycol.update_one(mydoc2, mydict4)
		return str(clc)
	except:
		pass



#add points
def add_point(repy_id, add):
	try:
		#print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
		mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
		print(mydoc2)
		if str(repy_id) not in str(mydoc2):
			mydict = {str(repy_id): str(repy_id), "point": str(add)}
			x = mycol.insert_one(mydict)
			return str(add)
		else:
			print("is old grupe")
			g = [mydoc2]
			oldadd = int(g[0]['point'])
			newadd = int(add)
			clc = oldadd + newadd
			print("is clc :" + str(clc))
			mydict77 = {str(repy_id): str(repy_id), "point": str(clc)}
			mydict4 = {"$set": mydict77}
			mycol.update_one(mydoc2, mydict4)
			return str(clc)
	except:
		pass



#chuck point
def get_point(user_id):
	try:
		print("id  points :" + str(user_id))
		mydoc2 = mycol.find_one({str(user_id): str(user_id)})
		print(mydoc2)
		if str(user_id) not in str(mydoc2):
			mydict = {str(user_id): str(user_id), "point": allgive}
			x = mycol.insert_one(mydict)
			return allgive
		else:
			g = [mydoc2]
			print("user is old in file time :" + str(g[0]['point']))
			return str(g[0]['point'])
	except:
		pass

def chegg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
    
      text = update.message.text 
    except:
     pass

def Check(update):
    try:
        if not 'callback_query' in str(update) and not 'channel_post' in str(update):
            
            user_id = update["message"]["from"]["id"]
            chat_id = update["message"]["chat"]["id"]
            chat_type= update["message"]["chat"]["type"]
            message_text = update['message']['text']
            try:
                first_name = update["message"]["from"]["first_name"]
            except:
                first_name = ''
            try:
                last_name = update["message"]["from"]["last_name"]
            except:
                last_name = ''
            try:
                username = update["message"]["from"]["username"]
            except:
                username = ''
            
            message_id = update["message"]["message_id"]
            if message_text=='/get':
                pi=get_point(chat_id)
                send_message('Remaining group chances:'+str(pi),chat_id,message_id)
            elif message_text.startswith('/badd-')  and str(user_id) in list:
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add=str(result[0])
                asd=add_point(chat_id ,add)
                send_message('Group chances increased:\n❤️➡️➡️  '+str(asd)+'  ⬅️⬅️❤️' ,chat_id,message_id)
            elif message_text=="/zero"  and str(user_id) in list:
                zz=zro(chat_id)
                print(str(zz))
                send_message("Total points have been deleted",chat_id,message_id)
            elif message_text=="/info"  and str(user_id) in list:
                send_message( 'The number of database groups :'+str(mycol.count()) , chat_id, message_id)


 
            



              
                    
                    
                #if str(chat_type) =='supergroup' or str(chat_type) =='group' :
#
 #                   if text.startswith("https://www.chegg.com/homework-help/questions-and-answers/") or text.startswith("https://www.chegg.com/homework-help/"):
  #                          await Downloader.main(text,mi_context,mi_update,name, user_id, user_name,  )
   #                 
    #                else:
     #                       send_message("  :\nhttps://t.me/Bartleby_vipp\n\nBot only works in groups\nyou can join with this group:\nhttps://t.me/Bartleby_vipp",chat_id,message_id)
        
         
                    

    except:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('Error EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    return True


def send_req(qurl,email):
    try:
        print("p")
    except:
        pass


def editMessage(text, chat_id, text_id , inline_keyboard):
    try:
        url = URL + "editMessageText?chat_id={}&message_id={}&parse_mode=&text={} &reply_markup=".format(chat_id,text_id, text) + inline_keyboard
        r = get_url(url)
        return r
    except:
        pass

def deleteMessage(chat_id, message_id):
    try:
        url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
        get_url(url)
    except:
        pass

def send_message(text, chat_id, text_id = None,inline_keyboard=None,parse_mode=None):
    try:
        data = {
            'text':text,
            'chat_id':chat_id,
            'reply_to_message_id':text_id,
            'reply_markup':inline_keyboard,
            'disable_web_page_preview':True,
            'parse_mode': parse_mode
        }
        r = post_url(URL + "sendMessage",data)
        return r
    except Exception as e:
        print(e)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        # print(updates)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                for i in updates['result']:
                    Check(i)
        except:
            try:
                print(updates['description'])
            except:
                pass



keep_alive()  
#bot.polling(none_stop=True, interval=0)
if __name__ == '__main__':
    main()
keep_alive ()