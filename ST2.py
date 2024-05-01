import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define college admission-related questions and answers
admission_qa = {
    'admission requirements': 'The admission requirements vary depending on the program and university. Generally, you need to submit your transcripts, test scores (SAT/ACT), a personal statement, and letters of recommendation.',
    'application deadline': 'Application deadlines differ for each university and program. Most universities have early action or early decision deadlines around November, and regular decision deadlines around January or February.',
    'application fee': 'Application fees range from $50 to $100 for most universities in the United States. Some universities may waive the fee for students with financial need.',
    'financial aid': 'Financial aid is available in the form of scholarships, grants, student loans, and work-study programs. You need to complete the Free Application for Federal Student Aid (FAFSA) to be eligible for federal aid.',
    'campus visit': 'Campus visits are highly recommended as they give you a chance to experience the university environment firsthand. You can attend information sessions, take a campus tour, and sometimes sit in on a class.'
}

# Preprocess the questions for matching
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

preprocessed_questions = {' '.join([stemmer.stem(word) for word in re.sub(r'[^a-zA-Z\s]', '', question).lower().split() if word not in stop_words]): answer for question, answer in admission_qa.items()}

def preprocess_question(question):
    return ' '.join([stemmer.stem(word) for word in re.sub(r'[^a-zA-Z\s]', '', question).split() if word not in stop_words])

def handle_query(question):
    preprocessed_question = preprocess_question(question)
    if preprocessed_question in preprocessed_questions:
        return preprocessed_questions[preprocessed_question]
    else:
        return "I'm sorry, I couldn't find an answer to your question. Please try rephrasing your question or asking something else related to college admission."

def main():
    st.title("College Admission Q&A Bot")
    st.write("Welcome! I'm here to help you with your college admission queries.")

    user_input = st.text_input("Please enter your question:")
    if user_input:
        response = handle_query(user_input)
        st.write(response)

if __name__ == "__main__":
    main()