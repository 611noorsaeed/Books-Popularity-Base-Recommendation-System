from flask import Flask, render_template
import pandas as pd
import pickle

app = Flask(__name__)

popular_df = pickle.load(open('popular_df.pkl','rb'))

books = popular_df.sort_values(by='avg-ratings',ascending=False)[:50]

@app.route('/')
def top_books():
    top_books = books.to_dict('records')
    return render_template('index.html',books = top_books)
if __name__ == "__main__":
    app.run(debug=True)