

import requests
import sys


try:
    if len(sys.argv) == 1:
        bitcoin_price = 38,761.0833 * float(sys.argv[1])
        print(bitcoin_price)
except IndexError:
    print("Missing command-line argument")








