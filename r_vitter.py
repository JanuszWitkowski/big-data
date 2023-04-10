#!/usr/bin/python3
from random import random, randrange    # random.uniform(a, b)
import cryptocompare
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class RVitter :
    def __init__(self, size_of_sample: int):
        self.k = 0
        self.n = size_of_sample
        self.data = [None for _ in range(size_of_sample)]
    
    def step(self, elem):
        self.k += 1
        if self.k <= self.n:
            self.data[self.k - 1] = elem
        else:
            if random() < self.n/self.k:
                self.data[randrange(self.n)] = elem
    
    def get(self):
        return self.data
    
    def clear(self):
        self.k = 0
        for i in range(self.n):
            self.data[i] = None



def vitter_bitcoin(size_of_sample: int):
    # Define the ticker symbol and other details
    ticker_symbol = 'BTC'
    currency = 'USD'
    limit_value = 2000
    exchange_name = 'CCCAGG'
    data_before_timestamp = datetime.now()

    # Fetch the raw price data
    raw_price_data = cryptocompare.get_historical_price_day(
    # raw_price_data = cryptocompare.get_historical_price_hour(
        ticker_symbol,
        currency,
        limit=limit_value,
        exchange=exchange_name,
        toTs=data_before_timestamp
    )

    # Convert the raw price data into a DataFrame
    daily_price_data = pd.DataFrame.from_dict(raw_price_data)
    # print(raw_price_data)
    # print(daily_price_data)

    # Set the time columns as index and convert it to datetime
    daily_price_data.set_index("time", inplace=True)
    daily_price_data.index = pd.to_datetime(daily_price_data.index, unit='s')
    daily_price_data['datetimes'] = daily_price_data.index
    daily_price_data['datetimes'] = daily_price_data['datetimes'].dt.strftime(
        '%Y-%m-%d')
    # print(daily_price_data)

    # Plot the close price
    plt.subplot(2, 1, 1)
    plt.figure(figsize=(15, 7))
    plt.plot(daily_price_data.close)
    # Set title and labels for the plot
    plt.title('BTC Close Price', fontsize=16)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Price ($)', fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    # Show the plot
    plt.savefig('z22_r_vitter/btc_full.png')
    # plt.show()

    # Vitter's R Algorithm
    rv = RVitter(size_of_sample)
    for _, row in daily_price_data.iterrows():
        rv.step(row)
    r_vitter_data = pd.DataFrame(rv.get()).close
    r_vitter_data.sort_values(by='time', inplace = True) 

    # Plot Vitter's R
    plt.subplot(2, 1, 2)
    plt.figure(figsize=(15, 7))
    plt.plot(r_vitter_data)
    # Set title and labels for the plot
    plt.title('BTC Close Price with Random Sample', fontsize=16)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Price ($)', fontsize=15)
    plt.tick_params(axis='both', labelsize=15)
    # Show the plot
    plt.savefig('z22_r_vitter/btc_vitter.png')
    # plt.show()



if __name__ == "__main__":
    size_of_sample = 40
    # rv = RVitter(40)
    # for i in range(10**3):
    #     rv.step(i)
    # print(rv.get())
    vitter_bitcoin(size_of_sample=size_of_sample)

