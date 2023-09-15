import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Load NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Sample knowledge base (you can expand this)
knowledge_base = {
    "tell me about yourself": "I am a software developer with 5 years of experience...",
    "what is your greatest strength": "My greatest strength is my problem-solving ability...",
    "what is your experience with Python": "I have extensive experience with Python...",
}

# Function to preprocess and clean text
def preprocess_text(text):
    # Tokenize text
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]

    return " ".join(words)

# Function to find the best-matching question
def find_best_match(user_question, knowledge_base):
    user_question = preprocess_text(user_question)
    best_match = None
    highest_similarity = 0

    for question, answer in knowledge_base.items():
        question = preprocess_text(question)
        similarity = nltk.edit_distance(user_question, question)
        if similarity > highest_similarity:
            best_match = answer
            highest_similarity = similarity

    return best_match

# Main loop
while True:
    user_question = input("You: ")
    if user_question.lower() == "exit":
        print("AI Interview Assistant: Goodbye!")
        break

    response = find_best_match(user_question, knowledge_base)
    if response:
        print("AI Interview Assistant:", response)
    else:
        print("AI Interview Assistant: I'm sorry, I don't have an answer for that question.")
