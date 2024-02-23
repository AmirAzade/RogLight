from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/button/<int:button_id>")
def button_click(button_id):
    if button_id == 0:
        os.system("rogauracore black")
    elif button_id == 1:
        os.system("rogauracore red")
    elif button_id == 2:
        os.system("rogauracore green")
    elif button_id == 3:
        os.system("rogauracore blue")
    elif button_id == 4:
        os.system("rogauracore yellow")
    elif button_id == 5:
        os.system("rogauracore gold")
    elif button_id == 6:
        os.system("rogauracore cyan")
    elif button_id == 7:
        os.system("rogauracore magenta")
    elif button_id == 8:
        os.system("rogauracore rainbow")
    elif button_id == 9:
        os.system("rogauracore white")

    return "Button clicked"


@app.route("/radio/<int:option_number>")
def radio_selected(option_number):
    if option_number == 1:
        os.system("rogauracore brightness 1")
    elif option_number == 2:
        os.system("rogauracore brightness 2")
    elif option_number == 3:
        os.system("rogauracore brightness 3")

    return "Option selected"


@app.route("/color", methods=["POST"])
def color_selected():
    color = request.form["color"]
    os.system("rogauracore single_static " + color[1:])
    
    return "Color selected"


if __name__ == "__main__":
    app.run(debug=True)
