from nsetools import Nse
from pprint import pprint

nse = Nse()

stock = input("Enter Stock Symbol :")

q = nse.get_quote(stock)

pprint(q)