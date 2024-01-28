from flask import Flask, render_template
app = Flask(__name__)

import requests

def get_kintone_data():
    url = 'https://[your-subdomain].kintone.com/k/v1/records.json'
    app_id = '[your-app-id]'
    api_token = r"6I59Yzq0u6g2L3gc6oQchsMccyfBjpif7e4tfZmx"
    headers = {
        'X-Cybozu-API-Token': api_token,
        'Content-Type': 'application/json'
    }
    params = {
        'app': app_id
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['records']
    else:
        return None 

@app.route('/')
def index():
    data = get_kintone_data()
    return  render_template('index.html', data=data)
