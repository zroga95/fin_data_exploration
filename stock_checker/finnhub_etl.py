import requests
import json
import pandas as pd
from datetime import datetime
from pprint import pprint

def run_finnhub_etl():

	#put api secret here
    token = ""
    symbol = "TSLA" 

    #get peer tickers
    base_url = 'https://finnhub.io/api/v1/stock/peers?'
    r = requests.get(base_url, params = {'symbol': symbol, 'token':token})
    text = r.text
    company_peers = json.loads(text)

    #get financial data
    peer_list = []
    base_url = "https://finnhub.io/api/v1/stock/profile2?"
    for stock in company_peers:
	    r = requests.get(base_url, params = {'symbol':stock,'token':token})
	    text = r.text
	    company_profile = json.loads(text)
	    peer_list.append(company_profile)

    industry_df = pd.DataFrame(peer_list)
    industry_df.to_csv('industry_stock_data.csv')

run_finnhub_etl()