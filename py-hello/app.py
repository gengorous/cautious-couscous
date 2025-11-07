from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, Flask world!"
@app.get("/health")
def health():
    return {"status": "ok"}  # JSONが返る


if __name__ == "__main__":
    app.run(debug=True)

