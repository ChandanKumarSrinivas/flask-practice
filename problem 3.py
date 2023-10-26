from flask import Flask
app=Flask(__name__)

@app.route("/blog/<int:postID>")
def show_blog(postID):
    return 'Blog number is %s' %postID

@app.route("/rev/<float:revNo>")
def revision(revNo):
    return 'Revision number  is %s' %revNo

@app.route("/name/<usrName>")
def show_name(usrName):
    return "User name given is: %s" %usrName

@app.route("/")
def hello():
    return "Hello World!"


if __name__=="__main__":
    app.run()