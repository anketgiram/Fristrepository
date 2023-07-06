from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)
model = pickle.load(open("linear_model.pkl", "rb"))


@app.route("/")   # decorator
def status():
    return jsonify({"Message" : "Status is active"})


@app.route("/predict_sepal_Length", methods = ["POST"])    #api and endpoint
def predict_sepal_Length():
    data = request.get_json()
    print(data)
    SepalWidthCm = data["SepalWidthCm"]
    print("SepalWidthCm",SepalWidthCm)
    PetalLengthCm = data["PetalLengthCm"]
    print("PetalLengthCm",PetalLengthCm)
    PetalWidthCm = data["PetalWidthCm"]
    print("PetalWidthCm",PetalWidthCm )
    Species = data["Species"]
    print("Species", Species)

    if Species == "Iris-setosa" :
        Species = 0
    elif Species == "Iris-versicolor" :
        Species = 1
    elif Species == "Iris-virginica" :
        Species = 2

    print("Encoding Species",Species)        

    test_array = [SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]
    prediction = model.predict([test_array])
    prediction

    return jsonify({'Predicted Sepal Length': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)    




