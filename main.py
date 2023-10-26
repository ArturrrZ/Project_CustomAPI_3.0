from flask import Flask, request, jsonify

data= {
    'f_name':{'first_name': 'Artur',},
    'l_name':{'last_name': 'Ziianbaev',},
    'age':{'current_age': '22',},
    'date_of_birth': {"day":"23","month":"January","year":"2001","_full_date":"01/23/2001"}
}

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

if __name__ == "__main__":
    app.run(debug=True)