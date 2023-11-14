from flask import Flask,render_template,request,redirect,url_for
from responce import prediction 

app = Flask(__name__)

@app.route('/',methods=["post",'get'])
def index():
    if request.method=='POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form.get('exang', '0'))
        oldpeak = float(request.form['oldpeak'])  
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        test=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        ans=prediction([test])
        
        return render_template('update.html',ans=ans)
    return render_template('index.html')

if __name__ == '__main__':


    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)
