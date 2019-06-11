from flask import Flask, render_template, redirect, request
from mysql import connectToMySQL      # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('pets')             # call the function, passing in the name of our db
    pets = mysql.query_db('SELECT * FROM pets;')     # call the query_db function, pass in the query as a string
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/add_pet", methods=["POST"])
def add_pet():
    mysql = connectToMySQL('pets')
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        "name": request.form["name"],
        "type": request.form["type"]
    }
    id = mysql.query_db(query,data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
