# Project 2: Machine Learning & Algorithmic Trading
## Group 12
Amany El Gouhary, Katharine Zenta, Nicolas Hernandesz, Al Bakomito 


## Code description
### Part 1: Library Importation & Streamlit Setup (ln 1-45) 
In this section we: 
* Import libraries and their dependencies (ln 1-27).
* Create our main Streamlit header, containing our project title, introduction, and objective (ln 28-33).
* Upload our first illustration in the main body of the streamlit UI (ln 34-37). 
* Set up a sidebar with a dropdown list that prompts the user to choose a stock portfolio, namely S&P500,  NASDAQ, and our Custom Portfolio comprised of 6 clean energy stocks (ln 38-45). 

### Part 2: API setup, data retrieval & dataframe cleaning (ln 46-91)
In this section we: 
* Set Alpaca API public and  secret keys (ln 46-55). 
* Sort our API request by setting start and end dates, choosing NASDAQ tickers for all stocks, including American Depository Receipts for non-US companies, and the S&P500 and NASDAQ indices (ln 56-67). 
* Retrieve closing prices from Alpaca, using the get_bars() function (ln 68-74). 
* Reorganize our 7 dataframes and separate our ticker data (ln 75- 85). 
* Concatenate our ticker Dataframes using the ticker axis (ln 86-88). 
* Review our concatenated ticker dataframe (ln 89-91). 

### Part 3: Algorithmic Trading  (ln 92-
In this section we: 
* Define a function (get_tickers_data)that pulls tickers daily closing prices in the given time period using alpaca trade api (ln 92-108). 
* Retrieve 5 years of tickers data using the get_tickers_data function just created (ln 109-117). 
* Define the renewable energy stocks in our portfolio (ln 118-125). 
* Perform the First Solar Algorithm by importing TA from finta, slicing  just the `close` column, determining the Bollinger Bands for the Dataset, concatenating the  Bollinger Bands to the DataFrame, setting the Signal column, and generating the trading signals for a long position trading algorithm (ln 126-146).  
