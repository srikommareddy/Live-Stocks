#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 5 minutes
st_autorefresh(interval=300000, key="refresh")

st.title("📈 NSE Stock Dashboard")
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]

@st.cache_data(ttl=300)
def get_data(symbols):
    data = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1d", interval="5m")
        if not df.empty:
            data[symbol] = df
    return data

stock_data = get_data(stocks)

for symbol, df in stock_data.items():
    st.subheader(symbol)
    st.dataframe(df.tail(5))
  

