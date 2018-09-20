from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Mr-T','last_name' : 'Barracas'},
        {'first_name' : 'Al','last_name' : 'Pacino'},
        {'first_name' : 'Tony','last_name' : 'Montana'},
        {'first_name' : 'Keyser','last_name' : 'Soze'},
        {'first_name' : 'Wonder','last_name' : 'Woman'}



    ]

    return render_template("index.html", title="Users Table", user=users)
if __name__=="__main__":
    app.run(debug=True)
