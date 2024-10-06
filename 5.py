import pandas as pd

df = pd.read_csv('C:/Users/ROXANA CASTILLO/Desktop/354/gym_members_exercise_tracking.csv')

def normalize_manual(column):
    min_value = min(column)
    max_value = max(column)
    return [(value - min_value) / (max_value - min_value) for value in column]

normalized_weight = normalize_manual(df['Weight (kg)'])
normalized_height = normalize_manual(df['Height (m)'])
normalized_bmi = normalize_manual(df['BMI'])

def l1_penalty(weights):
    return sum(abs(w) for w in weights)

def l2_penalty(weights):
    return sum(w ** 2 for w in weights)

l1_weight = l1_penalty(normalized_weight)
l2_weight = l2_penalty(normalized_weight)

print(l1_weight, l2_weight)
