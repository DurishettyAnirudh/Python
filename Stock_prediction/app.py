import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
from datetime import datetime


st.set_page_config(layout="wide")
st.title('Stock Dashboard')


# setting columns
pricing_data, portfolio, news = st.tabs(["Pricing Data", "Stock Portfolio Tracker", "Top 10 News",])
with portfolio:
        if 'portfolio' not in st.session_state:
            st.session_state.portfolio = {}

        def add_stock(symbol, shares):
            """Add a stock to the portfolio."""
            try:
                stock = yf.Ticker(symbol)
                # Try to get the current price from different possible keys
                for price_key in ['regularMarketPrice', 'currentPrice', 'price']:
                    current_price = stock.info.get(price_key)
                    if current_price is not None:
                        break
                
                if current_price is None:
                    # If we couldn't get the price from info, try to get it from history
                    current_price = stock.history(period="1d")['Close'].iloc[-1]
                
                st.session_state.portfolio[symbol] = {
                    'shares': shares,
                    'purchase_price': current_price
                }
                return True
            except Exception as e:
                st.error(f"Error adding stock {symbol}: {str(e)}")
                return False

        def remove_stock(symbol):
            """Remove a stock from the portfolio."""
            if symbol in st.session_state.portfolio:
                del st.session_state.portfolio[symbol]

        def get_current_prices(symbols):
            """Fetch current prices for given symbols."""
            try:
                return yf.download(symbols, period="1d")['Close'].iloc[-1]
            except Exception as e:
                st.error(f"Error fetching current prices: {str(e)}")
                return pd.Series()

        def calculate_portfolio_value(portfolio, current_prices):
            """Calculate the current value of the portfolio."""
            total_value = 0
            for symbol, data in portfolio.items():
                if symbol in current_prices:
                    total_value += data['shares'] * current_prices[symbol]
            return total_value

        # Streamlit UI
        st.title('Stock Portfolio Tracker')

        # Add new stock
        st.subheader('Add New Stock')
        new_stock = st.text_input('Enter stock symbol (e.g., AAPL):')
        shares = st.number_input('Enter number of shares:', min_value=1, value=1)
        if st.button('Add Stock'):
            if new_stock:
                if add_stock(new_stock.upper(), shares):
                    st.success(f'Added {shares} shares of {new_stock.upper()} to your portfolio.')
            else:
                st.error('Please enter a valid stock symbol.')

        # Display and manage portfolio
        st.subheader('Your Portfolio')
        if st.session_state.portfolio:
            symbols = list(st.session_state.portfolio.keys())
            current_prices = get_current_prices(symbols)
            
            portfolio_data = []
            for symbol, data in st.session_state.portfolio.items():
                if symbol in current_prices:
                    current_price = current_prices[symbol]
                    purchase_price = data['purchase_price']
                    shares = data['shares']
                    value = current_price * shares
                    profit_loss = (current_price - purchase_price) * shares
                    profit_loss_percentage = (current_price - purchase_price) / purchase_price * 100
                    
                    portfolio_data.append({
                        'Symbol': symbol,
                        'Shares': shares,
                        'Current Price': f'${current_price:.2f}',
                        'Total Value': f'${value:.2f}',
                        'Profit/Loss': f'${profit_loss:.2f}',
                        'Profit/Loss %': f'{profit_loss_percentage:.2f}%'
                    })
                else:
                    st.warning(f"Could not fetch current price for {symbol}")
            
            if portfolio_data:
                df = pd.DataFrame(portfolio_data)
                st.table(df)
                
                total_value = calculate_portfolio_value(st.session_state.portfolio, current_prices)
                st.subheader(f'Total Portfolio Value: ${total_value:.2f}')
            
            # Remove stock
            stock_to_remove = st.selectbox('Select stock to remove:', symbols)
            if st.button('Remove Stock'):
                remove_stock(stock_to_remove)
                st.success(f'Removed {stock_to_remove} from your portfolio.')
                st.rerun()
        else:
            st.info('Your portfolio is empty. Add some stocks to get started!')

# importing names from the dataset
tickers_df = pd.read_csv('datasets/stock_info.csv')
tickers_list = sorted(tickers_df['Ticker'].tolist())
# Dropdown menu for selecting a ticker with searchable functionality
ticker = st.sidebar.selectbox('Select Ticker', options=tickers_list)

start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')


# using yahoo finance to extract static stock data of selected time period
data = yf.download(ticker, start = start_date, end = end_date) 


with pricing_data:

    data.columns = [col[0] for col in data.columns]
    data.index.name = None

    data.index = data.index.tz_localize(None)
    x = data.index.values
    y = data[f"Adj Close"].values

    fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
    st.plotly_chart(fig)
    st.write('Price Movements')
    data2 = data
    
    data2['% Change'] = (data['Adj Close']/data['Adj Close'].shift(1)-1) * 100
    st.dataframe(data2, width=1200, height=500)
    
    
    annual_return = data2['% Change'].mean()*252*100
    st.write("Annual Return is ",annual_return,"%")

    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Annual Standard Deviation is ', stdev*100, '%')
# from alpha_vantage.fundamentaladata import FundamentalData
# with fundamental_data:
#     key = ''

        



from stocknews import StockNews
with news :
    st.write("Top news here")
    st.header(f"News of {ticker}")
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f"News {i+1}")
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')