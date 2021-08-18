from flask import Flask, request
from sub_controller import sub_page

flask_application = Flask(__name__)
flask_application.register_blueprint(sub_page)


@flask_application.route("/")
def home():
    print(request.headers)
    return "Hello Flask!"
