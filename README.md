# 🌍 Air Pollution Analysis & PM2.5 Prediction 🚀

A powerful machine learning web app that **predicts PM2.5 pollution levels** using air quality indicators like PM10, NO₂, SO₂, and O₃. Built with **Python**, **Flask**, and **RandomForestRegressor**, this project empowers governments, researchers, and citizens to fight air pollution with data.

---

## 🔥 Live Demo

> ⚙️ Run locally: `python src/app.py`  
> 💡 Send POST request to `/predict` with input features  
> 💬 Get back predicted PM2.5 levels instantly!

---

## 📈 Features

✅ Predicts dangerous **PM2.5** levels with high accuracy  
✅ Trained on real-world pollution data  
✅ RESTful Flask API — easy to integrate  
✅ Built with **Random Forest**, no complex tuning needed  
✅ Easily extendable to include more pollutants or time series  

---

## 💻 Tech Stack

| Tech | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data cleaning & preprocessing |
| Scikit-learn | Machine Learning (RandomForestRegressor) |
| Flask | Web backend & REST API |
| Joblib | Saving & loading ML models |
| Postman | API testing |
| Jupyter | Prototyping & EDA |
| Matplotlib / Seaborn | Visualization |

---

## 📂 Project Structure

```
air_pollution_analysis_prediction/
│
├── data/
│   ├── air_quality.csv                # Raw dataset
│   └── processed_air_quality.csv      # Cleaned dataset used for training
│
├── src/
│   ├── data_preprocessing.py          # Cleans and prepares the data
│   ├── model_training.py              # Trains and saves the ML model
│   ├── air_quality_model.pkl          # Trained model (Random Forest)
│   └── app.py                         # Flask web server
│
├── README.md                          # You’re reading it!
└── requirements.txt                   # Python dependencies
```

---

## 📊 How it Works

1. Preprocesses air quality data (drop missing, format columns)
2. Trains `RandomForestRegressor` using `PM10`, `NO₂`, `SO₂`, `O₃`
3. Saves model to `.pkl` using `joblib`
4. Flask app loads model and exposes `/predict` endpoint
5. Sends predictions back to frontend/postman

---

## 🧪 Example API Usage (Postman)

- **URL:** `http://127.0.0.1:5000/predict`  
- **Method:** POST  
- **Body (raw JSON):**
```json
[
  { "pm10": 55, "no2": 20, "so2": 10, "o3": 30 },
  { "pm10": 80, "no2": 35, "so2": 15, "o3": 45 }
]
```
- **Response:**
```json
{
  "predictions": [27.52, 39.01]
}
```

---

## 📌 Requirements

- Python 3.8+
- pip packages in `requirements.txt`
```bash
pip install -r requirements.txt
```

---

## 📚 Future Improvements

- Add support for time series forecasting
- Integrate a dashboard with charts (using Streamlit or React)
- Deploy using Docker + Render or Railway
- Live data API integration (CPCB or WAQI)
- Mobile notifications when PM2.5 is dangerous

---

## 🧠 Inspiration

PM2.5 is linked to millions of premature deaths worldwide. This project proves that **data + machine learning** can be used to **save lives**. It's designed to help researchers, cities, and citizens take timely action.

---

## 🤝 Contributing

Have ideas? Want to extend the model? Feel free to fork, PR, or raise an issue.

---

## 🛡️ License

MIT License — use it freely and responsibly.

---

## ⭐ Final Words

> "This isn’t just a data project. It’s a breath of fresh air — literally."

Made with ❤️ by [Your Name]