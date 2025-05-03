### 📄 `README.md`

```markdown
# 🚗 Parking Space Occupancy Prediction

This project predicts whether a parking space is **occupied or not** based on 23 numerical features using ensemble learning models. A fully responsive **Streamlit web application** is included for real-time predictions.

---

## 📂 Project Structure

```

.
├── park\_space\_prediction.ipynb     # Jupyter Notebook for data processing and model training
├── ensemble.pkl                    # Trained ensemble model (Voting Classifier)
├── scaler.pkl                      # StandardScaler used during preprocessing
├── streamlit.py                          # Streamlit UI application
├── requirements.txt                # List of Python dependencies
└── README.md                       # Project documentation

````

---

## 🧠 Model Overview

- **Algorithms Used**:
  - Decision Tree
  - Random Forest
  - XGBoost
  - Combined using VotingClassifier
- **Preprocessing**: StandardScaler normalization
- **Performance**:
  - Decision Tree: 94% accuracy
  - Random Forest: 95% accuracy
  - XGBoost: 98% accuracy
  - Voting Ensemble: 96% accuracy (robust generalization)

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/parking-prediction-app.git
cd parking-prediction-app
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare the Model

If not already present, save your trained model and scaler:

```python
import joblib
joblib.dump(ensemble, 'ensemble.pkl')
joblib.dump(scaling, 'scaler.pkl')
```

Make sure both `ensemble.pkl` and `scaler.pkl` are in the root directory.

### 4. Launch the Streamlit App

```bash
streamlit run streamlit.py
```

Open your browser to the local URL provided by Streamlit (e.g., `http://localhost:8501/`).

---

## 🌐 App Features

* Responsive layout for desktop and mobile
* Input fields for 23 numerical features
* Instant prediction of parking space status:

  * `Occupied`
  * `Not Occupied`

---

## ⚙️ Requirements

Below are the key packages used:

```
streamlit
numpy
pandas
xgboost
scikit-learn
joblib
```

To install them:

```bash
pip install -r requirements.txt
```

## 📌 Notes

* This project assumes pre-cleaned numerical input features.
* Future updates may include location, time, or image-based prediction.


## ✍️ Author

**Prince Kumar Gupta**
Machine Learning & Data Science Enthusiast
📫 Email: \[[princegupta1726@gmail.com](mailto:princegupta1726@gmail.com)]
🔗 GitHub: [https://github.com/CodeNobility](https://github.com/CodeNobility)

