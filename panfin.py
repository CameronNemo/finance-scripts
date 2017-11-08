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

def histogram(df):
    # Plot volume data in max of thirty intervals
    vol = df['Volume']
    intervals = vol.size
    if intervals > 30:
        intervals = 30
    plt.hist(vol, bins=intervals)
    # Overlay mean and median
    plt.axvline(vol.mean(), color='r', label="Mean")
    plt.axvline(vol.median(), color='g', label="Median")
    # Title and labels
    plt.title("Volume Histogram")
    plt.xlabel("Volume")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

def scatterplot(df):
    # Points
    price_change = abs(df['Open'] - df['Close'])
    plt.plot(price_change, df['Volume'], 'ro')
    # Trend line (linear)
    z = np.polyfit(price_change, df['Volume'], 1)
    trend = np.poly1d(z)
    plt.plot(price_change, trend(price_change), 'b-', label="Fitted line")
    # Title and labels
    plt.title("Price Change-Volume Scatterplot")
    plt.xlabel("Absolute Price Change")
    plt.ylabel("Volume")
    plt.legend(loc='lower right')
    plt.show()

# Tickers are listed as arguments
data = fetch_data(sys.argv[1:], start_date, end_date)

if sys.argv[0] == "./histogram":
    histogram(data)
elif sys.argv[0] == "./scatterplot":
    scatterplot(data)

