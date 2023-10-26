from flask import Flask, request, jsonify
import random
data= {
    'f_name':{'first_name': 'Artur',},
    'l_name':{'last_name': 'Ziianbaev',},
    'age':{'current_age': '22',},
    'date_of_birth': {"day":"23","month":"January","year":"2001","_full_date":"01/23/2001"}
}

FACTS_ABOUT_ME=[
    "I do not have any tattoos",
    "I tried alcohol at the age of 12 for the first time (quite by chance xD; Don't think that I am an alcoholic person)",
    "I used to play soccer for 15 years",
    "I've been going to the gym for 6 years",
    "I have a younger brother. He is 10 years old",
    "I've read 5 books during the previous year",
    "I lived in Ohio for 18 months"
]

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"


@app.route("/first_name")
def give_first_name():

    return jsonify(data['f_name']),200

@app.route("/last_name")
def give_last_name():

    return jsonify(data['l_name']),200

@app.route("/date_of_birth")
def show_date_of_birth():
    return jsonify(data['date_of_birth']),200

@app.route("/age")
def show_age():

    return jsonify(data['age']),200

@app.route("/personal_info")
def show_full_info():
    return jsonify(data),200

#random facts
@app.route("/random_fact")
def show_random_fact():
    random_fact=random.choice(FACTS_ABOUT_ME)
    response={
        "random_fact": random_fact
    }
    return response



if __name__ == "__main__":
    app.run(debug=True)
