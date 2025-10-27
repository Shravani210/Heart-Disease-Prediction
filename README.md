# Heart Disease Prediction Using Machine Learning

This project predicts whether a person is likely to have heart disease based on medical attributes such as age, cholesterol level, blood pressure, etc. The model is trained using the UCI Heart Disease dataset and saved using joblib for future use.


## 🔍 Project Overview

Heart disease is a major global health issue. Early risk detection can save lives.  
This project uses a **Logistic Regression** classification model to determine the presence of heart disease (1 = Yes, 0 = No).


## 📂 Project Structure

Heart Disease Prediction 
- ├── heart.csv                      # Dataset
- ├── heart_disease_model.py         # Model training + EDA + saving model
- ├── model.joblib                   # Saved ML model (generated after training)
- └── README.md                      # Project Explanation (this file)


## 📊 Dataset Information

The dataset contains patient health-related features:

| Feature      | Meaning                                              |
|--------------|------------------------------------------------------|
| age          | Age of the patient                                   |
| sex          | Gender (1 = Male, 0 = Female)                        |
| cp           | Chest pain type                                      |
| trestbps     | Resting blood pressure                               |
| chol         | Serum cholesterol                                    |
| fbs          | Fasting blood sugar                                  |
| restecg      | Resting electrocardiographic results                 |
| thalach      | Maximum heart rate achieved                          |
| exang        | Exercise induced angina                              |
| oldpeak      | ST depression induced by exercise                    |
| slope        | Slope of peak exercise ST segment                    |
| ca           | Number of major vessels colored by fluoroscopy       |
| thal         | Thalassemia                                          |
| target       | 1 = Heart disease, 0 = No heart disease              |


## 🧠 Model Used

- Logistic Regression (Classification)
- StandardScaler applied to normalize features
- Model saved using joblib (`model.joblib`)


## 📈 Visualizations Included (EDA)

- Correlation Heatmap
- Age Distribution Plot
- Heart Disease Count Plot
- Chest Pain Type vs Target Comparison

These help understand the feature impact on heart disease.


## ▶️ How to Run

### Step 1: Install Dependencies
pip install pandas numpy seaborn matplotlib scikit-learn joblib

### Step 2: Run the Model Training File
python heart_disease_model.py

After running, it will:

- ✅ Show graphs
- ✅ Train the ML model
- ✅ Save the model as model.joblib


## 🖥️ Output

PS C:\Users\Shravani\OneDrive\Desktop\PROJECTS\Heart Disease Prediction> python train_model.py 

✅ Model Trained Successfully!
📊 Accuracy: 79.51%

💾 model_joblib.pkl and scaler_joblib.pkl saved successfully!

PS C:\Users\Shravani\OneDrive\Desktop\PROJECTS\Heart Disease Prediction> python predict.py
C:\Users\Shravani\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\validation.py:2749: UserWarning: X does not have valid feature names, but StandardScaler was fitted with feature names
  warnings.warn()

🔍 Prediction Result:
💔 High Risk of Heart Disease

PS C:\Users\Shravani\OneDrive\Desktop\PROJECTS\Heart Disease Prediction> python heart_disease_model.py
   age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
0   52    1   0       125   212    0        1      168      0      1.0      2   2     3       0
1   53    1   0       140   203    1        0      155      1      3.1      0   0     3       0
2   70    1   0       145   174    0        1      125      1      2.6      0   0     3       0
3   61    1   0       148   203    0        1      161      0      0.0      2   1     3       0
4   62    0   0       138   294    1        1      106      0      1.9      1   3     2       0


## 🎯 Project Result

The Logistic Regression model was able to successfully classify heart disease based on input medical features. This project demonstrates understanding of:

- Data preprocessing
- EDA & visualization
- Model training & evaluation
- Saving & loading ML models


## 📝 Future Enhancements

| Improvement           | Description                                      |
| --------------------- | ------------------------------------------------ |
| GUI/Web App           | Add Streamlit or Flask interface for user inputs |
| More Models           | Try SVM, Random Forest, XGBoost for comparison   |
| Hyperparameter Tuning | Improve accuracy using GridSearchCV              |

