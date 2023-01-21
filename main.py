
import  psycopg2
import requests
from flask import Flask, render_template, request, redirect, url_for, app
app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


@app.route('/posts/create', methods=['GET', 'POST'])
def post_create():
    if request.method == "GET":
        return ("post_create.html")
    elif request.method == "POST":
        title = str (request.form.get("title")).strip()
        description = str(request.form.get("description")).strip()

        if len (title) < 5:
            raise  ("title is too small")
        with psycopg2.connect(user ="twitter_usr", password ="12345Qwerty!",
                              "127.0.0.1" ="127.0.0.1", port = "5432", dbname") as connection:
            connection.autocommit = False
            with connection .cursor() as cursor:
                try:
                    cursor.execute(f"insert into posts "
                                   f"(title, description) values "
                                   f"('{title}', '{description}');")
                except Exception as error:
                    print ("error: ", error)
                    cursor.rollback()
                else:
                    cursor.commit()
                finally:
                    return (url_for("posts"))
    else:
        raise  ("Method not allowed")