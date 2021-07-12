# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from random import randint
import requests
import pickle
import os

# data request using alpha vantage
symbol = str(sys.argv[1]) #optional for terminal use
API_KEY = 'Your Alphavantage key'

# setup for the functions (query) for the url, csv notation was used:
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY" + f"&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
response = requests.get(url)
contents = response.text
contents_list = list(csv.reader(contents.splitlines()))

"""write different file (using f string for file name) with all stock prices following the
date, ignore the first list (elemental list) inside the 2D list contents_list"""

doc = open(f"prices.{symbol}.txt", 'w')
# for loop will be used to write (full outputsize) the date (index position [i][0])
for i in range (1, len(contents_list)):
    doc.write(f"{contents_list[i][0]} ${float(contents_list[i][4]):.2f} \n")
doc.close()
# program output (not doc.write) for the stock symbol written through command line (argv)
print(f"Wrote historical price data for {symbol} to file price.{symbol}.txt")
