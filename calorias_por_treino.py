import pandas as pd
import matplotlib.pyplot as plt

file_path = "./gym_members_exercise_tracking_synthetic_data.csv"
data = pd.read_csv(file_path)

avg_calories = data.groupby('Workout_Type')['Calories_Burned'].mean().sort_values()

plt.figure(figsize=(10, 6))
avg_calories.plot(kind='bar', color='skyblue')
plt.title("Calorias Médias Queimadas por Tipo de Treino", fontsize=16)
plt.xlabel("Tipo de Treino", fontsize=12)
plt.ylabel("Calorias Médias Queimadas", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("calorias_por_treino.png") 
plt.show()
