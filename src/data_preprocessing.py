import pandas as pd

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)
    # Example preprocessing: drop NA, encode dates
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    # Add more features as needed
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    preprocess('data/air_quality.csv', 'data/processed_air_quality.csv')
