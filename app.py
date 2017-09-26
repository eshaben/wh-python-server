import sqlite3
from flask import Flask, request
import json


app = Flask(__name__)

@app.route('/api/hoops', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        all_hoops = get_all_hoops()
        return json.dumps(all_hoops)
        pass
    elif request.method == 'POST':
        pass

def get_all_hoops():
    with sqlite3.connect('hoops.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM hoops")
        all_hoops = cursor.fetchall()
        return all_hoops

if __name__ == '__main__':
    app.debug = True
    app.run()
