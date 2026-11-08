import pandas as pd

import grades

db = {
    "Алия": [90, 85, 100],
    "Тимур": [70, 65, 80],
    "Дана": [95, 100, 90],
    "Ерлан": [50, 60, 45],
}

df = pd.DataFrame({"name": list(db), "avg": [grades.average(s) for s in db.values()]})
df["grade"] = df["avg"].apply(grades.grade)
print(df.sort_values("avg", ascending=False).to_string(index=False))
print("Средний балл группы:", round(df["avg"].mean(), 2))
