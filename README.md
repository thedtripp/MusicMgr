# MusicMgr

## How To Run
0. [Optional] demo app at:
```
https://musicmgr.herokuapp.com/
```

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ source env/bin/activate
```

3. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

4. Run the `json2sqlite.py` script to generate the playlist database:
```
$ (env) python json2sqlite.py
```

5. Start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

## Usage

### List:
By default, the application presents a paginated table of songs.
Click the `Display All` button to return to this view.

### Search:
List all attributes of the song matching the search term.
Search is case sensitive.

### Rate:
Provide a star rating for your songs so you know what you like (and what you don't).
Accepts an integer from [0, 5].
Floats will be truncated.