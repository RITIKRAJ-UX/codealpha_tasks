from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

with open("faqs.txt", "r") as file:
    data = file.read()

faq_blocks = data.strip().split("\n\n")

questions = []
answers = []

for block in faq_blocks:
    q, a = block.split("\n")
    questions.append(q)
    answers.append(a)

stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    return " ".join([w for w in tokens if w.isalpha() and w not in stop_words])

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

while True:
    user_question = input("\nAsk a question (type 'exit' to quit): ")
    if user_question.lower() == "exit":
        break

    processed_user = preprocess(user_question)
    user_vector = vectorizer.transform([processed_user])

    similarity = cosine_similarity(user_vector, question_vectors)
    best_index = similarity.argmax()
    score = similarity[0][best_index]

    if score > 0.2:
        print("Answer:", answers[best_index])
    else:
        print("Sorry, I don't understand your question.")
