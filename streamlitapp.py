# Import libraries and their dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
from PIL import Image

import os
import requests


# Create Header
st.write('''# Renewable Enegergy Portfolio: An Outperformer?''')
st.write('''## Introduction''')
st.write('Using signals from our Algorithmic Trading model, we attempt to determine if our 5-stock equal-weight renewable energy portfolio is likely to outperform the benchmark S&P500 index.' 
         ' Finally, we conclude by using Machine Learning models from Sci-kit Learn and Tensor Flow, with price action as an indicator, that our renewable energy portfolio is likely to outperform the S&P500.')

# First image
image1 = Image.open('./Visualizations/farm.jpg')
st.image(image1) 

# Set up sidebar
st.sidebar.header('FSLR,SEDG, CSIQ, AQN, DQ Portfolio')
image2 = Image.open('./Visualizations/ui_logo.jpg')
st.sidebar.image(image2)        
st.sidebar.write('Group 12: Amany El Gouhary, Katharine Zenta, '
                 'Nicolas Hernandez, Al Bakomito')

# Algorithmic Trading Outputs 
st.write ('''## Algorithmic Trading & Bollinger Bands''') 
st.write('Portfolio Total (SPY): US$137175')
image3= Image.open('./Visualizations/Algo1.jpg')
st.image(image3)

st.write('Portfolio Total(Think Green Portfolio): US$150284')
image4= Image.open('./Visualizations/Algo2.jpg')
st.image(image4)

# Machine Learning Outputs 
st.write('''## Machine Learning Outputs''')
st.write('''### LSTM One-level Sequential Model, 10 Day Window''')
st.write('Portfolio & SPY Closing Price: US$100k Initial Investment')
image5= Image.open('./Visualizations/ML1.jpg')
st.image(image5)

st.write('Validation & Prediction Period')
image6= Image.open('./Visualizations/ML2.jpg')
st.image(image6)

st.write('Validation & Prediction Period: Zoomed in')
image7= Image.open('./Visualizations/ML3.jpg')
st.image(image7)