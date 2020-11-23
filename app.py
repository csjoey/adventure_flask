from flask import Flask

app = Flask(__name__)

app.secret_key = ***

# Dr. Bart added this: It imports my views
import views


if __name__ == '__main__':
    app.run(debug=True, reloader=True)
