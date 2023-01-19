from cs50 import SQL
from flask import Flask, redirect, render_template, request
from datetime import datetime


# Configuration and ensurin auto-reload
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQL("sqlite:///bucket.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add something to the bucketlist/watchlist/readlist
        name = request.form.get("name")
        type = request.form.get("type")
        db.execute("INSERT INTO bucketlist (name, type, status) VALUES(?, ?, ?)", name, type, "TO DO")
        print("check3")
        return redirect("/")

    else:
        return render_template("index.html")


        
@app.route("/bucket", methods=["GET"])
def bucket():
    if request.method == "GET":
        # Show the entire bucket list
        bucketlist = db.execute("SELECT * FROM bucketlist WHERE type='bucket'")
        return render_template("bucketlist.html", my_list=bucketlist)


@app.route("/watch", methods=["GET"])
def watch():
    if request.method == "GET":
        # Show the entire watch list
        watchlist = db.execute("SELECT * FROM bucketlist WHERE type='watch'")
        return render_template("bucketlist.html", my_list=watchlist)


@app.route("/read", methods=["GET"])
def read():
    if request.method == "GET":
        # Show the entire read list
        readlist = db.execute("SELECT * FROM bucketlist WHERE type='read'")
        return render_template("bucketlist.html", my_list=readlist)


@app.route("/task", methods=["GET"])
def task():
    if request.method == "GET":
        # Show the entire read list
        tasklist = db.execute("SELECT * FROM bucketlist WHERE type='task'")
        return render_template("bucketlist.html", my_list=tasklist)



@app.route("/done", methods=["POST"])
def done():
    # mark task as done
    id = request.form.get("id")
    date_to_print = datetime.today().strftime('%Y-%m-%d')
    db.execute("UPDATE bucketlist SET status = 'DONE', date = ?   WHERE id = ?", date_to_print ,id)
    list_type = db.execute("SELECT type FROM bucketlist WHERE id=?", id)[0]["type"]
    print(list_type)
    return redirect(f"/{list_type}")


@app.route("/undone", methods=["POST"])
def undone():
    # mark task as not done
    id = request.form.get("id")
    db.execute("UPDATE bucketlist SET status = 'TO DO', date = 'todayyy'   WHERE id = ?", id)
    list_type = db.execute("SELECT type FROM bucketlist WHERE id=?", id)[0]["type"]
    return redirect(f"/{list_type}")


@app.route("/delete", methods=["POST"])
def delete():
    # delate entry
    id = request.form.get("id")
    # first check type of entry before removing it from the database
    list_type = db.execute("SELECT type FROM bucketlist WHERE id=?", id)[0]["type"]
    db.execute("DELETE FROM bucketlist WHERE id = ?", id)
    return redirect(f"/{list_type}")
