from flask import Flask, render_template, request
import joblib

model = joblib.load(r"C:\Users\straw\Desktop\AIS\ProjectPool 2\Roue-des-emotions\Output\Models\nlp_models.pkl")

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        #return render_template('prediction.html')
        return "<h3>No sailors to display for this query...</h3>"
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)