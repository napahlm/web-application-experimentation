from flask import Flask

app = Flask(__name__)

@app.route("/")                     # decorator to connect URL endpoints

def index():                        # Activates when the specified URL endpoint is requested by user
    return("Web app deployed.")

def fahrenheit_from(celsius):
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return("Invalid input")


if __name__ == "__main__":
    celsius = input("Celsius: ")
    print("Fahrenheit: ", fahrenheit_from(celsius))
    app.run(host="127.0.0.1", port=8080, debug=True)