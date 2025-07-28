from src.main import read_scores, calculate_average

def test_calculate_average():
    df = read_scores("data/scores.csv")
    avg = calculate_average(df)
    assert round(avg, 1) == 16.8
