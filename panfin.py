#!/usr/bin/env python

import sys

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pandas_datareader import data
#from scipy.optimize import curve_fit

start_date='2017-01-01'
end_date='2017-11-01'

def fetch_data(tickers, start, end):
    source = 'google'
    return data.DataReader(tickers, source, start, end).dropna(1, 'all').to_frame()

def prep_vol_hist(df):
    v = df['Volume']
    b = v.size
    if b > 30:
        b = 30
    plt.hist(v, bins=b)
    plt.axvline(v.mean(), color='r')
    plt.axvline(v.median(), color='b')

def histogram(df):
    prep_vol_hist(df)
    plt.title("Volume Histogram")
    plt.xlabel("Volume")
    plt.ylabel("Frequency")
    plt.show()

def scatterplot(df):
    # Points
    price_change = abs(df['Open'] - df['Close'])
    plt.plot(price_change, df['Volume'], 'ro')
    # Trend line (linear)
    z = np.polyfit(price_change, df['Volume'], 1)
    trend = np.poly1d(z)
    plt.plot(price_change, trend(price_change), 'b-')
    plt.title("Price Change-Volume Scatterplot")
    plt.xlabel("Absolute Price Change")
    plt.ylabel("Volume")
    plt.show()

# Tickers are listed as arguments
data = fetch_data(sys.argv[1:], start_date, end_date)

if sys.argv[0] == "./histogram":
    histogram(data)
elif sys.argv[0] == "./scatterplot":
    scatterplot(data)

