from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Deployed!</h1><style>body { display: flex; align-items: center; justify-content: center; height: 100vh; }</style>'
if __name__ == "__main__":
    # Run the Flask app on the public IP address of your server
    app.run(host='130.162.188.246', port=8000)