from flask import Flask, jsonify , Response,render_template,request
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
from datetime import date
from datetime import timedelta

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tatamotors', methods=['POST'])
def tatamotors():
    
    # Get form data
    start_date = request.form['start_date']
    today = date.today()
    # Define the stock symbol and start and end dates
    stock_symbol = 'TATAMOTORS.NS'
    end_date = end_date = today - timedelta(days = 1)

    # Retrieve historical data for the stock
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate moving averages for 50 and 200 days
    stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

    
    output = ""
    if stock_data['Close'][-1] > stock_data['MA50'][-1] and stock_data['MA50'][-1] > stock_data['MA200'][-1]:
        output += f"Tatamotors is currently in an uptrend or in bullish Market, In a bull market, the ideal thing for an investor to do is to take advantage of rising prices by buying stocks early in the trend (if possible) and then selling them when they have reached their peak. \n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."

    elif stock_data['Close'][-1] < stock_data['MA50'][-1] and stock_data['MA50'][-1] < stock_data['MA200'][-1]:
        output += f"Tatamotors is currently in a downtrend or in Bearish Market.Invest for the long term Smart investors understand that the stock market is cyclical and that bear markets are a natural part of the cycle. Therefore, they focus on the long-term outlook for their investments rather than short-term fluctuations in stock prices.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    else:
        output += f"Tatamotors is currently in a sideways trend.When analyzing sideways trends, traders should look at other technical indicators and chart patterns to provide an indicator of where the price may be headed and when a breakout or breakdown may be likely to occur.\n"
        output += "Tip:This is only Suggestion,Invest on your own Risk."
    return output



# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=5000)
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)
    
    
    