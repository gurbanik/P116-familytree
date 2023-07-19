# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Gurbani" # write your name
    age = "14" # write your age
    relation = "me"

    return render_template('index.html' , name = name , age = age, relation = relation)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Gurjeet"
    age = "46"
    relation = "father"

    return render_template('father.html' , name = name , age = age, relation = relation)


# define the route to mother webpage
@app.route("/mother")
def mother():

    name = "Gurvinder"
    age = "46"
    relation = "mother"

    return render_template('mother.html' , name = name , age = age, relation = relation)


# define the route to friends webpage
@app.route("/friend")
def friend():

    name = "Navneet"
    age = "14"
    relation = "friend"

    return render_template('friend22.html' , name = name , age = age, relation = relation)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)