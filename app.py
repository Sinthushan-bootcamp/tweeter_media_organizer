from flask import Flask, escape, render_template, request
import twitter_app
import pdb
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    urls = []
    if request.method == 'POST':
        id = request.form['user_name']
        col = request.form['sort_by']
        ascending = request.form['sort_order'] == 'True'
        df = twitter_app.get_twitter_data(id)
        df = df.sort_values(by=[col], ascending=ascending)
        urls = df['media'].tolist()
        print(urls)
    return render_template('index.html', urls=urls)
