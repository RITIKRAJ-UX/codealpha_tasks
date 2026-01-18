import tkinter as tk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- LOAD FAQ DATA ----------------
with open("faqs.txt", "r", encoding="utf-8") as f:
    data = f.read()

faq_pairs = data.strip().split("\n\n")

questions = []
answers = []

for pair in faq_pairs:
    q, a = pair.split("\n", 1)
    questions.append(q)
    answers.append(a)

# ---------------- PREPROCESS ----------------
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

# ---------------- CHAT FUNCTION ----------------
def chatbot_reply():
    user_input = entry.get()
    entry.delete(0, tk.END)

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    user_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_processed])

    similarity = cosine_similarity(user_vector, question_vectors)
    best_match = similarity.argmax()

    chat_area.insert(tk.END, "Bot: " + answers[best_match] + "\n\n")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("FAQ Chatbot - Python Beginner")

chat_area = tk.Text(root, height=20, width=70)
chat_area.pack()

entry = tk.Entry(root, width=60)
entry.pack(side=tk.LEFT, padx=10)

send_btn = tk.Button(root, text="Send", command=chatbot_reply)
send_btn.pack(side=tk.RIGHT)

root.mainloop()
