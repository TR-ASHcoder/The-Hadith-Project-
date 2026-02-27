from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_hadith():
    page = random.randint(1, 757)
    url = f"https://hadithapi.pages.dev/api/bukhari?page={page}"
    response = requests.get(url).json()
    

    filtered = [h for h in response['results'] if 100 <= len(h['hadith_english']) <= 500]
    
 
    if not filtered:
        return get_hadith()
    
    item = random.choice(filtered)
    
    hadith = item['hadith_english']
    fact = item['refno']
    narr = item['header']
    chap = item['chapterName']
    
    return hadith, fact, narr, chap

@app.route('/')
def index():
    hadith, fact, narr, chap = get_hadith()
    return render_template("index.html", hadith=hadith, fact=fact, narr=narr, chap=chap)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)


# made by TR ASH