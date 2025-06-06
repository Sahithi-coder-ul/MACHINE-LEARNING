

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
messages = [
    "Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/123456 to claim now.",
    "Hi, can we reschedule our meeting?",
    "URGENT! Your mobile number has been selected for a $5000 prize!",
    "Hey, just checking in. How are you?",
    "You have been selected for a free cruise to the Bahamas!",
    "Don't forget to bring your notes to the study group.",
    "Win money now!!! Click this link to get rich quick!",
    "Let’s catch up over coffee tomorrow.",
]

labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

# Step 1: Split data
X_train, X_test, y_train, y_test = train_test_split(messages, labels, test_size=0.3, random_state=42)

# Step 2: Convert text to numeric vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 3: Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 4: Predict
y_pred = model.predict(X_test_vec)

# Step 5: Evaluation
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=["Not Spam", "Spam"]))

# Step 6: Try your own message
user_msg = input("\n💬 Enter your own message to check if it's spam: ")
user_msg_vec = vectorizer.transform([user_msg])
prediction = model.predict(user_msg_vec)

print("📩 Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")

