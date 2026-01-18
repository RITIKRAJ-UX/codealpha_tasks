import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

with open("faqs.txt", "r") as file:
    text = file.read()

text = text.lower()
tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_tokens = []
for word in tokens:
    if word not in stop_words and word.isalpha():
        filtered_tokens.append(word)

clean_text = " ".join(filtered_tokens)
print("Clean Text:")
print(clean_text)
