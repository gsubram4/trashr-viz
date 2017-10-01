# -*- coding: utf-8 -*-
import matplotlib as mpl
mpl.use('Agg')
import seaborn as sns
import pandas as pd
import sqlite3
import sqlalchemy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def make_basic_ts_plot(config):
    db_name = config['db_dir']
    engine = sqlalchemy.create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
    df = pd.read_sql_table("capacity", engine,parse_dates="time")
    
    sns.set_context('talk')
    xfmt = mdates.DateFormatter('%H:%M')
    
    time = df.time.as_matrix()
    capacity = df.capacity.as_matrix()
    fig = plt.figure(1)
    plt.clf()
    plt.plot(time, capacity, lw=4)
    plt.ylim([0,100])
    fig.autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(xfmt)
    
    plt.xlabel('time')
    plt.ylabel('capacity (%)')
    plt.title('A Day in the Life of Lonely Dumpster')
    plt.savefig("%s/ts_plot.png"%(config['output_dir']))
