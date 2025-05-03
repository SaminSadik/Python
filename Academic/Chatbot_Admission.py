import spacy
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy's pre-trained model
nlp = spacy.load('en_core_web_md')

# Optimized training data: answers as keys, list of questions as values
training_data = {
    "Hi, what would you like to know about Admission in the Department of CSE?": [
        "Hi", "help me", "have some questions"
    ],
    "You can apply online through the university's admission portal.": [
        "How to apply?",  "How do I get admission in the Department of CSE?", 
        "How to get admission?", "How I apply?"
    ],
    "The admission requirements and study costs can be found in the university's website": [
        "What do I need for addmission?",
        "What documents do I need to apply?", "documents required for admission", 
        "What are the Fees?", "What is the cost", "How costly is it?"
    ],
    "The Department of CSE is arguably the best department in our University": [
        "Is the CSE Department Good?", "How is the Dept of CSE?"
    ],
    "You're welcome! Feel free to ask if you have more questions.": [
        "Thanks", "Thank you"
    ]
}

# Function to compute Cosine Similarity using spaCy's word vectors
def get_cosine_similarity(text1, text2):
    vec1 = nlp(text1).vector
    vec2 = nlp(text2).vector
    return cosine_similarity([vec1], [vec2])[0][0]

def is_relevant_question(user_input):
    keywords = ['admission', 'apply', 'documents', 'cost', 'cse', 'question', 'help', 'hi', 'thank']
    return any(keyword in user_input.lower() for keyword in keywords)

# Main chatbot loop
def chat():
    print("This bot will answer all your Admission related queries! [Type 'bye' to end the conversation.]")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['bye']:
            print("AdmissionHelpBot: Goodbye!")
            break
        if not is_relevant_question(user_input):
            print("AdmissionBot: Sorry, I can only help with questions about the CSE department admission process.")
            continue

        # Find the best matching question based on cosine similarity
        best_match_score = 0
        best_match_answer = ""

        for answer, questions in training_data.items():
            for question in questions:
                similarity = get_cosine_similarity(user_input, question)
                if similarity > best_match_score:
                    best_match_score = similarity
                    best_match_answer = answer

        # Provide the best matching answer if similarity threshold is met
        if best_match_score >= 0.8:
            print(f"AdmissionHelpBot: {best_match_answer}")
        else:
            print("AdmissionHelpBot: Sorry, can you please rephrase your question?")

chat() # Start the chatbot
