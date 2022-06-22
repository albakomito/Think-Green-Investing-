# Project 2: Think Green Investing

<img src="https://user-images.githubusercontent.com/99312687/175099873-19f75476-b014-40c2-97d2-16e12625226b.png" width="600" height="400">

The purpose of this project is to use algorithmic trading and machine learning to show our renewable energy portfolio is a good investment for environmentally conscious and socially responsible investors. The following will provide a brief description of how we gathered the data and developed our code, followed by our findings after analysing the data. Finally, we used Streamlit as a frontend development tool to display our result in a user friendly avenue.

## Group 12
Amany El Gouhary, Katharine Zenta, Nicolas Hernandez, Al Bakomito 

## Code description and Data Analysis

### Notebook: Algorithmic Trading & Analysis

#### Data Preparation (ln 1-4)
In this section we: 
* Execute our initial imports of libraries (ln 1). 
* We use the alpaca trade api in order to gather the necessary data (ln 2). 
* Create a function ('get_tickers_data')that pulls our 5 tickers' daily closing prices in the given time period using alpaca trade api (ln 3). This section pulls and cleans the data with the provided function.
* Define the stocks in the solar/wind energy portfolio. The companies are:
   *  First Solar (FSLR) 
   *  Solar Edge Technologies (SEDG). 
   *  Daqo New Energy Corp (DQ). 
   *  Canadian Solar Inc. (CSIQ)
   *  Algonquin Power & Utilities Corp. ('AQN')
* Conclude by setting ticker information for the 5 stocks above. We overlay our portfolio constituents with the S&P500 ('SPY') and choose a daily timeframe (all ln 4).  

#### Three and a half-year period Portfolio: Jan '19 through Jun '22 (ln 5-21)
In this section we: 
* Set our start and end date. We start in January 2019, as this followed the worst December in the stock market since 1931, and to avoid overfitting our model. We choose our end date as June 15th, 2022, following 10 days of significant losses in the stock market, driven by Federal Reserve monetary tightening (highest single interest rate increase since the '90s), increased recessionary risk, and strong inflation forecasts. Finally, we apply the get_tickers_data function (from ln 3) to our time frame, and create the df tickers_data (ln 5). 
* Display our cleaned df, comprising our 5 stocks and the S&P500 ('SPY') index (ln 6). 
* Create the  function 'algo_trading', which returns our Bollinger Bands, RSI, and trading signals in a concatinated dataframe(ln 7). 
* Create the  function 'visualize_algo_trading(bb_df)', which returns plots of our Bollinger Bands by visualizing entry/exit position relative to close price (ln 8).
* Create the function 'cal_return(initial_capital,bb_df)', which returns the df bb_df, using a share size of 100, and other parameters (ln 9). 
* Set starting capital of US$100k and apply the 'algo_trading','visualize_algo_trading(bb_df)', and 'cal_return(initial_capital,bb_df)' to FSLR, and plot our Bollinger Bands (ln 10-11). 
* Similarly, we apply the same 3 functions from ln 10-11 to the other stocks and SPY and print our Bollinger Bands and Portfolio Totals (ln 12-21). 

### Algorithmic Trading Findings 
The purpose of this section is to use alogrithmic trading to show that our renewable energy portfolio provides reasonable returns comparable, if not better than the S&P 500. While developing this strategy, we experienced many trial and errors. Many other stratgies such as DMAC, sentiment analysis and EMA were explored. 
* We decided to use bollinger bands and relative strength index (RSI) in our trading strategy as it had potential to yield good results. The following shows a graph of our strategy applied to the S&P 500:

<img src="https://user-images.githubusercontent.com/99312687/175101519-c5fcec9c-3d57-49cd-b73b-6c3303792061.png" width="800" height="300">

* Below is our trading strategy applied to our portfolio as a whole:

<img src="https://user-images.githubusercontent.com/99312687/175100755-ea621f6c-61c1-4255-9e07-700241538143.png" width="800" height="300">

However, after, again, more trail and error, we found our companies individually did not outperform the S&P 500. This could have been perhaps due to the more volitile trends of the invidual companies in comparison to the steady upward trend of the S&P500. Or simply perhaps with more time we could have optimized and adjusted our code to develop a more refined strategy that would give us better results. Regardless of the reason, due to time constraints we decided to focus the machine learning aspect of the project on predicting the potential returns in comparision to the S&P 500, which as we will see below yielded more desirable results.

### Notebook: Machine Learning Models & Analysis 
#### Data Preparation (ln 1-5). 
In this section we:
* Complete our initial imports (ln 1).  
* Set the random seed for reproducibility (ln 2).
* Initialize alpaca trade api, using our public and secret keys, to gather the necessary data (ln 3). 
* Create the function get_tickers_data that pulls our tickers' daily closing prices in the given time period using alpaca trade api, and returns a df with the tickers, and closing prices as a two level column structured df with index defined as date (ln 4). 
* Similar to Notebook 2 (ln 4), we define the intial 4 top-performing stocks and set the ticker information, adding AQN for this project (ln 5). 

#### Three and a half-year period Portfolio: Jan '19 through Jun '22 (ln 6-15)
In this section we: 
* Apply the get_tickers_data function (from ln 4) to our time frame (see Notebook 2, ln 5), and create the dataframe tickers_data (ln 6). 
* Create an equal-weight portfolio, using the 5 stocks in the tickers_data df (ln 7). 
* Create a plot comprising the value of our portfolio from January 2019 through June 15th, 2022 (ln 8). 
* Test our data from the tickers_data df (ln 9). 
* Set our train_ and test_ generators respectively over a 10-day period (ln 10). 
* Create our LSTM model, and fit the model to our train_generator (ln 11). 
* Perform a prediction using our test_generator (ln 12). 
* Print a line chart comprised of our historical data and our prediction (ln 13). 
* Create the 'predict(num_prediction, model)' function that returns a list of predictions. Create the 'predict_dates(num_prediction)' function that returns prediction dates. Finally, we apply both dates to return a forecast of 30 predictions and prediction dates (ln 14). 
* Create a plot consisting of our historical data, prediction and ground truth (ln 15).  

### Machine Learning Findings
The purpose of this section was to use Long short-term Memory(LSTM) and 30-day Prediction to simulate a predictive machine learning model that analyzes future prices of our renewable energy portfolio in comparison to the S&P500. 

### Notebook (.py file): Streamlit Deployment
The following will decribe the steps involved in deployment of streamlit for the findings in our project.

#### Part 1: Library & Image imports, User Interface ('UI') setup (ln 1-29) 
In this section we: 
* Import all libraries and their dependencies (ln 1-12). 
* Create our project header, with our introduction,  project objective and upload our first image (ln 13-22). 
* Set up our side bar with the 5 stocks to include in our portfolio, the names of our team members and our 2nd image (ln 23-29). 

#### Part 2: Algorithmic Trading Outputs (ln 30-51)
In this section we: 
* Pull our five Bollinger Band visualizations,  illustrating our portfolio totals compared to the S&P500 (ln 30-51). 
* Conclude that, based on our Algorithmic Trading strategies, our portfolio is unlikely to outperform the S&P500, thus creating the need for machine learning models.  

#### Part 3: Machine Learning Outputs (ln 52-65)
In this section we: 
* Pull our historical portfolio visualization,  illustrating the superior return of $100000 invested in our portfolio relative to the S&P500 between January 2019 and mid-June 2022 (ln 52-58). 
* Illustrate our Portfolio's predicted performance compared to the S&P500, using a Long Short-term Memory Network (LSTM), one level sequential model over 10 days (ln 59-65). 
* Conclude that during our validation and prediction period,  our portfolio is likely to outperform the S&P500 over the next 10 trading days. 

### Key Takeaways and Conclusion

### Resources 
https://taraenergy.com/blog/renewable-energy-need-to-know/

