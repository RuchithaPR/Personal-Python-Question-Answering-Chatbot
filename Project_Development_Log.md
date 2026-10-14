# Personal Python Question-Answering Chatbot
## Project Development Log

### Day 1 — Environment Setup and Initial Implementation
**Date:** 13 October 2026

### 1. Goal
Set up the Python environment and build the initial version of the chatbot.

### 2. Work Completed
- Created the project folder.
- Created a Python virtual environment.
- Installed Streamlit and scikit-learn.
- Created chatbot.py for chatbot logic.
- Created app.py for the user interface.
- Created requirements.txt for dependencies.
- Implemented question matching using TF-IDF and cosine similarity.
- Added a similarity threshold to reject some unrelated questions.
- Ran the Streamlit application locally.
- Initialized Git and created the first commit.
- Published the initial project files to GitHub.

### 3. Technical Concepts Introduced
- Python virtual environments
- TF-IDF vectorization
- Cosine similarity
- Similarity thresholds
- Streamlit
- Git and GitHub

### 4. Files Created
- chatbot.py
- app.py
- requirements.txt
- .gitignore
- Chatbot_5Day_Tracker.xlsx

### 5. Testing
- Tested Python-related questions.
- Tested machine-learning-related questions.
- Tested an unrelated question.
- Observed the similarity scores returned by the chatbot.

### 6. Pending Tasks
- Test the chatbot with 15–20 questions.
- Understand the code line by line.
- Learn TF-IDF and cosine similarity in detail.
- Improve question matching and rejection of unrelated questions.

### 7. Next Session
Continue learning the existing code and improve the chatbot's question-matching logic.

# Day 2: Knowledge Base Development and Testing
**Date:** October 14, 2026  
**Project:** Personal Python Question-Answering Chatbot  
**Status:** Completed

## 1. Objectives
- Expand the chatbot's knowledge base.
- Improve question matching and answer retrieval.
- Test the chatbot's ability to answer known questions and reject unrelated questions.
- Verify the Streamlit web application.
- Save and push project updates to GitHub.

## 2. Work Completed

### Knowledge Base Development
Expanded the knowledge base from 5 to 15 question-answer pairs.

Topics covered:
- Python programming
- Variables and functions
- Lists, loops, and dictionaries
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Deep Learning
- Neural Networks
- Supervised and Unsupervised Learning
- Data Science
- Natural Language Processing (NLP)
- Datasets

### Question Matching
Used TF-IDF vectorization to convert stored questions into numerical representations.

Used cosine similarity to compare the user's question with the questions stored in the knowledge base.

Updated the similarity threshold from 0.5 to 0.65 to improve the rejection of unrelated questions.

### Unknown-Question Handling
Tested the chatbot's response to questions outside its knowledge base.

The chatbot successfully rejected the tested unrelated question when its similarity score fell below the configured threshold.

### Testing Results

| Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|
| Deep learning question | Return the relevant answer | Correct answer returned | Passed |
| Python dictionary question | Return the relevant answer | Correct answer returned | Passed |
| Quantum physics question | Reject the unrelated question | Unknown-question response returned | Passed |
| Streamlit application | Launch successfully in the browser | Application running on localhost | Passed |

Note: Testing was performed using three sample questions. Additional testing with varied question phrasing and edge cases is required.

## 3. Technologies Used
- Python
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- NumPy
- Streamlit
- Git
- GitHub

## 4. Application Verification
Successfully launched the Streamlit application locally using:

    streamlit run app.py

Verified that the application opened in the browser and was running correctly.

## 5. GitHub Update
Committed and pushed the Day 2 changes to the remote GitHub repository.

Repository:
https://github.com/RuchithaPR/Personal-Python-Question-Answering-Chatbot

Branch: master

Commit ID: 170b8c7

Commit Message:
"Complete Day 2 chatbot knowledge base and testing"

Files committed:
- chatbot.py
- Project_Development_Log.md

## 6. Challenges and Improvements
- Observed that an unrelated question could receive an incorrect answer when its similarity score exceeded the original threshold.
- Increased the similarity threshold from 0.5 to 0.65.
- Verified that the tested unrelated question was rejected after the change.

A higher threshold may also reject some valid questions, so further testing and threshold tuning may be required.

## 7. Day 2 Outcome
Successfully expanded the chatbot's knowledge base, improved similarity-based answer rejection, tested the core question-answering functionality, verified the Streamlit interface, and updated the GitHub repository.

## 8. Plan for Day 3
- Review the next tasks specified in the Edufyi project timetable.
- Continue improving the chatbot according to the project requirements.
- Test additional question variations and edge cases.
- Update the project development log and GitHub repository.