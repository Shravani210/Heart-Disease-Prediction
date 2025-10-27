import joblib

####### Load saved model and scaler ########
model = joblib.load("model_joblib.pkl")
scaler = joblib.load("scaler_joblib.pkl")

sample_input = [[63,1,3,145,233,1,0,150,0,2.3,0,0,1]]

sample_scaled = scaler.transform(sample_input)

result = model.predict(sample_scaled)[0]

print("\n🔍 Prediction Result:")
if result == 1:
    print("💔 High Risk of Heart Disease")
else:
    print("❤️ Low Risk of Heart Disease")
