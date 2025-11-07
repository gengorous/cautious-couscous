from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, Flask world!"
@app.get("/health")
def health():
    return {"status": "ok"}  # JSONが返る
@app.get("/greet/<name>")
def greet(name):
    return f"Hello, {name}! Nice to meet you!"

if __name__ == "__main__":
    app.run(debug=True)



