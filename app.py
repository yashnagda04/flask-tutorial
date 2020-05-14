from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!!'

@app.route('/home')
def greetUser():
    return render_template('home.html')

@app.route('/test',methods=['GET', 'POST'])
def calculateResult():
    if request.method == 'POST':
        height=request.form['height']
        message=''
        if height == '8848':
            message="Your Answer:"+height+"\nYou have passed the test,Keep it up."
        else:
            message="Your Answer:"+height+"\nYou have failed the test, keep trying."

        return render_template('test.html', message=message) 
    else:
        return render_template('test.html', message='')

if __name__ == "__main__":
    app.run(debug=True)