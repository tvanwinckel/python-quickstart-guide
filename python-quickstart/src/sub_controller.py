from flask import Blueprint

sub_page = Blueprint("sub-controller", __name__)

@sub_page.route("/sub")
def hello_world():
    return "hello world from sub-controller"
