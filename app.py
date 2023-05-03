#calc folder
from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a + b

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a - b

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a * b

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = a/b

    return str(result)

# PART TWO

    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)