from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "corriendo el servidor base"

if __name__ == '__main__':
    app.run(debug=True, port=3000)