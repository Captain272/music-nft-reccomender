# FeedBack
# ---------------------------------------------------------------------------------------------
# Use a feedback system to know how accurate are the recommended results with respeat to web2.
# ---------------------------------------------------------------------------------------------

from flask import Flask,render_template,redirect,request,url_for
import json
import collections
from web3 import Web3
import requests
import random

base_url = 'https://music-nft-recomender.herokuapp.com/'





vector=[]
preds=[]
top_preds=[]
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello():
    global vector
    global preds
    global top_preds
    # print(vector,preds)
    if len(vector) and len(preds):
        return render_template('index.html',top_preds=top_preds,preds=preds,preds_len=len(preds))
    elif request.method == 'POST':
         l=[]
         d={}
         track=request.form['track']
         music=request.form['music']
         duration=request.form['duration']
         l.append(2)
         l.append(track)
         l.append(music)
         l.append(duration)
         d["a"]=str(2)
         d["b"]=str(track)
         d["c"]=str(music)
         d["d"]=str(duration)
         vector=[l]
         print(vector,d)
         data=requests.post(base_url,json=d)
         result=data.json()
         top_preds=result['song_names_top']
         preds=result['song_names_alt']
        #  random.shuffle(preds)
         print(top_preds,preds)
         return render_template('index.html',top_preds=top_preds,preds=preds,preds_len=len(preds))       
    else:
        return render_template('index.html',top_preds=[],preds=[])
app.run(host='0.0.0.0', port=5000,debug=False)
# 4shLiTRdwhAJ1JW7GrNd8D5FRiWXJnuqFDddRn5gpQT8
# https://magiceden.io/item-details/4shLiTRdwhAJ1JW7GrNd8D5FRiWXJnuqFDddRn5gpQT8?name=Slumberville-%23164
# https://magiceden.io/item-details/4EtYS1jL6EmQKrVitngKksUXpmEM8xPgoC7nxN3759BZ?name=Dude-on-the-Dance-Floor-%23140
