import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)
    # Example: predict 'pm2_5' using other numeric features
    X = df.drop(['pm2_5', 'date'], axis=1)
    y = df['pm2_5']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    joblib.dump(model, model_path)
    print(f"Model trained with R^2 score: {score:.2f}")
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model('data/processed_air_quality.csv', 'src/air_quality_model.pkl')
