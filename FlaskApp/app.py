from flask import Flask, render_template
import joblib

model = joblib.load(r"C:\Users\straw\Desktop\AIS\ProjectPool 2\Roue-des-emotions\Output\Models\nlp_models.pkl")

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)