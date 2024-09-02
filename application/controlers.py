from flask import render_template,request,Flask
from flask import current_app as app
from application.models import *




@app.route("/",methods=["GET","POST"])
def f1():
    if request.method=="GET":
        return render_template("index.html")
    else:
        a=dict(request.form)
        return render_template("form.html")