# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import re
import pandas as pd
import sqlite3

data = requests.get("http://trashr123.herokuapp.com/demo/")
f1_matcher = re.compile("Sullivan Shops III dumpster is currently .*([0-9]+\.[0-9]+)%\n", flags=re.DOTALL)
f2_matcher = re.compile("Last reading taken at \n        <p>(.*)</p>", flags=re.DOTALL)

result1 = f1_matcher.search(data.text)
result2 = f2_matcher.search(data.text)

if type(result1) is None or type(result2) is None:
    print "Something Broke"
    exit()

capacity = float(result1.group(1))
time = pd.to_datetime(result2.group(1))

df = pd.DataFrame({'capacity':[capacity], 'time':[time]})

conn = sqlite3.connect("trashr.db")
df.to_sql("capacity",con=conn, if_exists = 'append')