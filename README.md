# 💡 Insurance Cost Prediction Web App

### 🚀 Machine Learning + Flask + Modern UI

The **Insurance Cost Prediction** project is a **machine learning-powered web application** built using **Flask**.  
It predicts an individual's **medical insurance cost** based on key personal factors such as **age**, **BMI**, **number of children**, **smoking status**, **gender**, and **region**.  

This project blends **data science** with **modern web design**, offering a clean, animated, and responsive interface for real-time predictions.  

---

## 🧠 Features

- 🧩 **Machine Learning Model** trained on a real-world insurance dataset  
- ⚙️ **End-to-End Pipeline:** Data ingestion → Preprocessing → Model prediction  
- 💻 **Flask Backend:** Lightweight Python web framework for easy deployment  
- 🎨 **Modern Frontend:** Animated, responsive UI built with HTML, CSS, and JavaScript  
- 🔮 **Instant Predictions:** Get real-time insurance cost estimates  
- 🌐 **Dual Interface:**
  - Web form via UI
  - JSON-based API endpoint (`/predict`) for integration with other systems  

---

## 🏗️ Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML5, CSS3, JavaScript (ES6) |
| **Backend** | Flask (Python) |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Model Used** | Linear Regression / Random Forest Regressor |
| **Version Control** | Git & GitHub |
| **Deployment Ready** | Render / Heroku / AWS Compatible |

---

## 🧩 Folder Structure

insurance_cost_prediction/
│
├── app.py # Flask main application
├── requirements.txt # Dependencies
├── data/ # Dataset folder
│ └── insurance.csv
├── src/ # Source code
│ ├── components/ # Data ingestion & transformation
│ ├── pipeline/ # Prediction pipeline
│ ├── constant/ # File paths and constants
│ └── logger.py
├── templates/
│ └── index.html # Frontend HTML page
├── static/
│ ├── style.css # CSS animations and design
│ └── script.js # Button animation and interactivity
└── artifacts/ # Saved outputs and model files


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Aditya-raj123/insurance_cost_prediction.git
cd insurance_cost_prediction
python -m venv myenv
myenv\Scripts\activate
source myenv/bin/activate
pip install -r requirements.txt
python app.py



