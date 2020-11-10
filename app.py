from flask import Flask,  render_template, url_for, request, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "0748d28ecb03830a0acae6d1886c55ed"

products = [
    {
        "id": 0,
        "name": "Sample product 1",
        "company": "Sample Company 1",
        "price": 20,
    },
    {
        "id": 1,
        "name": "Sample product 2",
        "company": "Sample Company 2",
        "price": 69,
    },
    {
        "id": 2,
        "name": "Sample product 3",
        "company": "Sample Company 3",
        "price": 420,
    },
    {
        "id": 3,
        "name": "Sample product 4",
        "company": "Sample Company 4",
        "price": 50,
    },
    {
        "id": 4,
        "name": "Sample product 5",
        "company": "Sample Company 5",
        "price": 20,
    },
    {
        "id": 5,
        "name": "Sample product 6",
        "company": "Sample Company 6",
        "price": 69,
    },
    {
        "id": 6,
        "name": "Sample product 7",
        "company": "Sample Company 7",
        "price": 420,
    },
    {
        "id": 7,
        "name": "Sample product 8",
        "company": "Sample Company 8",
        "price": 50,
    }
]

  

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html", title="About")

@app.route("/contact/")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/product/<int:pid>")
def product(pid):
    return render_template("products.html", product=products[pid])

@app.route("/catalog/")
def catalog():
    return render_template("catalog.html", products=products)

@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        print("YERER")
        return f"Account created for {form.company.data}!"

    return render_template("register.html", title="Register", form=form)

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)