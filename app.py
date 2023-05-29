
from flask import *
import mysql.connector
from face import *
from emotions import *
from recording import *



app=Flask(__name__)
usr=['prat' ]
pwd=['prat1008']
mydb = mysql.connector.connect(host="localhost", user="root", password='Mouse@2010', database="the_sweet_spot")
cur= mydb.cursor()
def validate():
    presence, name = face_detection()
    return presence, name

@app.route("/", methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        for i in range(len(usr)):
            if usr[i]==username and pwd[i] ==password:
                global name
                presence, name = validate()
                if presence==True and usr[i].lower()==name.lower():
                    return redirect(url_for("home"))
    return render_template("html/index.html")

@app.route("/home", methods=['GET', 'POST'])
def home():
    cur.execute("SELECT * FROM entry")
    sentiments=[]
    time=[]
    for i in cur:
        sentiments.append(i[1])
        time.append(i[0])

    if request.method=='POST':
        seconds=request.form['seconds']
        emo, time_rn = record(seconds, 'PRAT')
        print(emo, time_rn)
        query='INSERT INTO entry(date,Mood) values(%s,%s)'
        data=(str(time_rn), emo)
        cur.execute(query,data)
        mydb.commit()
    return render_template("html/home.html", zip=zip(sentiments,time))

@app.route("/text", methods=['GET', 'POST'])
def text():
    if request.method=='POST':
        text=request.form['text']
        emo, time_rn = text_emo(text)
        print(emo, str(time_rn))
        query='INSERT INTO entry(date,Mood) values(%s,%s)'
        data=(str(time_rn), emo)
        cur.execute(query,data)
        mydb.commit()
    return render_template('html/text.html')

if __name__ == "__main__":
    app.run(debug=True)