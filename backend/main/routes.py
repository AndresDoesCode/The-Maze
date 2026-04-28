from main import app

@app.route("/")
def hello():
    print("Hello!")
    return "Hi there!"