from email import message
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from googlesearch import search
from bs4 import BeautifulSoup

 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
 
@csrf_exempt
def callback(request):

    keyword_bot_name = '狗狗'
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            msg_text = event.message.text

            if len(msg_text) > 2:
                keyword = msg_text[:2]
            else:
                keyword = ''

            if isinstance(event, MessageEvent) and keyword_bot_name in keyword:  # 如果有訊息事件
                # print(event)
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TextSendMessage(handle_message(msg_text))
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def handle_message(msg_text):
    
    keyword_search = ' 魔法覺醒 Youtube'
    print(msg_text)
    msg_text = msg_text[2:]
    print(msg_text)
    query = msg_text + keyword_search
    print(query)
    for j in search(query, stop=1, pause=2.0): 
        return j




