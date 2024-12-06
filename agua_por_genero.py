import pandas as pd
import matplotlib.pyplot as plt

file_path = "./gym_members_exercise_tracking_synthetic_data.csv"
data = pd.read_csv(file_path)

avg_water_intake = data.groupby('Gender')['Water_Intake (liters)'].mean()

plt.figure(figsize=(10, 6))
avg_water_intake.plot(kind='bar', color=['lightcoral', 'lightblue'])
plt.title("Consumo Médio de Água por Gênero", fontsize=16)
plt.xlabel("Gênero", fontsize=12)
plt.ylabel("Consumo Médio de Água (litros)", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("agua_por_genero.png")
plt.show()