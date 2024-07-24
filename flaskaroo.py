from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

def get_hadith():
  url = "https://random-hadith-generator.vercel.app/bukhari/?data="
  response = json.loads(requests.request("GET", url).text) 
  hadith = response['data']['hadith_english']
  fact = response['data']['refno']
  narr = response['data']['header']
  chap = response['data']['chapterName']
  return hadith, fact, narr, chap
  
@app.route('/')
def index():
    hadith, fact, narr, chap = get_hadith()
    return render_template("index.html", hadith = hadith, fact = ref, narr = narr, chap = chap)
 
app.run(host="0.0.0.0", port=8080)
