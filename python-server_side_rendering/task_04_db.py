import csv
import json
import os
import sqlite3
from contextlib import closing
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_json_products():
    """Read products from products.json and return a list of dicts"""
    path = os.path.join(BASE_DIR, 'products.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv_products():
    """Read products from products.csv and return a list of dicts"""
    path = os.path.join(BASE_DIR, 'products.csv')
    products = []
    with open(path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


def read_sql_products():
    path = os.path.join(BASE_DIR, 'products.db')
    with closing(sqlite3.connect(path)) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(
            'SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open("items.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    elif source == 'sql':
        data = read_sql_products()
    else:
        return render_template('product_display.html',
                               error='Wrong source', products=[])

    if product_id is not None:
        data = [p for p in data if str(p['id']) == product_id]
        if not data:
            return render_template('product_display.html',
                                   error='Product not found', products=[])

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
