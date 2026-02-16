## how to integrate HTML with Flask web page

from flask import Flask, render_template


app=Flask(__name__)

@app.route("/")  ## route decorator to tell flask what url should trigger our function
def Welcome_message():
    return "<html><H1>Welcome to Flask Framework. This is a best and simple Flask application.</H1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)