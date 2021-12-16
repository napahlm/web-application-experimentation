from flask import Flask, request

app = Flask(__name__)

# This is used to route data. Here "int" is specified. Returns error if anything else.
@app.route("/")
def index():
    celsius = request.args.get("celsius", "")

    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius: <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )

def fahrenheit_from(celsius):
    "C to F"
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)