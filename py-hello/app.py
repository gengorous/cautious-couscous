from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
<<<<<<< HEAD
    return "Hello from main branch!"
=======
    return "Hello from branch A!"
>>>>>>> feature/conflict-A

if __name__ == "__main__":
    app.run(debug=True)



