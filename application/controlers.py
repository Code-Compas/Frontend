from flask import render_template,request,Flask
from flask import current_app as app
from application.models import *

b=dict()


@app.route("/",methods=["GET","POST"])
def f1():
    if request.method=="GET":
        return render_template("index.html")
    else:
        a=dict(request.form)
        for i in a:
            b[i]=a[i]
        if "login" in a:
            
            return render_template("form.html",a=b)
        else:
            if "submit" in a:
                return render_template("dumy.html",a=b)
            return render_template("form.html",a=b)

