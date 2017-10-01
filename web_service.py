# -*- coding: utf-8 -*-

from flask import Flask, send_file
from trashr_tools import loadConfig
app = Flask(__name__)

config = loadConfig()

@app.route('/')
def basic():
    return send_file("%s/ts_plot.png"%config['output_dir'], mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug='True')