import streamlit as st
import yfinance as yf
st.set_page_config(page_title='Crypto Dashbord',page_icon=":chart_with_upwards_trend:")
st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")

Bitcoin ="BTC-INR"
Ethereum ="ETH-INR"
Ripple="XRP-INR"
BitcoinCash ="BCH-INR"
Solana = "SOL-INR"

BTC_Data=yf.Ticker(Bitcoin)
ETH_Data=yf.Ticker(Ethereum)
XRP_Data=yf.Ticker(Ripple)
BCH_Data=yf.Ticker(BitcoinCash)

BTCHis =BTC_Data.history(period="max")
ETHHis =ETH_Data.history(period="max")
XRPHis =XRP_Data.history(period="max")
BCHHis =BCH_Data.history(period="max")

BTC = yf.download(Bitcoin,period='2h',interval='1m')
ETH = yf.download(Ethereum,period='2h',interval='1m')
XRP = yf.download(Ripple,period='2h',interval='1m')
BCH = yf.download(BitcoinCash,period='2h',interval='1m')

st.write("BITCOIN ($)")
#Display a table
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)

st.write("ETHEREUM ($)")
st.table(ETH)
st.bar_chart(ETHHis.Close)

st.write("RIPPLE ($)")
st.table(XRP)
st.bar_chart(XRPHis.Close)

st.write("BITCOINCASH ($)")
st.table(BCH)
st.bar_chart(BCHHis.Close)

