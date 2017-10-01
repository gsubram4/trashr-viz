# -*- coding: utf-8 -*-
from trashr_tools import scrape, loadConfig
from plotting import make_basic_ts_plot

config = loadConfig()
scrape(config)
make_basic_ts_plot(config)