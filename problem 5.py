from flask import Flask
app=Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" %name

@app.route("/login", method = ["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form("nm")
        return redirect(url_for('success',name = user))
    else:
        user=request.arg.get("nm")
        return redirect(url_for("success",name=user))

if __name__=="__main__":
    app.run()