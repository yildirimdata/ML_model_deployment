import yfinance as yf
import streamlit as st

# source: https://github.com/dataprofessor/code/blob/master/streamlit/part1/myapp.py

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

st.image("bulls-bears.jpeg", width = 600, caption = "source: https://www.istockphoto.com/de/vektor/bull-vs-bear-origami-gm514753795-47901098")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2013-4-27', end='2023-4-27')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.subheader("Daily stock closing price")
st.line_chart(tickerDf.Close)

st.subheader("Daily volume value of google")
st.line_chart(tickerDf.Volume)

st.success("Mission complete!")