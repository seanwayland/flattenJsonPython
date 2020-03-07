
# Dependencies
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint 

# function to flatten json object
def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
    
    
url = "http://api.worldbank.org/v2/"
format = "json"
# Get country information in JSON format from API call 
countries_response = requests.get(f"{url}countries?format={format}").json()


f = flatten_json(countries_response)

data = pd.DataFrame(json_normalize(f))
# make rows into columns so it's easier to read
data = data.transpose()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    display(data)
# First element is general information, second is countries themselves
val = countries_response[1][26]['name']
print(val)
