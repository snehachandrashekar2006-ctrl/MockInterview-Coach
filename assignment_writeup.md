# Assignment 1: Company-Smart Mock Interview Coach

## Abstract
Company-Smart Mock Interview Coach is a demo interview-preparation application. It lets a student select a company style and job role, answer sample interview questions, and receive a keyword-based score with feedback. The prototype demonstrates the basic interview practice workflow. It does not use an institution's ten-year interview archive because that data has not been supplied; such an archive can be integrated later.

## Problem Statement
To develop a mock interview coaching application that presents role-based interview questions, collects candidate answers, evaluates answer coverage using keywords, and provides a score and feedback report.

## Algorithm
1. Start the application.
2. Display company-style and job-role selection options.
3. Load a sample question set for the selected role.
4. Display the questions and collect the candidate's answers.
5. Compare each answer with the question's expected keywords.
6. Calculate a demo score based on the matched keyword ratio.
7. Display scores and suggestions for improvement.
8. Allow the candidate to download the feedback report as JSON.
9. Stop.

## Program
The implementation is in `app.py`. It uses Streamlit to create the interface and Python keyword matching to calculate demo feedback. Install the dependency with `pip install -r requirements.txt` and run `streamlit run app.py`.

## Note
The scoring is a simple educational prototype, not a validated hiring assessment or a true AI model. The institutional interview archive can be connected when the dataset is available.
