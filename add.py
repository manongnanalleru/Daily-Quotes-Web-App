from flask import Flask, render_template
import random

app = Flask(__name__)

def get_random_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return random.choice(quotes)

@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote.strip())

if __name__ == '__main__':
    app.run(debug=True)
