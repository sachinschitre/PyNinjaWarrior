#!/usr/local/bin/python3

from tkinter import *
from tkinter import ttk
import sqlite3
import time
import threading
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from api_helper import ShoonyaApiPy, get_time

import logging  # Import for logging
import pandas as pd

import time

import login

root = Tk()

root.geometry("680x350")

api = ShoonyaApiPy()

count = 0

user = login.user
pwd = login.pwd
factor2 = login.factor2
vc = login.vc
app_key = login.app_key
imei = login.imei

ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

niftyTokens = []
expiry = ""
niftyToken = ""


def startThread(instrument):

    if instrument == "future":
        t1 = threading.Thread(target=futureOi)
        t1.start()

    elif instrument == "oi":
        t1 = threading.Thread(target=oiChange)
        t1.start()


def optionChain():
    global niftyToken
    global niftyTokens

    widgets = optionFrame.winfo_children()

    for widget in widgets:
        widget.destroy()

    incrementor = 50

    startIndex = 13

    if indexName.get() == "NIFTY":
        niftyToken = "26000"
    else:
        niftyToken = "26009"
        startIndex = 17
        incrementor = 100

    try:
        # Attempt login and handle potential errors
        ret = api.get_quotes(exchange="NSE", token=niftyToken)
        ltp = int(float(ret["lp"]))
        ltp = (ltp) - (ltp % incrementor)
    except Exception as e:
        logging.error(f"Error fetching quotes for {niftyToken}: {e}")
        return

    exch = 'NFO'
    query = 'banknifty'

    try:
        # Attempt search and handle potential errors
        ret = api.searchscrip(exchange=exch, searchtext=query)
        if ret is None:
            return
        symbols = ret['values']
    except Exception as e:
        logging.error(f"Error searching for banknifty options: {e}")
        return

    for symbol in symbols:
        if symbol['tsym'].endswith("0"):
            niftyToken = (symbol['tsym'])
            print(niftyToken)
            niftyToken = (niftyToken[9:16])
            print(niftyToken)
            break

    strike = (indexName.get() + niftyToken + "P" + str(ltp))
    print(strike)

    expiry = niftyToken

    try:
        # Attempt getting option chain and handle potential errors
        chain = api.get_option_chain(exchange=exch, tradingsymbol=strike, strikeprice=ltp, count=5)
        chainscrips = []
        for scrip in chain['values']:
            scripdata = api.get_quotes(exchange=scrip['exch'], token=scrip['token'])
            chainscrips.append(scripdata)
    except Exception as e:
        logging.error(f"Error getting option chain for {strike}: {e}")
        return

    print(chainscrips[0]["tsym"])

    i = 0
    j = 9

    Label(optionFrame, text="CHANGE", width=10, bg="blanchedalmond", font=("Arial Black", 10)).grid(row=0, column=0)
    Label(optionFrame, text="CE OI", width=10, bg="blanchedalmond", font=("Arial Black", 10)).grid(row=0, column=1)
    Label(optionFrame, text="LTP", width=10, bg="blanchedalmond", font=("Arial Black", 10)).grid(row=0, column=2)
    Label(optionFrame, text="STRIKE", width=10, bg="blanchedalmond", font=("Arial Black", 10)).grid(row=0, column=
