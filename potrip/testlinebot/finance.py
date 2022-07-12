import pandas as pd
import requests, json

import matplotlib.pyplot as plt
import mplfinance as mpf

def get_stock_data(date, stock_no):

    html = requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=%s&stockNo=%s' % (date,stock_no))
    content = json.loads(html.text)
    stock_data = content['data']
    col_name = content['fields']

    df = pd.DataFrame(data=stock_data, columns=col_name)
    df.head()
    return df

