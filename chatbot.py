# Knowledge base for the Python chatbot
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
knowledge_base = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level programming language known for its simple syntax."
    },
    {
        "question": "What is a variable?",
        "answer": "A variable is a name used to store or refer to a value."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning enables computers to learn patterns from data."
    },
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial intelligence enables machines to perform tasks that typically require human intelligence."
    },
    {
        "question": "What is a function in Python?",
        "answer": "A function is a reusable block of code designed to perform a specific task."
    },
    {
        "question": "What is deep learning?",
        "answer": "Deep learning is a branch of machine learning that uses neural networks with multiple layers to learn complex patterns."
    },
    {
        "question": "What is data science?",
        "answer": "Data science combines statistics, programming, and domain knowledge to extract insights from data."
    },
    {
        "question": "What is a list in Python?",
        "answer": "A list is an ordered, mutable collection of items in Python."
    },
    {
        "question": "What is a loop in Python?",
        "answer": "A loop repeats a block of code while a condition holds or for each item in a sequence."
    },
    {
        "question": "What is a neural network?",
        "answer": "A neural network is a computing model inspired by interconnected neurons in the human brain."
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning trains a model using labeled examples containing inputs and expected outputs."
    },
    {
        "question": "What is unsupervised learning?",
        "answer": "Unsupervised learning identifies patterns and structures in data without labeled outputs."
    },
    {
        "question": "What is natural language processing?",
        "answer": "Natural language processing enables computers to analyze, understand, and generate human language."
    },
    {
        "question": "What is a dataset?",
        "answer": "A dataset is a collection of related data organized for analysis or processing."
    },
    {
        "question": "What is a Python dictionary?",
        "answer": "A Python dictionary stores data as key-value pairs."
    }
]


# Extract all questions from the knowledge base
questions = [item["question"] for item in knowledge_base]

# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_question, threshold=0.65):
    if not user_question.strip():
        return "Please enter a question.", 0.0

    # Convert the user's question into TF-IDF
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity with stored questions
    similarities = cosine_similarity(
        user_vector, question_vectors
    ).flatten()

    # Find the best match
    best_index = int(np.argmax(similarities))
    best_score = float(similarities[best_index])

    # Reject questions with low similarity
    if best_score < threshold:
        return "Sorry, I don't know the answer to that question.", best_score

    # Extract meaningful words
    analyzer = vectorizer.build_analyzer()
    user_words = set(analyzer(user_question))
    matched_words = set(analyzer(questions[best_index]))

    # Require at least one shared meaningful word
    if not user_words.intersection(matched_words):
        return "Sorry, I don't know the answer to that question.", best_score

    # Return exactly two values
    return knowledge_base[best_index]["answer"], best_score


