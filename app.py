from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def first_webpage():

    name="Flask"
    return render_template('index.html',index_variable=name)

@app.route("/flask_2")
def second_flask():
    return "Python is fun!"

#run using debug argument
app.run(debug=True)
