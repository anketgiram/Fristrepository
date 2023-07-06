from flask import Flask

app = Flask(__name__)


@app.route("/")   # decorator
def welcome():
    return "Welcome to home page"


@app.route("/predict_sepal_Length")    #api and endpoint
def predict_sepal_Length():
    return "Predict sepal Length"


@app.route("/predict_species")    #api and endpoint
def predict_species():
    return "predict species "



@app.route("/predict_petal_width")    #api and endpoint
def predict_petal_width():
    return "predict petal width"


@app.route("/car_price_pridction", methods = ["POST"])    #api and endpoint
def car_price_pridction():
    return "car price pridction"

if __name__ == "__main__":
    app.run(debug=True)    




