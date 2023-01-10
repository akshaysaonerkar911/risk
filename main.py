from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

model = pickle.load(open("iris.pkl","rb"))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/iris",methods=["GET","POST"])
def iris():
    sepal_length=float(request.form.get("sepal length (cm)"))
    sepal_width=float(request.form.get("sepal width (cm)"))
    petal_length=float(request.form.get("petal length (cm)"))
    petal_width=float(request.form.get("petal width (cm)"))


    result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])

    outcome = result[0]
    if outcome==0:
        return "setosa"
    elif outcome==1:
        return "versicolour"
    else:
        return "versinica"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)