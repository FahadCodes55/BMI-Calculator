from flask import Flask, render_template, request
app = Flask(__name__, template_folder="template")


@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = 0
    if request.method == "POST":
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        bmi = calc_bmi(weight, height)
    return render_template("bmi.html", bmi=bmi)


def calc_bmi(weight, height):
    return round(weight / (height/100) ** 2, 2)


if __name__ == '__main__':
    app.run(debug=True)
