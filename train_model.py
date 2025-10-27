import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib  ###### (joblib is used to save and load trained machine learning models efficiently, especially when they contain large numpy arrays.)#######

df = pd.read_csv("heart.csv")

####### Split into features and label #########
X = df.drop("target", axis=1)
y = df["target"]

####### Scale features ##########
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

######## Train-test split #########
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

####### Train Logistic Regression model ##########
model = LogisticRegression()
model.fit(X_train, y_train)

####### Evaluate model #######
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\n✅ Model Trained Successfully!")
print(f"📊 Accuracy: {accuracy * 100:.2f}%")

####### Save model and scaler using joblib #########
joblib.dump(model, "model_joblib.pkl")
joblib.dump(scaler, "scaler_joblib.pkl")

print("\n💾 model_joblib.pkl and scaler_joblib.pkl saved successfully!")
