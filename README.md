# Project 2: Machine Learning & Algorithmic Trading
## Group 12
Amany El Gouhary, Katharine Zenta, Nicolas Hernandez, Al Bakomito 


## Code description
### Notebook 1 (.py file): Streamlit Deployment
#### Part 1: Library & Image imports, User Interface ('UI') setup (ln 1-44)
* In this section we: 

* Import all libraries and their dependencies (ln 1-27). 
* Create our project header, with our introduction,  project objective and upload our first image (ln 28-37). 
* Set up our side bar with the 5 stocks to include in our portfolio, the names of our team members and our 2nd image (ln 38-44). 

#### Part 2: Algorithmic Trading Outputs (ln 45-66)
* In this section we: 
* Pull our five Bollinger Band visualizations,  illsutrating our portfolio totals compared to the S&P500 (ln 45-66). 
* Conclude that, based on our Algorithmic Trading strategies, our portfolio is unlikely to outperform the S&P500, thus creating the need for machine learning models.  
#### Part 3: Machine Learning Outputs (ln 67-80)
* In this section we: 
* Pull our historical portfolio visualization,  illsutrating the superior return of $100000 invested in our portfolio relative to the S&P500 between January 2019 and     mid-June 2022 (ln 67-73). 
* Illustrate our Portfolio's predicted performance compared to the S&P500, using a Long Short-term Memory Network (LSTM), one level sequential model over 10 days (ln 73-77). 
* Zoom in on our validation and prediction period, and  conclude that our portfolio is likely to outperform the S&P500 over the next 10 trading days(ln 78-80). 

### Notebook 2: Algorithmic Trading & Analysis

#### Data Preparation (ln 1-4)
* In this section we: 

* Complete our initial imports of libraries and their dependencies (ln 1). 
* Intialize our  alpaca trade api, using both our public and secret keys (ln 2). 
* Create a function that pulls our 5 tickers' daily closing prices in the given time period using alpaca trade api, initialize the api before using the function, and set the function to return a dataframe with the tickers and closing prices as 2-level column structured df with the index defined as the date (ln 3). 
* Define the stocks in the solar energy portfolio form top performers in 2021 using Motley Fool and Investopedia. The companies are:
   *  First Solar (FSLR)
   *  Brookfield Renewable (BEPC) --> removed. 
   *  Solar Edge Technologies (SEDG). 
   *  Daqo New Energy Corp (DQ). 
   *  Canadian Solar Inc. (CSIQ)

* Conclude by setting ticker information for 4 stocks above (excluding BEPC) but including Algonquin Power & Utilities Corp. (Nasdaq: 'AQN'). We overlay our portfolio constituents with the S&P500 ('SPY') and choose a daily timeframe (all ln 4) 

#### Five-year period: Jan '19 through Jun '22 (ln 5-21)
* In this section we: 
* Set our start and end date. We start in January 2019, as this followed the worst December in the stock market since 1931, and to avoid overfitting our model. We choose our end date as June 15th, 2022, following 10 days of significant losses in the stock market, driven by Federal Reserve monetary tightening (highest single interest rate increase since the '90s), increased recessionary risk, and strong inflation forecasts (ln 5). 
* Drop na's from our df tickers_data (created in ln 5) and display our cleaned df, comprising our 5 stocks and the S&P500 ('SPY'). 
* Create a new function named 'algo_trading' 

### Notebook 3: Machine Learning Models & Analysis 
#### In this section we:
* 
