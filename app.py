from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace the database credentials with your actual values
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "loki",
    "database": "flask",
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["pwd"]
        gender = request.form["gender"]

        # Insert data into the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "INSERT INTO login (name, email, password, gender) VALUES (%s, %s, %s, %s)"
        data = (name, email, password, gender)

        try:
            cursor.execute(query, data)
            connection.commit()
            message = "signed Successfully"
        except mysql.connector.Error as err:
            connection.rollback()
            message = f"Error: {err}"
        finally:
            cursor.close()
            connection.close()

        return render_template("prac.html", message=message)

    return render_template("prac.html")

if __name__ == "__main__":
    app.run(debug=True)