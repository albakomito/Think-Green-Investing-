# Import libraries and their dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
import joblib
import pickle
from collections import Counter
from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import os
import requests
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import json
import hvplot.pandas
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset

# Create Header
st.write('''# Renewable Enegergy Portfolio: An Outperformer?''')
st.write('''## Introduction''')
st.write('Using Machine Learning models from Sci-kit Learn and Tensor Flow, with price action as an indicator, we determine whether our 6-stock renewable energy portfolio has historically outerperformed the S&P500 benchmark.' 
        ' We conclude by using signals from our Algorithmic Trading model to determine by what order of maginitude our equal-weight portfolio is likely to be more profitable than the benchmark.')

# First image
image1 = Image.open('C:/Users/Owner/Class_Notes/03_Projects/Project_2/01_Code/02_consol_code/01_source/farm.jpg')
st.image(image1) 

# Set up sidebar
st.sidebar.header('Choose your stock')
stocks = st.sidebar.selectbox('Stocks', ['FSLR', 'SEDG','CSIQ','AQN','NPIFF','DQ'])
image2 = Image.open('C:/Users/Owner/Class_Notes/03_Projects/Project_2/01_Code/02_consol_code/01_source/ui_logo.jpg')
st.sidebar.image(image2)        
st.sidebar.write('Group 12: Amany El Gouhary, Katharine Zenta, '
                 'Nicolas Hernandez, Al Bakomito')

