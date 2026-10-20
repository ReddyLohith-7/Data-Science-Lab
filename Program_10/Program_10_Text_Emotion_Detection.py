#==============================================================
# Name: B.Reddy Lohith
# Roll No: 23102A010287
# Branch: CSE(AI/ML)
# Section: B4
#==============================================================

#==============================================================
# Program 10: Text Emotion Detection
# Case Study: Detecting Emotions from Text Using Machine Learning
# AIM: To classify text into emotion categories using
# CountVectorizer and Multinomial Naive Bayes.
#==============================================================


# ============================================================
# IMPORT REQUIRED LIBRARIES
# ============================================================

# CountVectorizer converts text into numerical features.
from sklearn.feature_extraction.text import CountVectorizer

# MultinomialNB is used for text classification.
from sklearn.naive_bayes import MultinomialNB


# ============================================================
# CREATE SAMPLE TRAINING DATA
# ============================================================

texts = [
    "I am happy",
    "I am angry",
    "I feel sad",
    "I love this"
]

labels = [
    "happy",
    "angry",
    "sad",
    "happy"
]

print("=" * 60)
print("TRAINING DATA")
print("=" * 60)

for sentence, emotion in zip(texts, labels):
    print(f"Text: {sentence} --> Emotion: {emotion}")


# ============================================================
# TEXT VECTORIZATION
# ============================================================

vec = CountVectorizer()

# Convert text into numerical features.
X = vec.fit_transform(texts)

print("\n")
print("=" * 60)
print("VOCABULARY")
print("=" * 60)
print(vec.get_feature_names_out())

print("\n")
print("=" * 60)
print("VECTORIZED DATA")
print("=" * 60)
print(X.toarray())


# ============================================================
# TRAIN MACHINE LEARNING MODEL
# ============================================================

model = MultinomialNB()

# Train the model using text features and emotion labels.
model.fit(X, labels)

print("\nModel Training Completed Successfully")


# ============================================================
# TEST DATA
# ============================================================

new_text = ["I am so sad today"]

print("\n")
print("=" * 60)
print("TEST SENTENCE")
print("=" * 60)
print(new_text)

# Convert the new sentence using the learned vocabulary.
test = vec.transform(new_text)

print("\nVectorized Test Data:")
print(test.toarray())


# ============================================================
# PREDICTION
# ============================================================

prediction = model.predict(test)

print("\n")
print("=" * 60)
print("PREDICTED EMOTION")
print("=" * 60)
print(prediction[0])


# ============================================================
# ADDITIONAL TEST CASES
# ============================================================

sample_sentences = [
    "I love my friends",
    "I am angry with you",
    "I feel very sad",
    "Today I am happy"
]

print("\n")
print("=" * 60)
print("MULTIPLE PREDICTIONS")
print("=" * 60)

for sentence in sample_sentences:
    sample_vector = vec.transform([sentence])
    result = model.predict(sample_vector)
    print(f"{sentence} --> {result[0]}")


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n")
print("=" * 60)
print("TEXT EMOTION DETECTION COMPLETED")
print("=" * 60)
