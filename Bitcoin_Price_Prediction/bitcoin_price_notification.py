# -*- coding: utf-8 -*-
"""Bitcoin_Price_Notification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hCif4uOHe96K5LblSk4xUT_NmEi4nqZ-
"""

#Description: Get the current price of Bitcoin


#Resource: 
#1. https://realpython.com/python-bitcoin-ifttt/
#2. https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/

#Import libraries
import requests
from datetime import datetime

#Get the URL ticker to get the .json files of the crypto currencies
TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'

#Function to get the latest crypto currency price of a specific 'crypto' e.g bitcoin, litecoin, etc.
# crypto = {bitcoin, litecoin, ethereum, ...}
def get_latest_crypto_price( crypto ):
    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

#Test the function 
get_latest_crypto_price( 'bitcoin')

BITCOIN_PRICE_THRESHOLD = 10000  # A threshold set to whatever you like

def main():
  
  #Set last_price to -1 to indicate the last price hasn't been recorded yet
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_latest_crypto_price(crypto)
   
    #You can use the following variables to get specific datetime
    #year = datetime.now().year
    #month = datetime.now().month
    #day = datetime.now().day
    #hour = datetime.now().hour
    #minute = datetime.now().minute
    #second = datetime.now().second
    #microsecond = datetime.now().microsecond
    
    now = datetime.now()
    now.strftime("%Y-%m-%d %H:%M")#Returns format (YYYY-mm-DDTHH:MM:SS.MS)
    
    #Check if the crypto currency price is less than your threshold
    if price < BITCOIN_PRICE_THRESHOLD:
      print('The Crypto is lower than your threshold')
    
    #Print the price of bitcoin only if the current price is different from the last price
    if price != last_price:
      print(now.isoformat() , ' Bitcoin price = ',price)
      last_price = price #update last_price to be the current price

main()
