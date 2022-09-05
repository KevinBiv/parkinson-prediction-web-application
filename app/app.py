from flask import Flask,render_template,request
import MLAppPredict as ml

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html' ,name='kevin')
  

@app.route('/predictionpage',methods=['GET','POST'])
def predict():

#   shimmer=request.form['shimmer']
    shimmer = request.form.get("shimmer", False)
    mdvp=request.form.get('mdvp', False)
    shd=request.form.get('shd', False)
    nhr=request.form.get('nhr', False)
    hnr=request.form.get('hnr', False)
    mdvpfhi=request.form.get('mdvpfhi', False)
    mdvpflo=request.form.get('mdvpflo', False)
    prediction=ml.prediction(shimmer,mdvp,shd,nhr,hnr,mdvpfhi, mdvpflo)
    if prediction==0:
        predict='YOU DONT HAVE PARKINSON'
    else:
        predict='YOU HAVE PARKINSON'     
  
    return render_template('predictionpage.html' ,predicte=predict)

   
if __name__=="__main__":
    app.run(debug=True)    
