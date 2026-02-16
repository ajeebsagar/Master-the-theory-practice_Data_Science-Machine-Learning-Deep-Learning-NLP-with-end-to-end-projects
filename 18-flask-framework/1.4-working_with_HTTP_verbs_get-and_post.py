## HTTP get and post


## Http is four type 1 get, 2. post, 3.put, 4.delete 

## how to integrate HTML with Flask web page

from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/")  ## route decorator to tell flask what url should trigger our function
def Welcome_message():
    return "<html><H1>Welcome to Flask Framework. This is a best and simple Flask application.</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
        pass
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
        pass
    return render_template('submit.html')

if __name__=="__main__":
    app.run(debug=True)