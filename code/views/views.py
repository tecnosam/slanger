from flask.helpers import send_from_directory
from .. import app
from flask import url_for, redirect, render_template

@app.route("/")
def index_view():
    return render_template( "base.html" )

@app.route("/slangs")
def slangs_view():
    return render_template( "slangs.html" )

@app.route( "/profiles" )
def profiles_view():
    return render_template( "profiles.html" )

@app.route( "/comments" )
def comments_view():
    return render_template( "comments.html" )

@app.route("/crawler/logs")
def crawler_logs_view():
    return send_from_directory( "logs", "crawler.txt" )