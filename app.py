from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS
from chat_module import get_resp
msg = ""
app = Flask(__name__)
#CORS(app)


@app.get("/")
def get_index():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_resp(text)
    message = {"answer": response}
    return jsonify(message)
    

if __name__ == "__main__": app.run();