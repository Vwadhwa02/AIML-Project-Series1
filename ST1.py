import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import time

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def timee():
    return str(time.localtime().tm_hour)+" : "+str(time.localtime().tm_min)

#tm_year=2024, tm_mon=5, tm_mday=2
def datee():
    return str(time.localtime().tm_year)+" / "+str(time.localtime().tm_mon)+" / "+str(time.localtime().tm_mday)

# Define questions and answers
qa = {
    "name?": "My name is Claude, the Anthropic chatbot.",
    "how are you?": "I'm doing well, thanks for asking!",
    "weather": "I don't actually have access to real-time weather data.",
    "time": "Right Now Time is "+str(timee()),
    "date":"Right Now Time is "+str(datee()),
    "joke": "Why don't scientists trust atoms? Because they make up everything!" # type: ignore
}

# Preprocess the questions for matching
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

preprocessed_questions = {' '.join([stemmer.stem(word) for word in re.sub(r'[^a-zA-Z\s]', '', question).lower().split() if word not in stop_words]): answer for question, answer in qa.items()}

def preprocess_question(question):
    return ' '.join([stemmer.stem(word) for word in re.sub(r'[^a-zA-Z\s]', '', question).split() if word not in stop_words])

def handle_query(question):
    preprocessed_question = preprocess_question(question)
    
    if preprocessed_question in preprocessed_questions:
        response=preprocessed_questions[preprocessed_question]
        return preprocessed_questions[preprocessed_question]
    else:
        return "I'm sorry, I couldn't find an answer to your question."
    

def main():
    
    st.title("Super Q&A Bot")
    st.write("Welcome!")

    user_input = st.chat_input("Please enter your question:")
    answers=[]
    if user_input:
        response = handle_query(user_input)
        answers.append(response)
        st.write(answers)

if __name__ == "__main__":
    main()