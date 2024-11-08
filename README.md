Fake News Detection Model
This project aims to develop a machine learning model that can detect fake news articles. By leveraging natural language processing (NLP) and various machine learning algorithms, this model classifies news as either fake or real based on its content. This model was developed as part of an academic project to apply machine learning in the detection of misinformation.

Overview
The rise of fake news has created significant challenges in ensuring that people are informed with factual information. This project aims to address this issue by building an AI-based fake news detector that analyzes the text of articles and predicts their authenticity.

Dataset
The dataset used in this project contains labeled news articles classified as fake or real. It includes fields for the article text, headlines, and the target label. The dataset is stored in the data/ directory and can be downloaded from:
Kaggle - Fake and Real News Dataset
Kaggle - Fake News Detection

Model Training
Multiple machine learning models are trained and evaluated to detect fake news, including:

Logistic Regression
Support Vector Machine (SVM)
Naive Bayes
Random Forest
Each model is trained on the processed text data, and performance is measured to select the best model for fake news detection.

Model Evaluation
Evaluation metrics for model performance include:

Accuracy: Percentage of correctly classified news articles
Precision and Recall: To balance false positives and false negatives

Usage
After training, the model can be used to classify new articles as either fake or real.
