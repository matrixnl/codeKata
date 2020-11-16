from flask import Flask
import os
app = Flask('codeKata')


@app.route("/")
def index():
    return true

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
