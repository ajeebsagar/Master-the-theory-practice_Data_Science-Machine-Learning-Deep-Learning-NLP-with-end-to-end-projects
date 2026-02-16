from flask import  Flask

''''
it creats an instance of Flask class,
which is the WSGI application.
'''

## WSGI application
app=Flask(__name__)

@app.route("/")  ## route decorator to tell flask what url should trigger our function
def Welcome_message():
    return "Welcome to Flask Framework. This is a best and simple Flask application."


if __name__=="__main__":
    app.run(debug=True)  ## run the application in debug mode

