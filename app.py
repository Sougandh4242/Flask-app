from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client.flask_database
todos = db.todos

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route("/<id>/delete/", methods=['POST'])
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
