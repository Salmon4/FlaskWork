from flask import Flask, render_template
app = Flask(__name__)
#print("Printing this in the flask console")
@app.route("/")
def hello_world():
  print(__name__)
  return  "Call me king, cuz I be k"

#@app.route("/static/template.html")
#def template():
#    x = [0,1,1,2,3,5,8]
#    return "coll = " + str(x)

@app.route("/static/templates/template/.html")
def test_tmplt():
    col = [0,1,1,2,3,5,8]
    return render_template(
        'template.html',
        foo="fooooo",
        collection=col
    )


if __name__ == "__main__":
  app.debug = True
  app.run()
