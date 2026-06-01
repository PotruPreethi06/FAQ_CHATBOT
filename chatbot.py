import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stopwords = {
    'a','about','above','after','again','against','all','am','an','and','any','are','as','at',
    'be','because','been','before','being','below','between','both','but','by',
    'could','did','do','does','doing','down','during',
    'each','few','for','from','further',
    'had','has','have','having','he','her','here','hers','herself','him','himself','his','how',
    'i','if','in','into','is','it','its','itself',
    'just',
    'me','more','most','my','myself',
    'no','nor','not','now',
    'of','off','on','once','only','or','other','our','ours','ourselves','out','over','own',
    'same','she','should','so','some','such',
    'than','that','the','their','theirs','them','themselves','then','there','these','they','this','those','through','to','too',
    'under','until','up','very',
    'was','we','were','what','when','where','which','while','who','whom','why','with','would',
    'you','your','yours','yourself','yourselves'
}

# FAQ Questions and Answers
faq_data = {
    "What is artificial intelligence?":
        "Artificial Intelligence is the simulation of human intelligence by machines.",

    "What is machine learning?":
        "Machine Learning is a subset of AI that enables systems to learn from data.",

    "What is deep learning?":
        "Deep Learning uses neural networks with multiple layers to learn patterns.",

    "What is Python?":
        "Python is a high-level programming language used in web development, AI, and data science.",

    "Who developed Python?":
        "Python was developed by Guido van Rossum in 1991.",

    "What is NLP?":
        "Natural Language Processing enables computers to understand human language.",

    "What is data science?":
        "Data Science is the field of extracting knowledge and insights from data."
}

# Preprocessing Function
def preprocess(text):
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)

    words = [
        word for word in words
        if word not in string.punctuation
        and word not in stopwords
    ]

    return " ".join(words)

# Prepare Questions
questions = list(faq_data.keys())
processed_questions = [preprocess(q) for q in questions]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot Function
def chatbot(user_query):
    processed_query = preprocess(user_query)

    query_vector = vectorizer.transform([processed_query])

    similarity_scores = cosine_similarity(
        query_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    if best_score > 0.3:
        return faq_data[questions[best_match_index]]
    else:
        return "Sorry, I couldn't find a relevant answer."

# Main Chat Loop
print("===== FAQ CHATBOT =====")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot(user_input)
    print("Bot:", response)
