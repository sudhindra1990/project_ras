# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:22:08 2024

@author: z0035k1b
"""
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def fetch_data():
    # This is a dummy URL; replace with an actual endpoint for real usage
    response = requests.get('https://api.example.com/data')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

