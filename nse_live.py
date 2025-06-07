#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# app.py
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
# List of NSE stock symbols (with .NS suffix for NSE in yfinance)
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"]

st.set_page_config(page_title="NSE Stock Monitor", layout="wide")

st.title("📈 NSE Stock Dashboard")

# Auto-refresh every 5 minutes (300 seconds)
st_autorefresh(interval=300000, key="refresh")
st_autorefresh_interval = 5 * 60 * 1000  # 5 minutes in milliseconds
st.experimental_set_query_params(refresh=str(datetime.now()))
st.experimental_rerun()

st.markdown("### Live Stock Prices (refreshed every 5 minutes)")

# Get live data
@st.cache_data(ttl=300)  # cache for 5 minutes
def get_data(symbols):
    data = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1d", interval="5m")
        if not df.empty:
            data[symbol] = df
    return data

stock_data = get_data(stocks)

# Display data
for symbol, df in stock_data.items():
    st.subheader(symbol)
    st.dataframe(df.tail(5))  # show last 5 entries

