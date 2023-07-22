# main.py

from flask import Flask, render_template, request, redirect
import random
import string
import sqlite3
import validators
import requests
import sqlite3

# Create the database and URL table
connection = sqlite3.connect('urls.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        long_url TEXT NOT NULL,
        short_url TEXT NOT NULL UNIQUE
    )
''')

connection.commit()
connection.close()

# start the flask implementation and code logic


app = Flask(__name__)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # You can adjust the length of the short URL
    return short_url

def is_short_url_available(short_url):
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    connection.close()

    return result is None

def shorten_url(long_url, custom_short_url=None):
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    if custom_short_url:
        if not is_short_url_available(custom_short_url):
            return "Custom short URL is not available. Please choose another one."

    if custom_short_url:
        short_url = custom_short_url
    else:
        short_url = generate_short_url()
        while not is_short_url_available(short_url):
            short_url = generate_short_url()

    cursor.execute('INSERT INTO urls (long_url, short_url) VALUES (?, ?)', (long_url, short_url))
    connection.commit()
    connection.close()

    return short_url

def retrieve_long_url(short_url):
    connection = sqlite3.connect('urls.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    connection.close()

    return result[1] if result else None

def has_valid_ssl_certificate(url):
    try:
        response = requests.get(url, verify=True)
        return response.status_code == 200
    except requests.exceptions.SSLError:
        return False
    except requests.exceptions.RequestException:
        return False

def is_valid_url(url):
    if not validators.url(url):
        return False

    # Check if the URL uses HTTPS and has a valid SSL certificate
    if url.startswith('https://') and not has_valid_ssl_certificate(url):
        return False

    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    custom_short_url = request.form['custom_short_url']

    if not is_valid_url(long_url):
        return render_template('index.html', error="Invalid URL. Please enter a valid URL.")

    if custom_short_url and not custom_short_url.isalnum():
        return render_template('index.html', error="Custom short URL can only contain letters and numbers.")

    if custom_short_url and not is_short_url_available(custom_short_url):
        return render_template('index.html', error="Custom short URL is not available. Please choose another one.")

    shortened_url = shorten_url(long_url, custom_short_url)
    return render_template('index.html', shortened_url=shortened_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = retrieve_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return f"Short URL '{short_url}' not found."

if __name__ == '__main__':
    app.run(debug=True)
