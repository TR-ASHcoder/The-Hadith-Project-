# The Hadith Project (T.H.P)

The Hadith Project is a self run site that, using Flask, gives you a random hadith from
sahih bukhari, by just a click of a button.

- Very compact architecture
- Uses Python, HTML & CSS
- ⚡ Blazingly Fast ⚡

## Features

- Fetches random Hadith from an API
- Displays the Hadith along with its reference, narrator, and chapter
- Provides a button to fetch a new Hadith

## Files

- `flaskaroo.py`: The main Flask application that fetches Hadith data and renders the HTML page.
- `index.html`: The HTML template that displays the Hadith and provides a button to fetch a new one.
- `styles.css`: The CSS file for styling the HTML template.

## Installation

The T.H.P uses a [Python](https://www.python.org/) version 3.10 or above. Once you've installed Python and set it up
in the editor of your choice (we recommend [VsCode](https://code.visualstudio.com/)).

Required PIP installations are `flask` and `requests` the rest of the modules are already installed.
```
pip install flask
pip install requests
```

# Running The Hadith Project

To get into the website, you must run `flaskaroo.py` which will start the self-hosted website. Then, you will
see the local IP address it is running on. Copy that into your browser and the website should display.

Open your browser and navigate to: http://127.0.0.1:8080

Example of what you should see in the terminal: (The x's are your IP)
```bash
> PS flaskaroo.py
 * Serving Flask app 'flaskaroo'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://xxx.xxx.x.xx:8080
 ```
 
# License
This project is licensed under the MIT License - see the LICENSE file for details.
Authors: Trash (Developer), MAG (Readme creator)
 