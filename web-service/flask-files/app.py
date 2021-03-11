import time
import psycopg2 as psg
from flask import Flask, redirect, url_for, render_template, request, session , flash

app = Flask(__name__)
conn = psg.connect("host='localhost' dbname='docker' user='docker' password='docker'")
cur = conn.cursor()

@app.route('/')
def index():
	cur.execute("SELECT * FROM teste")
	result = cur.fetchall()
	return render_template("index.html",dados=result)
