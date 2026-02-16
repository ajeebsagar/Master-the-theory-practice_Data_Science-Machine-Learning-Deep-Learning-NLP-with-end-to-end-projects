### buliding url dynamically
## jinja 2 templete engine


''''
{{ }}  expresssion to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

## variable rule

## HTTP get and post


## Http is four type 1 get, 2. post, 3.put, 4.delete 

## how to integrate HTML with Flask web page

from flask import Flask, render_template, request, redirect, url_for


app=Flask(__name__)

@app.route("/")  ## route decorator to tell flask what url should trigger our function
def Welcome_message():
    return "<html><H1>Welcome to Flask Framework.</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')




## variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAILed"
    return render_template('results.html',results=res)        
    return "The marks you got is "+(score)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAILed"

    exp={'score':score,"res":res}  
    return render_template('results1.html',results=exp)      
## if condition
@app.route('/successif/<int:score>')
def successif(score):
   
    return render_template('results.html',results=score)   
    
@app.route('/fail/<int:score>')
def fail(score):
    
    return render_template('results1.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)