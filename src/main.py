import pandas as pd

def read_scores(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_average(df):
    return df["score"].mean()

if __name__ == "__main__":
    df = read_scores("data/scores.csv")
    avg = calculate_average(df)
    print("Average score:", round(avg, 2))
