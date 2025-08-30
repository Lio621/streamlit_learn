import streamlit as st
import yfinance as yf

st.title("Stock Price Analyzer")

stock_name = st.text_input("Enter Stock Ticker", "MSFT")
st.write("Microsoft : MSFT, Google : GOOG, Apple : AAPL, Amazon : AMZN")
ticket_data = yf.Ticker(stock_name)

start_date = st.date_input("Start Date", value=None, min_value=None, max_value=None, key=None)
end_date = st.date_input("End Date", value=None, min_value=None, max_value=None, key=None)

ticker_df = ticket_data.history(start=start_date, end = end_date, interval = '1d')

st.header("Stock Data")
st.dataframe(ticker_df.head(10))

st.subheader("Closing Price over time")
st.line_chart(ticker_df['Close'])

st.subheader("Volume over time")
st.line_chart(ticker_df['Volume'])