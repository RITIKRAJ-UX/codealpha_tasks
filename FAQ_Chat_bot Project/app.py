from flask import Flask, request, render_template_string
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

with open("faqs.txt", "r", encoding="utf-8") as f:
    data = f.read()

faq_pairs = data.strip().split("\n\n")

questions = []
answers = []

for pair in faq_pairs:
    q, a = pair.split("\n", 1)
    questions.append(q)
    answers.append(a)

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

HTML = """
<h2>FAQ Chatbot (Python Beginner)</h2>
<form method="post">
<input name="question" style="width:400px">
<input type="submit">
</form>
<p><b>Answer:</b> {{ answer }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        user_q = request.form["question"]
        user_vector = vectorizer.transform([preprocess(user_q)])
        similarity = cosine_similarity(user_vector, question_vectors)
        answer = answers[similarity.argmax()]
    return render_template_string(HTML, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
