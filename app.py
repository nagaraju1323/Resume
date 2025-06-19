from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")




@app.route('/objective')
def objective():
    return render_template("objective.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/certificates')
def certificates():
    return render_template("certificates.html")

@app.route('/languages')
def languages():
    return render_template("languages.html")

if __name__ == '__main__':
    app.run(debug=True)
