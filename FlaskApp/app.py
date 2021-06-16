from flask import Flask, render_template, request
import joblib
from nlp_preprocess import NLPpreprocess

model = joblib.load(r"C:\Users\straw\Desktop\AIS\ProjectPool 2\Roue-des-emotions\Output\Models\nlp_models.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        sentence = request.form['sentence']
        p_sentence = NLPpreprocess(sentence)
        prediction = model.predict([p_sentence.lemmas])[0]
        return render_template('result.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)