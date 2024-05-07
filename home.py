from flask import Flask,render_template,request,url_for

app=Flask(__name__)


@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/")
@app.route("/home")
def home():
    return render_template("page1.html")

if __name__=="__main__":
    app.run(debug=True)