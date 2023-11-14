from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:number>')
def success(number):

    res=""
    if number>=50:
        res="PASS"
    else:
        res="FAIL"
    exp = {'score':number, 'result':res}

    return render_template('result.html', result=exp)

@app.route('/submit',methods=['POST','GET'])
def result():

    total_score=0.0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        hindi = float(request.form['hindi'])
        english = float(request.form['english'])

    total_score = (science + maths + hindi + english)/4;
    return redirect(url_for('success',number=total_score))

if __name__=='__main__':
    app.run(debug=True)