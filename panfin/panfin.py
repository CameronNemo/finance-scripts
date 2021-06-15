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
    vol = df['Volume'] / 1000000
    intervals = vol.size
    if intervals > 30:
        intervals = 30
    plt.hist(vol, bins=intervals)
    # Overlay mean and median
    plt.axvline(vol.mean(), color='r', label="Mean = {:4.3f}".format(vol.mean()))
    plt.axvline(vol.median(), color='g', label="Median = {:4.3f}".format(vol.median()))
    # Title and labels
    plt.title("Volume Histogram")
    plt.xlabel("Volume (in millions)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("histogram.svg", format="svg")
    plt.show()

def scatterplot(df):
    # Points
    pct_change = 100 * abs(df['Open'] - df['Close']) / df['Open']
    plt.plot(pct_change, df['Volume'] / 1000000, 'ro', label='Observations')
    # Trend line (linear)
    z = np.polyfit(pct_change, df['Volume'] / 1000000, 1)
    trend = np.poly1d(z)
    plt.plot(pct_change, trend(pct_change), 'b-', label="Linear fit {}".format(trend))
    # Title and labels
    plt.title("Price Change-Volume Scatterplot")
    plt.xlabel("Absolute Percent Price Change")
    plt.ylabel("Volume (in millions)")
    plt.legend(loc='lower right')
    plt.savefig("scatterplot.svg", format="svg")
    plt.show()

# Tickers are listed as arguments
data = fetch_data(sys.argv[1:], start_date, end_date)

if sys.argv[0] == "./histogram":
    histogram(data)
elif sys.argv[0] == "./scatterplot":
    scatterplot(data)

