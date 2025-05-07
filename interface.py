from flask import Flask,request,jsonify
import config
from Project.utils import Medical_insurance
import numpy as np


app = Flask(__name__)
@app.route("/")
def get_home():
    return "Hello we are wiring API"

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance():
    if request.method == "POST" :
        data = request.form
        print("user data",data)
        age = eval(data["age"])
        gender =  data["gender"]
        bmi = eval (data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_ob = Medical_insurance(age,gender,bmi,children,smoker,region)
        charge = med_ob.get_predict_price()
        return jsonify({"Result": f"prdicted charges is  {charge[0]}"})

        
                   

                   





if __name__ == "__main__" :
    app.run()
