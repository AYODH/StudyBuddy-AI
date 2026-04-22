import time

def summarize_text(text: str) -> str:
    time.sleep(1)  # Simulate API delay
    return """📝 SUMMARY
- Machine Learning (ML) is a subset of AI that enables systems to learn from data without explicit programming
- Three main types: Supervised Learning, Unsupervised Learning, and Reinforcement Learning
- Supervised learning uses labelled data; unsupervised finds hidden patterns; reinforcement learns via rewards
- Overfitting occurs when a model memorises training data but fails on new data
- Underfitting occurs when a model is too simple to capture underlying patterns
- Common algorithms include Linear Regression, Decision Trees, SVM, and Neural Networks
- Model performance is measured using Accuracy, Precision, Recall, F1 Score, and MSE

🔑 KEY CONCEPTS
1. Supervised Learning – Training on labelled input-output pairs to predict outcomes
2. Overfitting – Model performs well on training data but poorly on unseen data
3. Feature – An input variable used by the model to make predictions
4. F1 Score – Harmonic mean of precision and recall; useful for imbalanced datasets
5. Neural Network – A model inspired by the human brain, powerful for images and text

🃏 FLASHCARDS
Q: What is the difference between supervised and unsupervised learning?
A: Supervised learning uses labelled data; unsupervised learning finds patterns in unlabelled data.

Q: What is overfitting and how can it be fixed?
A: Overfitting is when a model memorises training data. Fix: more data, regularisation, simpler model.

Q: What does the F1 score measure?
A: It measures the balance between precision and recall, useful when data is imbalanced.

Q: Name three common ML algorithms.
A: Linear Regression, Decision Trees, Random Forest, SVM, Neural Networks (any three).

Q: What is the purpose of splitting data into training and testing sets?
A: To evaluate how well the model generalises to new, unseen data."""


def generate_quiz(text: str) -> str:
    time.sleep(1)
    return """Q1: What is Machine Learning?
A) A type of hardware used in computers
B) A subset of AI that enables systems to learn from data
C) A programming language for data analysis
D) A database management system
Answer: B

Q2: Which type of learning uses labelled data?
A) Unsupervised Learning
B) Reinforcement Learning
C) Supervised Learning
D) Transfer Learning
Answer: C

Q3: What is overfitting?
A) When a model is too simple to learn patterns
B) When a model learns training data too well, including noise
C) When a model has too few parameters
D) When training data is insufficient
Answer: B

Q4: Which metric is best for imbalanced datasets?
A) Accuracy
B) Mean Squared Error
C) F1 Score
D) R-squared
Answer: C

Q5: What is a feature in machine learning?
A) A bug in the model
B) The final output of the model
C) An input variable used to make predictions
D) A type of neural network layer
Answer: C"""


def chat_with_notes(text: str, user_question: str) -> str:
    time.sleep(1)
    question_lower = user_question.lower()

    if "overfitting" in question_lower:
        return "Based on your notes: Overfitting occurs when the model learns the training data too well, including noise and outliers. It results in high training accuracy but poor performance on new data. Fixes include: more training data, regularisation, simpler model, or dropout."
    elif "supervised" in question_lower:
        return "Based on your notes: Supervised Learning is a type of ML where the model is trained on labelled data (input-output pairs). Examples include spam detection, house price prediction, and image classification."
    elif "unsupervised" in question_lower:
        return "Based on your notes: Unsupervised Learning finds hidden patterns in unlabelled data. Examples include customer segmentation, anomaly detection, and topic modelling."
    elif "algorithm" in question_lower or "algorithms" in question_lower:
        return "Based on your notes: Common ML algorithms include Linear Regression, Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM), Neural Networks, and K-Means Clustering."
    elif "f1" in question_lower:
        return "Based on your notes: F1 Score is the harmonic mean of precision and recall. It is particularly useful for imbalanced datasets where accuracy alone can be misleading."
    else:
        return f"Based on your notes: That's a great question about '{user_question}'. The notes cover ML types (supervised, unsupervised, reinforcement), key algorithms, overfitting/underfitting, and evaluation metrics. Try asking about a specific topic like overfitting, supervised learning, or algorithms!"
