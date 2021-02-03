from flask import Flask, render_template, request
import pickle
import numpy as np

#import the machine learning model
mod=pickle.load(open("age_marriage.pkl","rb" ))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('new.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = int(request.form['gender'])
    data2 = int(request.form['religion'])
    data3 = int(request.form['caste'])
    data4 = int(request.form['mother_tongue'])
    data5 = int(request.form['country'])
    data6 = int(request.form['height'])
    arr = np.array([[data1,data6, data2, data3, data4,data5]])
    predd= mod.predict(arr)
    pred_int=int(round(predd[0]))
    years=pred_int+int(request.form['yob'])
  
   
    return render_template('new.html', pred="Predicted Marriage Age(Year):-"+str(pred_int)+"("+str(years)+")")


if __name__ == "__main__":
    app.run(debug=True)















