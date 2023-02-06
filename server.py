from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    ano_actual = datetime.datetime.now().year
    return render_template("index.html", num=random_number, fecha=ano_actual)
if __name__ == "__main__":
    app.run(debug=True)