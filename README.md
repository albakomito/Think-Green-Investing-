# Project 2: Machine Learning & Algorithmic Trading
## Group 12
Amany El Gouhary, Katharine Zenta, Nicolas Hernandez, Al Bakomito 


## Code description
### Notebook 1 (.py file): Streamlit Deployment
#### Part 1: Library & Image imports, User Interface ('UI') setup (ln 1-44)
In this section we: 

* Import all libraries and their dependencies (ln 1-27). 
* Create our project header, with our introduction,  project objective and upload our first image (ln 28-37). 
* Set up our side bar with the 5 stocks to include in our portfolio, the names of our team members and our 2nd image (ln 38-44). 

#### Part 2: Algorithmic Trading Outputs (ln 45-66)
In this section we: 
* Pull our five Bollinger Band visualizations,  illustrating our portfolio totals compared to the S&P500 (ln 45-66). 
* Conclude that, based on our Algorithmic Trading strategies, our portfolio is unlikely to outperform the S&P500, thus creating the need for machine learning models.  
#### Part 3: Machine Learning Outputs (ln 67-80)
In this section we: 
* Pull our historical portfolio visualization,  illustrating the superior return of $100000 invested in our portfolio relative to the S&P500 between January 2019 and     mid-June 2022 (ln 67-73). 
* Illustrate our Portfolio's predicted performance compared to the S&P500, using a Long Short-term Memory Network (LSTM), one level sequential model over 10 days (ln 73-77). 
* Zoom in on our validation and prediction period, and  conclude that our portfolio is likely to outperform the S&P500 over the next 10 trading days(ln 78-80). 

### Notebook 2: Algorithmic Trading & Analysis

#### Data Preparation (ln 1-4)
In this section we: 

* Execute our initial imports of libraries and their dependencies (ln 1). 
* Initialize our  alpaca trade api, using both our public and secret keys (ln 2). 
* Create a function ('get_tickers_data')that pulls our 5 tickers' daily closing prices in the given time period using alpaca trade api, initialize the API before using the function, and set the function to return a dataframe with the tickers and closing prices as a 2-level column structured df with the index defined as the date (ln 3). 
* Define the stocks in the solar energy portfolio form top performers in 2021 using Motley Fool and Investopedia. The companies are:
   *  First Solar (FSLR)
   *  Brookfield Renewable (BEPC) --> removed. 
   *  Solar Edge Technologies (SEDG). 
   *  Daqo New Energy Corp (DQ). 
   *  Canadian Solar Inc. (CSIQ)

* Conclude by setting ticker information for 4 stocks above (excluding BEPC) and  Algonquin Power & Utilities Corp. (Nasdaq: 'AQN'). We overlay our portfolio constituents with the S&P500 ('SPY') and choose a daily timeframe (all ln 4).  

#### Five-year period Portfolio: Jan '19 through Jun '22 (ln 5-21)
In this section we: 
* Set our start and end date. We start in January 2019, as this followed the worst December in the stock market since 1931, and to avoid overfitting our model. We choose our end date as June 15th, 2022, following 10 days of significant losses in the stock market, driven by Federal Reserve monetary tightening (highest single interest rate increase since the '90s), increased recessionary risk, and strong inflation forecasts. Finally, we apply the get_tickers_data function (from ln 3) to our time frame, and create the df tickers_data (ln 5). 
* Drop na's from our df tickers_data (created in ln 5) and display our cleaned df, comprising our 5 stocks and the S&P500 ('SPY') index (ln 6). 
* Create the  function  'algo_trading', which returns our Bollinger Bands df, after determining Bollinger Bands for the Dataset, concatenating the Bollinger Bands to the DataFrame, calculating RSI, and generating the trading signals 1 (entry) or -1 (exit) for a long position trading algorithm (ln 7). 
* Create the  function  'visualize_algo_trading(bb_df)', which returns plots of our Bollinger Bands by visualizing exit position relative to close price, visualizing close price for the investment, and overlaying our plots(ln 8).
* Create the function 'cal_return(initial_capital,bb_df)', which returns the df bb_df, using a share size of 100, and other parameters (ln 9). 
* Set starting capital of US$100k and apply the 'algo_trading','visualize_algo_trading(bb_df)', and 'cal_return(initial_capital,bb_df)' to FSLR, and plot our Bollinger Bands (ln 10-11). 
* Similarly, we apply the same 3 functions from ln 10-11 to the other stocks and SPY and print our Bollinger Bands (ln 12-21).  

### Notebook 3: Machine Learning Models & Analysis 
#### Data Preparation (ln 1-5). 
In this section we:
* Complete our initial imports (ln 1).  
* Set the random seed for reproducibility (ln 2).
* Initialize alpaca trade api, using our public and secret keys (ln 3). 
* Create the function get_tickers_data that pulls our tickers' daily closing prices in the given time period using alpaca trade api, and returns a df with the tickers, and closing prices as a two level column structured df with index defined as date (ln 4). 
* Similar to Notebook 2 (ln 4), we define the top-performing stocks and set the ticker information, adding AQN (ln 5). 

#### Five-year period Portfolio: Jan '19 through Jun '22 (ln 6-15)
In this section we: 
* Apply the get_tickers_data function (from ln 4) to our time frame (see Notebook 2, ln 5), and create the df tickers_data (ln 6). 
* Create an equal-weight portfolio, using the 5 stocks in the tickers_data df (ln 7). 
* Create a plot comprising the value of our portfolio from January 2019 through June 15th, 2022 (ln 8). 
* Test our data from the tickers_data df (ln 9). 
* Set our train_ and test_ generators respectively over a 10-day period (ln 10). 
* Create our LSTM model, and fit the model to our train_generator (ln 11). 
* Perform a prediction using our test_generator (ln 12). 
* Print a line chart comprised of our historical data and our prediction (ln 13). 
* Create the 'predict(num_prediction, model)' function that returns a list of predictions. Create the 'predict_dates(num_prediction)' function that returns prediction dates. Finally, we apply both dates to return a forecast of 30 predictions and prediction dates (ln 14). 
* Create a plot consisting of our historical data, prediction and ground truth (ln 15).  
