from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_paginate import Pagination


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
db = SQLAlchemy(app)

class Songs(db.Model):

    index = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.String)
    title = db.Column(db.String)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)
    num_bars = db.Column(db.Integer)
    num_sections = db.Column(db.Integer)
    num_segments = db.Column(db.Integer)
    classs = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index(limit=10):
    if request.method == 'POST':
        song_title = request.form['title']
        songs = Songs.query.where(Songs.title==song_title).order_by(Songs.index).all()
        return render_template('search.html', songs=songs)
    else:
        songs = Songs.query.order_by(Songs.index).all()
        page = int(request.args.get("page", 1))
        start = (page - 1) * limit
        end = page * limit if len(songs) > page * limit else len(songs)
        paginate = Pagination(page=page, total=len(songs))
        ret = Songs.query.order_by(Songs.index).slice(start, end)
        return render_template('paginate.html', data=ret, paginate=paginate)

@app.route('/list_all/', methods=['POST', 'GET'])
def list_all(limit=10):
        songs = Songs.query.order_by(Songs.index).all()
        page = int(request.args.get("page", 1))
        start = (page - 1) * limit
        end = page * limit if len(songs) > page * limit else len(songs)
        paginate = Pagination(page=page, total=len(songs))
        ret = Songs.query.order_by(Songs.index).slice(start, end)
        return render_template('paginate.html', data=ret, paginate=paginate)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    songs = Songs.query.get_or_404(id)
    if request.method == 'POST':
        user_rating = int(float(request.form['rating']))
        if user_rating > 5 or user_rating < 0:
            return 'Error: Unable to rate. Please rate 0 - 5.'
        songs.rating = user_rating
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating that song rating.'
    return 'There was a problem updating that song rating.'

if __name__ == "__main__":
    app.run(debug=False)