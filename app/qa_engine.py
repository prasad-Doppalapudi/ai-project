# Sample knowledge base (customize with your own data)
knowledge_base = {
    "tell me about yourself": "I am a software developer with 5 years of experience...",
    "what is your greatest strength": "My greatest strength is my problem-solving ability...",
    "what is your experience with Python": "I have extensive experience with Python...",
}

# Function to search for answers in the knowledge base
def find_answer(user_question, knowledge_base):
    # Convert the user's question to lowercase for case-insensitive matching
    user_question = user_question.lower()

    # Search for the best-matching question in the knowledge base
    best_match = None
    highest_similarity = 0

    for question, answer in knowledge_base.items():
        question = question.lower()
        similarity = calculate_similarity(user_question, question)
        if similarity > highest_similarity:
            best_match = answer
            highest_similarity = similarity

    return best_match

# Function to calculate similarity between two strings (for question matching)
def calculate_similarity(str1, str2):
    # Implement your similarity calculation logic here
    # This can be based on methods like Jaccard similarity, cosine similarity, or other NLP techniques
    # For simplicity, we'll use a basic approach (percentage of shared words)
    
    words1 = set(str1.split())
    words2 = set(str2.split())
    shared_words = words1.intersection(words2)
    
    # Calculate similarity as the percentage of shared words
    similarity = len(shared_words) / max(len(words1), len(words2))
    
    return similarity

# Main function for answering questions
def answer_question(user_question, knowledge_base):
    # Find the best-matching answer in the knowledge base
    best_answer = find_answer(user_question, knowledge_base)
    
    if best_answer:
        return best_answer
    else:
        return "I'm sorry, I don't have an answer for that question."

# Sample usage
if __name__ == "__main__":
    while True:
        user_question = input("You: ")
        if user_question.lower() == "exit":
            print("QA Engine: Goodbye!")
            break

        response = answer_question(user_question, knowledge_base)
        print("QA Engine:", response)
