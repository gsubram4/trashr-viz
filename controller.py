# -*- coding: utf-8 -*-
from ConfigParser import SafeConfigParser
import os
from trashr_scape import scrape
from plotting import make_basic_ts_plot

def loadConfig():
    parser = SafeConfigParser()
    parser_path = os.path.dirname(os.path.realpath(__file__))+"/trashr_config.ini"
    parser.read(parser_path)
    return dict(parser.items("trashr"))

config = loadConfig()
scrape(config)
make_basic_ts_plot(config)