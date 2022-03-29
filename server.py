from flask import Flask, render_template, redirect,request,session


app = Flask(__name__)
app.secret_key = "yeah i guess this is top secret"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    count = 0
    print(request.form)
    session["firstname"] = request.form["first_name"]
    session["lastname"] = request.form["last_name"]
    session["emailid"] = request.form["email"]
    session["bought_strawberry"] = request.form["strawberry"]
    session["bought_raspberry"] = request.form["raspberry"]
    session["bought_apple"] = request.form["apple"]
    return redirect("/show")




@app.route('/show')
def show():
    return render_template('checkout.html',fname_on_template = session["firstname"],
    lname_on_template = session["lastname"],email_on_template = ['emailid'],strawberry_on_template = ['bought_strawberry'],
    raspberry_on_template = ["bought_raspberry"], apple_on_template = ["bought_apple"])





if __name__=='__main__': 
    app.run(debug=True)