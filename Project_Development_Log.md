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

## Day 3: Knowledge Base Expansion and Testing

### Objectives
- Expand the chatbot's knowledge base with additional Python, AI, and Machine Learning questions.
- Improve the chatbot's ability to answer a wider range of questions.
- Test the chatbot using different questions and evaluate its responses.

### Work Completed
- Expanded the knowledge base with additional question-and-answer pairs.
- Added questions covering Python lists, loops, dictionaries, functions, and variables.
- Added questions covering deep learning, data science, neural networks, supervised learning, unsupervised learning, and natural language processing.
- Used TF-IDF vectorization to represent questions numerically.
- Used cosine similarity to compare user questions with questions stored in the knowledge base.
- Tested the chatbot with different questions to verify its responses.
- Checked how the chatbot handles questions that are not sufficiently related to its knowledge base.

### Technologies Used
- Python
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Outcome
Successfully expanded the chatbot's knowledge base and tested its question-matching functionality. The chatbot can answer supported questions and reject questions when it cannot find a sufficiently suitable match.

### Status
Completed

## Day 4: Chatbot Improvements and Tuning

### Objectives
- Evaluate the chatbot's responses to differently worded questions.
- Identify and correct incorrect question matching.
- Improve the chatbot's ability to recognize user intent.
- Test the chatbot using relevant and unrelated questions.

### Work Completed

1. Tested the chatbot with differently worded questions, including:
   - Can you explain machine learning to me?
   - Tell me about neural networks.
   - How do I store a value in Python?
   - What is deep learning?

2. Tested the chatbot with an unrelated question:
   - What is the capital of France?

3. Identified a question-matching issue:
   - The chatbot initially returned an incorrect answer about functions when asked how to store a value in Python.
   - The incorrect answer was accepted with a similarity score of 0.68.

4. Adjusted the similarity threshold from 0.65 to 0.70 to make the chatbot more selective when accepting matches.

5. Improved the knowledge base by updating the variable-related question to include an alternative way of asking about storing values in Python.

6. Tested the variable-related question again and confirmed that the chatbot returned the appropriate answer.

7. Retested the deep learning question and confirmed that the chatbot continued to provide the expected answer.

8. Verified that the chatbot dashboard continued to function using Streamlit.

### Improvements Made
- Increased the similarity threshold to 0.70.
- Updated the variable-related knowledge-base entry to improve question matching.
- Improved the answer provided for questions about storing values in Python.
- Tested the chatbot's ability to reject unrelated questions.

### Technologies Used
- Python
- Streamlit
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Outcome
Improved the chatbot's handling of questions about Python variables and verified its responses to several supported questions. Testing also confirmed that unrelated questions can be rejected.

### Status
Technical improvements and testing completed. Documentation and final GitHub updates pending.

## Day 5: Final Polishing and Submission Preparation

### Objectives
- Perform final testing of the chatbot.
- Verify the application interface and functionality.
- Review the project files.
- Prepare the project for GitHub submission.

### Work Completed

1. Tested the chatbot with the question "What is Python?" and verified that it returned the expected explanation.

2. Tested the question "How do I store a value in Python?" and verified that the chatbot provided an appropriate answer about variables and the assignment operator.

3. Tested the unrelated question "What is the capital of France?" and verified that the chatbot rejected the question rather than providing an unrelated answer.

4. Verified that the Streamlit dashboard launched and functioned correctly.

5. Reviewed the project structure and confirmed that the required project files were present.

6. Reviewed the knowledge base, question-matching logic, and similarity threshold improvements made during development.

### Technologies Used
- Python
- Streamlit
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Outcome
Completed the final functional tests and verified the chatbot dashboard and essential project files. The project is prepared for the final GitHub update and submission.

### Status
Final testing completed. GitHub update and submission verification pending.