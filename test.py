from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
engine = create_engine('sqlite:///music.db', echo = True)
meta = MetaData()
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

songs = Table(
   'songs', meta, 
    Column('index', Integer, primary_key = True),
    Column('id',  String),
    Column('title', String),
    Column('danceability', Float),
    Column('energy',  Float),
    Column('key',  Integer),
    Column('loudness',  Float),
    Column('mode',  Integer),
    Column('acousticness',  Float),
    Column('instrumentalness',  Float),
    Column('liveness',  Float),
    Column('valence',  Float),
    Column('tempo',  Float),
    Column('duration_ms',  Integer),
    Column('time_signature',  Integer),
    Column('num_bars',  Integer),
    Column('num_sections',  Integer),
    Column('num_segments',  Integer),
    Column('classs',  Integer),
    Column('rating', Float),
)
meta.create_all(engine)

class Songs(Base):
    __tablename__ = 'songs'
    
    index = Column(Integer, primary_key = True)
    id = Column(String)
    title = Column(String)
    danceability = Column(Float)
    energy = Column(Float)
    key = Column(Integer)
    loudness = Column(Float)
    mode = Column(Integer)
    acousticness = Column(Float)
    instrumentalness = Column(Float)
    liveness = Column(Float)
    valence = Column(Float)
    tempo = Column(Float)
    duration_ms = Column(Integer)
    time_signature = Column(Integer)
    num_bars = Column(Integer)
    num_sections = Column(Integer)
    num_segments = Column(Integer)
    classs = Column(Integer)
    rating = Column(Float)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()


import json
music = json.load(open('playlist.json'))
columns = [attribute for attribute in music.keys()]
songs = list()
num_songs = len(music[columns[0]])
for i in range(num_songs):
    songs.append( [music[c][str(i)] for c in columns] )

for i in range(len(songs)):
    s = Songs(id = songs[i][0], title = songs[i][1], danceability = songs[i][2], energy = songs[i][3], key = songs[i][4], loudness = songs[i][5], mode = songs[i][6], acousticness = songs[i][7], instrumentalness = songs[i][8], liveness = songs[i][9], valence = songs[i][10], tempo = songs[i][11], duration_ms = songs[i][12], time_signature = songs[i][13], num_bars = songs[i][14], num_sections = songs[i][15], num_segments = songs[i][16], classs = songs[i][17], rating = None)
    session.add(s)
session.commit()